# import functions and packages
from horizons_api import fetch_horizons_data
import sys
from pprint import pprint
from astropy import units as u


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

    # Parse ephemeris data for each dictionary in NAIF-ID
    for item in planet_data:
        raw = item["data"]["result"]
        lines = raw.splitlines()

        gm_line = next(
            (line for line in lines if "GM, km^3/s^2" in line or "GM (km^3/s^2)" in line),
            None,
        )
        gm_value = None
        if gm_line:
            parts = gm_line.split("=")
            if len(parts) > 1:
                gm_value = parts[1].split()[0].strip()

        gm_val_units = None
        if gm_value is not None:
            gm_val_units = float(gm_value) * (u.km**3/u.s**2)

        start = lines.index("$$SOE") + 1
        end = lines.index("$$EOE")
        table_lines = [line for line in lines[start:end] if line.strip()]
        rows = [line.split(",") for line in table_lines]

        # GM output saved under gm_val_units
        # Ephemeris data saved as a list udner "rows"
        item["gm"] = gm_val_units
        print("NAIF-ID:", item["naifid"])
        print("GM:", item["gm"] if gm_line is not None else "not found")
        print("--- EPHEMERIS LINES ---")
        for num in rows:
            print(num)

    # ALT: printing all output, comment out above for loop
    # print(lines)

if __name__ == "__main__":
    raise SystemExit(main())