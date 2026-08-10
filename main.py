# import other file data
from horizons_api import fetch_horizons_data
import sys
from pprint import pprint


def main() -> dict:
    # Get requested NAIF-ID from commandline:
    if (len(sys.argv)) == 1:
        print("Please input planet NAIF-ID on command line.")
        sys.exit(2)

    naifid = sys.argv[1:] or [199]

    planet_data = []
    for cmd in naifid:
        planet_data.append({"naifid": cmd, "data": fetch_horizons_data(cmd)})
    # take only "results" data in each dictionary
    for item in planet_data:
        raw = item["data"]["result"]
        lines = raw.splitlines()
        start = lines.index("$$SOE") +1
        end = lines.index("$$EOE")
        table_lines = [line for line in lines[start:end] if line.strip()]
        rows = [line.split(",") for line in table_lines]
        print("NAIF-ID:", item["naifid"])
        pprint(rows)

if __name__ == "__main__":
    raise SystemExit(main())