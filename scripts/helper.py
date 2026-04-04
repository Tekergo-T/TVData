"""
 Copyright (c) 2023 Beáta Ungurán All rights reserved.
 Use of this source code is governed by a BSD-style
 license that can be found in the LICENSE file.
 """

import os
from .defs import *
import csv

import importlib
from functools import lru_cache


def import_prv_function(prv_module):
    """
    Import the 'prv' function from the specified module.

    Args:
        prv_module (str): The name of the module to import the 'prv' function from.

    Returns:
        function: The imported 'prv' function.
    """
    try:
        # Import the module dynamically
        module = importlib.import_module(".prv."+prv_module, package="templates.public_sector.shared.TVData.scripts")
        # Get the 'prv' function from the imported module
        return module.prv
    except ImportError:
        raise ImportError(
            f"Failed to import 'prv' function from module: {prv_module}")
import logging

logger = logging.getLogger(__name__)

_table_paths_cache = None
def _get_table_paths():
    global _table_paths_cache
    if _table_paths_cache is None:
        _table_paths_cache = {}
        # os.walk travels top-down, so we hit parent folders before subfolders.
        for root, _, files in os.walk(ps_tables_path):
            if 'Table.csv' in files and 'Meta.csv' in files:
                table_name = os.path.basename(root)
                # First valid folder wins, preventing nested subfolders from overwriting
                if table_name not in _table_paths_cache:
                    _table_paths_cache[table_name] = root
                else:
                    logger.warning(f"TVData Tables: Ignored duplicate path {root} for '{table_name}'. Keeping { _table_paths_cache[table_name] }")
    return _table_paths_cache


_allowance_paths_cache = None
def _get_allowance_paths():
    global _allowance_paths_cache
    if _allowance_paths_cache is None:
        _allowance_paths_cache = {}
        for root, _, files in os.walk(ps_allowances_path):
            if 'Table.csv' in files and 'Meta.csv' in files:
                allowance_name = os.path.basename(root)
                if allowance_name not in _allowance_paths_cache:
                    _allowance_paths_cache[allowance_name] = root
                else:
                    logger.warning(f"TVData Allowances: Ignored duplicate path {root} for '{allowance_name}'. Keeping { _allowance_paths_cache[allowance_name] }")
    return _allowance_paths_cache


_prv_paths_cache = None
def _get_prv_paths():
    global _prv_paths_cache
    if _prv_paths_cache is None:
        _prv_paths_cache = {}
        for root, _, files in os.walk(prv_tables_path):
            if 'Meta.csv' in files:
                prv_name = os.path.basename(root)
                if prv_name not in _prv_paths_cache:
                    _prv_paths_cache[prv_name] = root
                else:
                    logger.warning(f"TVData PRV: Ignored duplicate path {root} for '{prv_name}'. Keeping { _prv_paths_cache[prv_name] }")
    return _prv_paths_cache

def ls_tables():
    """List all remuneration tables in the directory specified by the `ps_tables_path` constant."""
    return list(_get_table_paths().keys())


def ls_prv():
    """List all the private retirement tables in the directory specified by the `prv_tables_path` constant."""
    return list(_get_prv_paths().keys())


@lru_cache(maxsize=128)
def csv2dic(full_name):
    """
    Read a CSV file specified by `full_name` argument and return a dictionary containing the data.
    """
    table_data = {}
    with open(full_name, "r") as infile:
        reader = csv.reader(infile)
        headers = next(reader)  # Read the headers from the first row
        for row in reader:
            # Create a new dictionary entry for the current row, using the first column as the key
            table_data[row[0]] = {key: value for key,
                                  value in zip(headers[1:], row[1:])}
    return table_data


def read_csv(table_name, csv_file):
    """
    Read a CSV file specified by `csv_file` argument from the directory specified by `table_name` argument and return a dictionary containing the data.
    """
    paths = _get_table_paths()
    if table_name in paths:
        return csv2dic(os.path.join(paths[table_name], csv_file))
    return {}


def read_all_table(TV):
    """
    Read all CSV files in the directory specified by the `TV` argument and return a dictionary containing the data.
    """
    table_data = {}
    paths = _get_table_paths()
    if TV in paths:
        path = paths[TV]
        for file in os.listdir(path):
            if file.endswith(".csv"):
                table_data[file] = csv2dic(os.path.join(path, file))
    return table_data


def read_meta_table(TV):
    """
    Read the `Meta.csv` file in the directory specified by the `TV` argument and return a dictionary containing the data.
    """
    paths = _get_table_paths()
    if TV in paths:
        return csv2dic(os.path.join(paths[TV], "Meta.csv"))
    return {}


def read_table(TV=""):
    """
    Read all CSV files in the directory specified by the `TV` argument (if provided) or all CSV files in the `ps_tables_path` directory (if `TV` is not provided) and return a dictionary containing the data.
    """
    paths = _get_table_paths()
    if TV:
        if TV in paths:
            return csv2dic(os.path.join(paths[TV], "Table.csv"))
        return {}
    else:
        table_data = {}
        for table, path in paths.items():
            table_data[table] = csv2dic(os.path.join(path, "Table.csv"))
        return table_data


def read_allowance_data(allowances=None):
    """
    Read data from the "allowances" directory and return a dictionary of table data.
    """
    table_data = {}
    paths = _get_allowance_paths()
    for allowance_name, path in paths.items():
        if allowances is None or allowance_name in allowances:
            table_data[allowance_name] = {
                "Meta.csv": csv2dic(os.path.join(path, "Meta.csv")),
                "Table.csv": csv2dic(os.path.join(path, "Table.csv"))
            }

    return table_data


def read_prv_data(prv=None):
    """
    Read data from the "prv" directory and return a dictionary of table data.
    """
    table_data = {}
    paths = _get_prv_paths()
    for prv_name, path in paths.items():
        if prv is None or prv_name in prv:
            table_data[prv_name] = {"Meta.csv": csv2dic(os.path.join(path, "Meta.csv"))}
    return table_data


def get_prv_sal_data(gross_sal, prv_type):
    prv_table = read_prv_data(prv_type)
    # try:
    prv_fun = import_prv_function(prv_table[prv_type]["Meta.csv"]["calc_fun"]["value"])
    # except:
    #   return gross_sal, gross_sal, 0, 0
    
    
    return prv_fun(gross_sal, prv_table[prv_type]["Meta.csv"])
