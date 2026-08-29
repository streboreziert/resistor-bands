import argparse
import json

from resistor_bands.lib import combine, e24_near, inverse, ohms, ohms5


def main() -> None:
    p = argparse.ArgumentParser(description="Resistor bands + E24 combine")
    p.add_argument("bands", nargs="*")
    p.add_argument("--ohms", type=float)
    p.add_argument("--five", action="store_true")
    p.add_argument("--combine", type=float)
    a = p.parse_args()
    if a.combine is not None:
        print(json.dumps(combine(a.combine), indent=2))
    elif a.ohms is not None:
        print(json.dumps({"inverse": inverse(a.ohms), "e24": e24_near(a.ohms)}, indent=2))
    elif a.five and len(a.bands) >= 4:
        print(json.dumps({"ohms": ohms5(*a.bands[:4])}, indent=2))
    else:
        print(json.dumps({"ohms": ohms(*a.bands[:3])}, indent=2))
