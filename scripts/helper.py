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


def ls_tables():
    """List all remuneration tables in the directory specified by the `ps_tables_path` constant."""
    return os.listdir(ps_tables_path)


def ls_prv():
    """List all the private retirement tables in the directory specified by the `prv_tables_path` constant."""
    return os.listdir(ps_tables_path)


@lru_cache(maxsize=128)
def csv2dic(full_name):
    """
    Read a CSV file specified by `full_name` argument and return a dictionary containing the data.

    Parameters:
    full_name (str): The full path to the CSV file.

    Returns:
    dict: A dictionary containing the data from the CSV file.
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

    Parameters:
    table_name (str): The name of the directory containing the CSV file.
    csv_file (str): The name of the CSV file to read.

    Returns:
    dict: A dictionary containing the data from the CSV file.
    """
    return csv2dic(os.path.join(ps_tables_path, table_name, csv_file))


def read_all_table(TV):
    """
    Read all CSV files in the directory specified by the `TV` argument and return a dictionary containing the data.

    Parameters:
    TV (str): The name of the directory containing the CSV files.

    Returns:
    dict: A dictionary containing the data from all CSV files in the specified directory.
    """
    table_data = {}
    path = os.path.join(ps_tables_path, TV)
    if os.path.exists(path):
        for table in os.listdir(path):
            if table.endswith(".csv"):
                table_data[table] = csv2dic(os.path.join(path, table))
    return table_data


def read_meta_table(TV):
    """
    Read the `Meta.csv` file in the directory specified by the `TV` argument and return a dictionary containing the data.

    Parameters:
    TV (str): The name of the directory containing the `Meta.csv` file.

    Returns:
    dict: A dictionary containing the data from the `Meta.csv` file.
    """
    return csv2dic(os.path.join(ps_tables_path, TV, "Meta.csv"))


def read_table(TV=""):
    """
    Read all CSV files in the directory specified by the `TV` argument (if provided) or all CSV files in the `ps_tables_path` directory (if `TV` is not provided) and return a dictionary containing the data.

    Parameters:
    TV (str, optional): The name of the directory containing the CSV files. Defaults to "".

    Returns:
    dict: A dictionary containing the data from all CSV files in the specified directory (or `ps_tables_path` if `TV` is not provided).
    """
    if TV:
        return csv2dic(os.path.join(ps_tables_path, TV, "Table.csv"))
    else:
        # If no table name is specified, read all tables and return their data in a dictionary
        table_data = {}
        for table in os.listdir(ps_tables_path):
            table_data[table] = csv2dic(os.path.join(
                ps_tables_path, table, "Table.csv"))
        return table_data


def read_allowance_data(allowances=None):
    """
    Read data from the "allowances" directory and return a dictionary of table data.

    Args:
    allowances (list): A list of allowance names to include in the output. If None, all allowances will be included.

    Returns:
    dict: A dictionary containing the data from the "allowances" directory.
    """
    # Initialize an empty dictionary to store the table data
    table_data = {}

    # Loop through each directory in the "allowances" directory
    for allowance_name in os.listdir(ps_allowances_path):
        # If the "allowances" argument is not specified or the current allowance is in the "allowances" argument list
        if allowances is None or allowance_name in allowances:
            # Read the "Meta.csv" and "Table.csv" files for the current allowance and add them to the dictionary
            table_data[allowance_name] = {
                "Meta.csv": csv2dic(os.path.join(ps_allowances_path, allowance_name, "Meta.csv")),
                "Table.csv": csv2dic(os.path.join(ps_allowances_path, allowance_name, "Table.csv"))
            }

    # Return the dictionary containing the table data
    return table_data


def read_prv_data(prv=None):
    """
    Read data from the "prv" directory and return a dictionary of table data.

    Args:
        prv (list): A list of PRV names to include in the output. If None, all PRVs will be included.

    Returns:
        dict: A dictionary containing the data from the "prv" directory.
    """
    # Initialize an empty dictionary to store the table data
    table_data = {}

    # Loop through each directory in the "prv" directory
    for prv_name in os.listdir(prv_tables_path):
        # If the "prv" argument is not specified or the current PRV is in the "prv" argument list
        if prv is None or prv_name in prv:
            # Read the "Meta.csv" file for the current PRV and add it to the dictionary
            table_data[prv_name] = {"Meta.csv": csv2dic(
                os.path.join(prv_tables_path, prv_name, "Meta.csv"))}

    # Return the dictionary containing the table data
    return table_data


def get_prv_sal_data(gross_sal, prv_type):
    prv_table = read_prv_data(prv_type)
    # try:
    prv_fun = import_prv_function(prv_table[prv_type]["Meta.csv"]["calc_fun"]["value"])
    # except:
    #   return gross_sal, gross_sal, 0, 0
    
    
    return prv_fun(gross_sal, prv_table[prv_type]["Meta.csv"])
