import os
from .defs import *
import csv


def ls_tables():
    """List all tables in the directory specified by the `ps_tables_path` constant."""
    return os.listdir(ps_tables_path)


def csv2dic(full_name):
    """
    Read a CSV file specified by `full_name` argument and return a dictionary containing the data.

    Parameters:
    full_name (str): The full path to the CSV file.

    Returns:
    dict: A dictionary containing the data from the CSV file.
    """
    dict1 = {}
    with open(full_name, "r") as infile:
        reader = csv.reader(infile)
        headers = next(reader)  # Read the headers from the first row
        for row in reader:
            # Create a new dictionary entry for the current row, using the first column as the key
            dict1[row[0]] = {key: value for key,
                             value in zip(headers[1:], row[1:])}
    return dict1


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
    dict1 = {}
    for table in os.listdir(os.path.join(ps_tables_path, TV)):
        dict1[table] = csv2dic(os.path.join(ps_tables_path, TV, table))

    return dict1


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
        # If a table name is specified, read only that table and return its data
        return csv2dic(os.path.join(ps_tables_path, TV, "Table.csv"))
    else:
        # If no table name is specified, read all tables and return their data in a dictionary
        dict1 = {}
        for table in os.listdir(ps_tables_path):
            dict1[table] = csv2dic(os.path.join(
                ps_tables_path, table, "Table.csv"))
        return dict1


def read_allowance_data(allowances=None):
    """
    Read data from the "allowances" directory and return a dictionary of table data.

    Args:
    allowances (list): A list of allowance names to include in the output. If None, all allowances will be included.

    Returns:
    dict: A dictionary containing the data from the "allowances" directory.
    """
    # Initialize an empty dictionary to store the table data
    dict1 = {}

    # Loop through each directory in the "allowances" directory
    for allowance_name in os.listdir(ps_allowances_path):
        # If the "allowances" argument is not specified or the current allowance is in the "allowances" argument list
        if allowances is None or allowance_name in allowances:
            # Read the "Meta.csv" and "Table.csv" files for the current allowance and add them to the dictionary
            dict1[allowance_name] = {
                "Meta.csv": csv2dic(os.path.join(ps_allowances_path, allowance_name, "Meta.csv")),
                "Table.csv": csv2dic(os.path.join(ps_allowances_path, allowance_name, "Table.csv"))
            }

    # Return the dictionary containing the table data
    return dict1
