import argparse
import decimal
import json
import logging
import os
import re
import shlex
import sys

DEBUG = False if "oDesktop" in dir() else True
MODULE_DIR_PARENT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(MODULE_DIR_PARENT)

from aedttest.logger import logger  # noqa: E402
from aedttest.logger import set_logger  # noqa: E402


def parse_args():
    """Parse arguments that were provided to the script when executed with RunScriptAndExit."""
    arg_string = ScriptArgument.replace('"', "")  # noqa: F821
    parser = argparse.ArgumentParser()
    parser.add_argument("--pyaedt-path")
    parser.add_argument("--logfile-path")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args(shlex.split(arg_string))
    return args.pyaedt_path, args.logfile_path, args.debug


def parse_args_debug():
    """Parse arguments that were provided to the script when the script is executed directly."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--desktop-version", default="2022.1")
    args = parser.parse_args()

    return args.desktop_version


log_level = logging.DEBUG
if not DEBUG:
    pyaedt_path, logfile_path, debug = parse_args()
    sys.path.insert(0, pyaedt_path)
    specified_version = None

    if not debug:
        log_level = logging.INFO
else:
    specified_version = parse_args_debug()
    logfile_path = os.path.join(MODULE_DIR_PARENT, "aedt_test_framework.log")

try:
    import pyaedt  # noqa: E402
    from pyaedt import get_pyaedt_app  # noqa: E402
    from pyaedt.desktop import Desktop  # noqa: E402
    from pyaedt.generic.general_methods import generate_unique_name  # noqa: E402
    from pyaedt.generic.report_file_parser import parse_rdat_file  # noqa: E402
except Exception as exc:
    set_logger(logging_file=logfile_path, level=log_level, pyaedt_module=None)
    logger.exception(str(exc))
    raise


set_logger(logging_file=logfile_path, level=log_level, pyaedt_module=pyaedt)

PROJECT_DICT = {"error_exception": [], "designs": {}}


class AedtTestException(Exception):
    """Base class for exceptions in this module."""


def parse_mesh_stats(mesh_stats_file, design_name, variation, setup_name):
    """Get the mesh element number.

    Parameters
    ----------
    mesh_stats_file : str
        Path of the mesh stats ``.mstat`` file.
    design_name : str
        Name of the design.
    variation : str
        Variation string.
    setup_name : str
        Name of the setup.

    Returns
    -------
    int
        Number of mesh elements.
    """

    with open(mesh_stats_file) as fid:
        lines = fid.readlines()

    for line in lines:
        if "Total number of mesh elements" in line:
            return int(line.strip().split(":")[1])
    else:
        PROJECT_DICT["error_exception"].append(
            "Design:{} Variation: {} Setup: {} has no mesh stats".format(design_name, variation, setup_name)
        )


def parse_profile_file(profile_file, design_name, variation, setup_name):
    """Get the simulation time.

    Parameters
    ----------
    profile_file : str
        Path of the profile file ``.prof``.
    design_name : str
        Name of the design.
    variation : str
        Variation string.
    setup_name : str
        Name of the setup.

    Returns
    -------
    simulation_time : str
        Elapsed simulation time.
    cell_number: int
        number of cells for Icepak
    """
    elapsed_time = ""
    cell_number = 0
    with open(profile_file) as file:
        for line in file:
            if "elapsed time" in line.lower():
                elapsed_time = line.lower()
            if "cells" in line.lower():
                val = re.match(r".*cells: (\d+)", line.lower()) or re.match(r".* (\d+) cells", line.lower())
                cell_number = int(val.group(1))

    if elapsed_time:
        split_line = elapsed_time.split("elapsed time")[1]

        simulation_time = re.findall(r"[0-9]*:[0-9][0-9]:[0-9][0-9]", split_line)[0]
        return simulation_time, cell_number
    else:
        PROJECT_DICT["error_exception"].append(
            ("Design:{} Variation:{} Setup:{} no elapsed time in file".format(design_name, variation, setup_name))
        )


def parse_value_with_unit(string):
    """Get the number and unit of a variation string.

    The number is truncated to 9 digits with scientific notation.

    Parameters
    ----------
    string : str
        Variation string which includes number and unit.

    Returns
    -------
    number : str
        String of number in format of 0.9e.
    unit : str
        Unit of the value.
    """
    units = ""
    precision = -9
    origin_string = string

    while string:
        try:
            number = float(string)
            d = decimal.Decimal(string)
            decimal_places = d.as_tuple().exponent
            if decimal_places < precision:
                return "{:0.9e}".format(number), units.strip()
            else:
                return string, units.strip()

        except ValueError:
            units = string[-1:] + units
            string = string[:-1]
    else:
        return origin_string, ""


def extract_data(desktop, project_dir, project_name, design_names):
    """Extract designs' data for a project.

    Parameters
    ----------
    desktop : pyaedt.desktop.Desktop
        ``pyaedt`` ``Desktop`` object.
    project_dir : str
        Path to the project.
    project_name : str
        Name of the project
    design_names : list
        List of design names.

    Returns
    -------
    designs_dict : dict
        Dictionary includes data of all listed designs.

    """

    designs_dict = {}

    for design_name in design_names:
        design_dict = {
            design_name: {"mesh": {}, "simulation_time": {}, "report": {}, "profile_name": {}, "mesh_name": {}}
        }
        app = get_pyaedt_app(design_name=design_name)
        setups_names = app.setup_names
        if not setups_names:
            PROJECT_DICT["error_exception"].append("Design {} has no setups".format(design_name))
            designs_dict.update(design_dict)
            continue

        sweeps = app.existing_analysis_sweeps
        setup_dict = {}
        for setups in setups_names:
            for sweep in sweeps:
                if setups in sweep:
                    setup_dict[setups] = sweep
                    break

        analyze_success = desktop.analyze_all(design=design_name)

        if not analyze_success:
            logger.error("design {} 'analyze_all' failed".format(design_name))
            error_messages = app.logger.get_messages(project_name, design_name, level=1, aedt_messages=True)
            messages = error_messages.design_level + error_messages.project_level + error_messages.global_level
            for message in messages:
                log_message = "{}: {}".format(design_name, message)
                logger.error(log_message)
                PROJECT_DICT["error_exception"].append(log_message)
        else:
            logger.info("design {} 'analyze_all' success".format(design_name))

        design_dict = extract_design_data(
            app=app,
            design_name=design_name,
            setup_dict=setup_dict,
            project_dir=project_dir,
            design_dict=design_dict,
        )

        report_names = app.post.all_report_names
        reports_dict = extract_reports_data(
            app=app, design_name=design_name, project_dir=project_dir, report_names=report_names
        )

        design_dict[design_name]["report"] = reports_dict

        designs_dict.update(design_dict)

    return designs_dict


def extract_design_data(app, design_name, setup_dict, project_dir, design_dict):
    """Extract single design data.

    Parameters
    ----------
    app : pyaedt.application.AedtObjects
        ``pyaedt`` Electronics Desktop application object.
    design_name : str
        Name of the design
    setup_dict : dict
        Dictionary of the setups. key: setup name, value: sweeps.
    project_dir : str
        Path to the project folder
    design_dict : dict
        Dictionary {design_name: {"mesh": {}, "simulation_time": {}, "report": {}}}.

    Returns
    -------
    design_dict : dict
        Dictionary with values of mesh elements, simulation_time and report data.

    """

    for setup, sweep in setup_dict.items():
        if app.design_type == "HFSS 3D Layout Design":
            variation_strings = app.list_of_variations(setup, sweep.lstrip(setup + " : "))
        else:
            variation_strings = app.available_variations.get_variation_strings(sweep)
        if not variation_strings:
            continue
        for variation_string in variation_strings:
            variation_name = "nominal" if not variation_string else compose_variation_string(variation_string)

            if variation_name not in design_dict[design_name]["mesh"]:
                design_dict[design_name]["mesh"][variation_name] = {}
            if variation_name not in design_dict[design_name]["simulation_time"]:
                design_dict[design_name]["simulation_time"][variation_name] = {}
            if variation_name not in design_dict[design_name]["profile_name"]:
                design_dict[design_name]["profile_name"][variation_name] = {}
            if variation_name not in design_dict[design_name]["mesh_name"]:
                design_dict[design_name]["mesh_name"][variation_name] = {}

            profile_file = generate_unique_file_path(project_dir, ".prof")
            profile_file = app.export_profile(setup, variation_string, profile_file)
            simulation_time, cell_number = parse_profile_file(profile_file, design_name, variation_name, setup)
            design_dict[design_name]["simulation_time"][variation_name][setup] = simulation_time

            if app.design_type == "Icepak":
                design_dict[design_name]["mesh"][variation_name][setup] = cell_number
                mesh_stats_file = profile_file
            else:
                mesh_stats_file = generate_unique_file_path(project_dir, ".mstat")
                app.export_mesh_stats(setup, variation_string, mesh_stats_file)
                mesh_data = parse_mesh_stats(mesh_stats_file, design_name, variation_name, setup)
                design_dict[design_name]["mesh"][variation_name][setup] = mesh_data

            design_dict[design_name]["profile_name"][variation_name][setup] = profile_file
            design_dict[design_name]["mesh_name"][variation_name][setup] = mesh_stats_file

    return design_dict


def compose_variation_string(variation_string):
    """Format the variation string.

    Parameters
    ----------
    variation_string : str
        Variation string from electronics desktop.

    Returns
    -------
    variation_name : str
        Formatted variation string

    """
    strings = variation_string.split(" ")
    variation_name = ""
    for string in strings:
        if "=" in string:  # smith chart curve key is real and imag
            var, val = string.split("=")
            val = val.replace("'", "")
            val = val.replace('"', "")
            val, unit = parse_value_with_unit(val)
            variation_name += "{}={}{} ".format(var, val, unit)
        else:
            variation_name = string
    variation_name = variation_name.strip()
    return variation_name


def extract_reports_data(app, design_name, project_dir, report_names):
    """Get the report data form .rdat file.

    Parameters
    ----------
    app : pyaedt.application.AedtObjects
        Any ``pyaedt`` Electronics Desktop application object.
    design_name : str
        Name of the design.
    project_dir : str
        Path to the project.
    report_names : list
        List of report names.

    Returns
    -------
    report_dict : dictionary
        Dictionary includes all data from report.
    """
    report_dict = {}

    if not report_names:
        PROJECT_DICT["error_exception"].append("{} has no report".format(design_name))
    else:
        for report in report_names:
            report_file = app.post.export_report_to_file(
                output_dir=project_dir, plot_name=report, extension=".rdat", unique_file=True
            )
            data_dict = parse_rdat_file(report_file)
            data_dict = compose_curve_keys(data_dict)
            data_dict = check_nan(data_dict)
            report_dict.update(data_dict)

    return report_dict


def compose_curve_keys(data_dict):
    """Format the curve keys' number to 0.9e.

    Parameters
    ----------
    data_dict : dict
        Report data dictionary.

    Returns
    -------
    data_dict : dict
        Report data dictionary with formatted keys.

    """
    for plot_name in data_dict.keys():
        for trace_name in data_dict[plot_name].keys():
            curves_dict = data_dict[plot_name][trace_name]["curves"]
            for curve_name in list(curves_dict.keys()):
                if not curve_name:
                    curve_name_composed = "nominal"
                else:
                    curve_name_composed = compose_variation_string(curve_name)

                curves_dict[curve_name_composed] = curves_dict.pop(curve_name)
    return data_dict


def check_nan(data_dict):
    """Remove the curve if ``nan`` is in ``x`` or ``y`` data.

    Parameters
    ----------
    data_dict : dict
        Report data dictionary.

    Returns
    -------
    data_dict : dict
        Checked report data dictionary.

    """

    for plot_name in data_dict.keys():
        for trace_name in data_dict[plot_name].keys():
            curves_dict = data_dict[plot_name][trace_name]["curves"]
            for curve_name in list(curves_dict.keys()):

                if sys.version_info.major == 3:
                    number_types = (float, int)
                else:
                    # need to handle "long" data type in python 2
                    number_types = (float, int, long)  # noqa: F821

                if any(not isinstance(x, number_types) for x in curves_dict[curve_name]["x_data"]) or any(
                    not isinstance(x, number_types) for x in curves_dict[curve_name]["y_data"]
                ):
                    curves_dict.pop(curve_name)

    return data_dict


def generate_unique_file_path(project_dir, extension):
    """Generate a unique file path.

    Parameters
    ----------
    project_dir : str
        Path to the project dir.
    extension : str
        Specified file extension.

    Returns
    -------
    file_path : str
        Unique path for the file.

    """
    file_name = generate_unique_name("")
    file_path = os.path.join(project_dir, file_name + extension)

    while os.path.exists(file_path):
        file_name = generate_unique_name(file_name)
        file_path = os.path.join(project_dir, file_name + extension)

    return file_path


def main():
    desktop = Desktop(specified_version=specified_version, non_graphical=False, new_desktop_session=False)

    project_name = desktop.project_list().pop()
    project_dir = desktop.project_path(project_name=project_name)
    project_path = os.path.join(project_dir, project_name + ".aedt")
    design_names = desktop.design_list()

    if design_names:
        logger.info("Start extraction for {}".format(project_path))
        designs_dict = extract_data(desktop, project_dir, project_name, design_names)
        PROJECT_DICT["designs"].update(designs_dict)
    else:
        PROJECT_DICT["error_exception"].append("Project has no design")

    logger.info("Finished extraction for {}".format(project_path))

    results_json = os.path.join(project_dir, project_name + ".json")
    with open(results_json, "w") as outfile:
        json.dump(PROJECT_DICT, outfile, indent=4)

    logger.debug("JSON dumped to {}".format(results_json))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        logger.exception(str(exc))
        raise
