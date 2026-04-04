import os
import csv
from glob import glob

def run_diagnostics():
    ps_path = os.path.dirname(os.path.realpath(__file__))
    ps_tables_path = os.path.join(ps_path, "tables")
    ps_allowances_path = os.path.join(ps_path, "allowances")
    
    print("--- TVData Doctor ---")

    def check_metadata(path, req_fields, label):
        for root, _, files in os.walk(path):
            if "Table.csv" in files:
                if "Meta.csv" not in files:
                    print(f"⚠️  [{label}] Missing Meta.csv in directory: {root}")
                    continue
                
                meta_path = os.path.join(root, "Meta.csv")
                try:
                    with open(meta_path, "r", encoding="utf-8") as infile:
                        reader = csv.reader(infile)
                        headers = next(reader)
                        keys = [row[0] for row in reader if row]
                        
                        missing = [f for f in req_fields if f not in keys]
                        if missing:
                            print(f"❌ [{label}] Missing required fields {missing} in: {meta_path}")
                except Exception as e:
                    print(f"❌ [{label}] Error reading {meta_path}: {e}")

    # Check Tables
    print("\nScanning Tables...")
    table_req = ["pay_grad_name", "valid_from"]
    check_metadata(ps_tables_path, table_req, "TABLE")

    # Check Allowances
    print("\nScanning Allowances...")
    allow_req = ["func_type", "adding_type", "default_option"]
    check_metadata(ps_allowances_path, allow_req, "ALLOWANCE")
    
    print("\n✔ Diagnostics complete.")

if __name__ == "__main__":
    run_diagnostics()
