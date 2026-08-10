#!/usr/bin/env python3
import requests
import sys
import json
from urllib.parse import urlencode

# Base URL for NASA JPL Horizons API
BASE_URL = "https://ssd.jpl.nasa.gov/api/horizons.api"

# Get requested NAIF-ID from commandline:
if (len(sys.argv)) == 1:
    print("Please input planet NAIF-ID on command line.")
    sys.exit(2)
naifid = sys.argv[1:]

# commands = ["199", "299", "499", "599", "699", "799", "899", "999"]
# commands = ["199"]

def main() -> int:
    for cmd in naifid:
        fetch_horizons_data(cmd)
    return 0

def fetch_horizons_data(cmd):
    print(f"\n=== COMMAND {cmd} ===")

    params = {
        "format": "json",
        "COMMAND": cmd,              # Target body (e.g., 399 = Earth)
        "EPHEM_TYPE": "OBSERVER",      # Type of ephemeris data
        "CENTER": "675@399",             # Observer location (site = predifined observatory site, @399 = on Earth)
        "START_TIME": "2026-07-20",    # Start date
        "STOP_TIME": "2026-07-21",     # End date
        "STEP_SIZE": "1d",             # Step size (daily)
        # "CSV_FORMAT": "YES"
    }

    #URL encode
    query_string = urlencode(params)
    url = f"{BASE_URL}?{query_string}"

    # Submit API request and decode JSON
    response = requests.get(url)
    print("URL:", url)
    try:
        data = json.loads(response.text)
    except ValueError:
        print("unable to decode JSON results.")

    
    if response.status_code != 200:
        raise RuntimeError(f"Error: {response.status_code}\n{response.text}")
        sys.exit(1)

    print("Request successful. Summary:")
    print(data.get("result") or data)
    return data


# data = fetch_horizons_data(naifid)



if __name__ == "__main__":
    raise SystemExit(main())
