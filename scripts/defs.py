import os

# Define the path to the "tables" directory relative to the current file
ps_path = os. path.dirname(os.path.realpath(__file__))
ps_tables_path = os.path.join(ps_path, "..", "tables")

ps_allowances_path = os.path.join(ps_path, "..", "allowances")
