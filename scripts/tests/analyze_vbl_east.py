import sys
import os

# Add relevant paths to sys.path
scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

from prv.vbl_east import prv as prv_east

def analyze_vbl_east():
    # Scenario: 3000 EUR Gross
    brutto = 3000.0
    
    # Current Data (Meta.csv values)
    data_dict = {
        "arbeitnehmeranteil": {"value": 4.25},
        "arbeitgeberanteil": {"value": 2.0},
        "umlage": {"value": 1.06},
        "pauschal": {"value": 89.48},
        "steuer_frei": {"value": 338},
        "grenzbetrag": {"value": 100},
        "sozi_freibetrags": {"value": 13.30}
    }
    
    # Run current script
    sozialver_brutto, strpflich_brutto, an_beitrag, ag_beitrag = prv_east(brutto, data_dict)
    
    print(f"--- Analysis for Brutto {brutto} ---")
    
    # Manual Calculation of Zurechnungsbetrag 2
    # Logic: max(0, (Umlagesatz * Brutto) - Freibetrag)
    # Current Script Logic: max(0, (Brutto / 100) - Freibetrag)  -> This is 1.00%
    
    zb2_current_script = max(0, (brutto / 100) - 13.30)
    print(f"Current Script ZB2 (1.00%): {zb2_current_script:.2f}")
    
    # Hypothesis: Should be Umlagesatz (1.06%)
    zb2_hypothesis = max(0, (0.0106 * brutto) - 13.30)
    print(f"Hypothesis ZB2 (1.06%):    {zb2_hypothesis:.2f}")
    
    diff = zb2_hypothesis - zb2_current_script
    print(f"Difference: {diff:.2f}")
    
    # Check what 'prv_east' actually returned by reverse engineering
    # sozialver_brutto = strpflich_brutto + (zb1 + zb2)
    # strpflich_brutto calculation in script:
    # umlage_eur = 0.0106 * 3000 = 31.80
    # pauschal_rest = 31.80 - 338 = 0
    # steuer_erhoehen = 0 - 89.48 = -89.48 -> 0
    # an_beitrag = 0.0425 * 3000 = 127.50
    # strpflich_brutto = 3000 + 0 - 127.50 = 2872.50
    
    # zb1 = max(0, min(338, 31.80) + min(89.48, 0) - 100) + 0 
    # zb1 = max(0, 31.80 + 0 - 100) = 0
    
    # So sozialver_brutto = 2872.50 + 0 + zb2_current_script
    # 2872.50 + 16.70 = 2889.20
    
    print(f"Script Result 'Sozialver Brutto': {sozialver_brutto:.2f}")
    
    calculated_soc_gross_current = 2872.50 + zb2_current_script
    calculated_soc_gross_hypothesis = 2872.50 + zb2_hypothesis
    
    print(f"Recalculated (1.00%): {calculated_soc_gross_current:.2f}")
    print(f"Recalculated (1.06%): {calculated_soc_gross_hypothesis:.2f}")

if __name__ == "__main__":
    analyze_vbl_east()
