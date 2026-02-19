import sys
import os

# Add relevant paths to sys.path
scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

from prv.vbl_east import prv as prv_east

def validate_vbl_east_logic():
    print("=== VBL East 2026 Logic Validation ===")
    print("Reference Rule: If Umlage < 2.5%, Zurechnungsbetrag 2 = (Umlage_Percent * Brutto) - Freibetrag")
    print("Source: Social Security Calculation Rules for VBL / Zusatzversorgung")
    print("---------------------------------------------------")

    # Scenario 1: VBL East 2026 Official Values
    # Umlage: 1.06%
    # Freibetrag: 13.30 EUR
    brutto = 3000.0
    data_2026 = {
        "arbeitnehmeranteil": {"value": 4.25},
        "arbeitgeberanteil": {"value": 2.0},
        "umlage": {"value": 1.06}, # Official 2026
        "pauschal": {"value": 89.48},
        "steuer_frei": {"value": 338},
        "grenzbetrag": {"value": 100},
        "sozi_freibetrags": {"value": 13.30}
    }
    
    _, _, _, _ = prv_east(brutto, data_2026)
    
    # Expected: 1.06% of 3000 = 31.80.
    # 31.80 - 13.30 = 18.50
    
    # To verify what the script actually calculated for ZB2, we can re-calculate the expected Social Gross
    # and compare it with the script output.
    # Script outputs: sozialver_brutto
    # sozialver_brutto = taxable_gross + ZB1 + ZB2
    
    # Calculate Taxable Gross (strpflich_brutto)
    # AG Umlage (Euro) = 1.06% * 3000 = 31.80
    # Tax-free (338) covers 31.80 fully.
    # Pauschal taxed = 0.
    # Taxable part of Umlage = 0.
    # AN contribution = 4.25% * 3000 = 127.50
    # strpflich_brutto = 3000 - 127.50 = 2872.50
    
    # Calculate ZB1
    # max(0, min(338, 31.80) + min(89.48, 0) - 100) = max(0, 31.80 - 100) = 0.
    
    # Expected Social Gross = 2872.50 + 0 + ZB2
    # If ZB2 = 18.50, then Social Gross = 2891.00
    
    script_result = prv_east(brutto, data_2026)[0]
    expected_result = 2891.00
    
    print(f"Scenario 2026 (1.06% Umlage):")
    print(f"  Brutto: {brutto}")
    print(f"  Expected ZB2: 18.50 (1.06% * 3000 - 13.30)")
    print(f"  Expected SocGross: {expected_result:.2f}")
    print(f"  Script SocGross:   {script_result:.2f}")
    
    if abs(script_result - expected_result) < 0.01:
        print("  [PASS] Script correctly uses 1.06% Umlage.")
    else:
        print(f"  [FAIL] Script output mismatch. Diff: {script_result - expected_result}")

    print("---------------------------------------------------")
    
    # Scenario 2: Hypothetical 1.00% Umlage (just to prove dynamic behavior)
    data_hypo = data_2026.copy()
    data_hypo["umlage"] = {"value": 1.00}
    
    # Expected ZB2: 1.00% * 3000 = 30.00 - 13.30 = 16.70
    # AG Umlage Euro: 30.00
    # Taxable Gross: 2872.50 (Same, as 30.00 is still tax free)
    # ZB1: Still 0.
    # Expected SocGross: 2872.50 + 16.70 = 2889.20
    
    script_result_hypo = prv_east(brutto, data_hypo)[0]
    expected_result_hypo = 2889.20
    
    print(f"Scenario Hypothetical (1.00% Umlage):")
    print(f"  Expected ZB2: 16.70")
    print(f"  Expected SocGross: {expected_result_hypo:.2f}")
    print(f"  Script SocGross:   {script_result_hypo:.2f}")
    
    if abs(script_result_hypo - expected_result_hypo) < 0.01:
         print("  [PASS] Script correctly adjusted to 1.00% Umlage.")
    else:
         print(f"  [FAIL] Script output mismatch.")

if __name__ == "__main__":
    validate_vbl_east_logic()
