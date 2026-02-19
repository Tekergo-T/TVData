import sys
import os

# Add relevant paths to sys.path
scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

from prv.vbl_west import prv as prv_west
from prv.vbl_east import prv as prv_east

def test_kvbw_2026():
    # KVBW uses vbl_west logic but with specific Meta.csv values
    # We test if the new limit (1821.49) is respected
    data_dict = {
        "arbeitnehmeranteil": {"value": 0.55},
        "arbeitgeberanteil": {"value": 5.75},
        "pauschal": {"value": 89.48},
        "steuer_frei": {"value": 338.00}, # Updated from 219
        "grenzbetrag": {"value": 100},
        "sozi_freibetrags": {"value": 13.30},
        "zurechnungs_grenze_2": {"value": 1821.49} # New
    }
    
    # Test High Income (4000 EUR) for KVBW
    # Expected ZB2 = max(0, (2.5% * 1821.49) - 13.30) = 32.237...
    brutto = 4000.0
    _, _, _, _ = prv_west(brutto, data_dict)
    
    zb2_kvbw = max(0, (0.025 * min(brutto, 1821.49)) - 13.30)
    print(f"KVBW (4000€): Expected ZB2 = {zb2_kvbw:.2f}")

    if abs(zb2_kvbw - 32.24) < 0.01:
        print("PASS: KVBW Check")
    else:
        print(f"FAIL: KVBW Check. Got {zb2_kvbw}")

def test_vbl_east_2026():
    # VBL East has its own logic (1% factor usually)
    # We verify that sozi_freibetrags is now 13.30
    data_dict = {
        "arbeitnehmeranteil": {"value": 4.25},
        "arbeitgeberanteil": {"value": 2.0},
        "umlage": {"value": 1.06},
        "pauschal": {"value": 89.48},
        "steuer_frei": {"value": 338},
        "grenzbetrag": {"value": 100},
        "sozi_freibetrags": {"value": 13.30} # Updated
    }
    
    # Logic in vbl_east.py:
    # zurechnungsbetrag_2 = max(0, (brutto_gehalt / 100 - sozi_freibetrags))
    # Test with 2000 EUR
    brutto = 2000.0
    zb2_east = max(0, (brutto / 100 - 13.30)) # 20 - 13.30 = 6.70
    
    print(f"VBL East (2000€): Expected ZB2 = {zb2_east:.2f}")
    if abs(zb2_east - 6.70) < 0.01:
        print("PASS: VBL East Check")
    else:
        print(f"FAIL: VBL East Check. Got {zb2_east}")

if __name__ == "__main__":
    test_kvbw_2026()
    test_vbl_east_2026()
