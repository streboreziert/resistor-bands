import argparse, json
from resistor_bands.lib import ohms, ohms5, inverse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("bands", nargs="*")
    p.add_argument("--ohms", type=float)
    p.add_argument("--five", action="store_true")
    a = p.parse_args()
    if a.ohms is not None:
        print(json.dumps(inverse(a.ohms), indent=2))
    elif a.five and len(a.bands) >= 4:
        print(json.dumps({"ohms": ohms5(*a.bands[:4])}, indent=2))
    else:
        print(json.dumps({"ohms": ohms(*a.bands[:3])}, indent=2))
