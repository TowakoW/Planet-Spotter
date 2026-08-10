# import functions and packages
from horizons_api import fetch_horizons_data
import sys
from pprint import pprint


def main() -> dict:
    # Get requested NAIF-ID(s) from commandline:
    if (len(sys.argv)) == 1:
        print("Please input planet NAIF-ID on command line.")
        sys.exit(2)

    naifid = sys.argv[1:] or [199]

    # Pulls ephimeris data from NASA JPL's Horizons API
    planet_data = []
    for cmd in naifid:
        planet_data.append({"naifid": cmd, "data": fetch_horizons_data(cmd)})

    # Parse ephimeris data for each dictionary in NAIF-ID
    for item in planet_data:
        raw = item["data"]["result"]
        lines = raw.splitlines()
        start = lines.index("$$SOE") +1
        end = lines.index("$$EOE")
        table_lines = [line for line in lines[start:end] if line.strip()]
        rows = [line.split(",") for line in table_lines]

    # Show ephimeris for each item in NAIF-ID
        print("NAIF-ID:", item["naifid"])
        pprint(rows)

if __name__ == "__main__":
    raise SystemExit(main())