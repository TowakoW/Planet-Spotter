# import other file data
from horizons_api import fetch_horizons_data
import sys


# Base URL for NASA JPL Horizons API
BASE_URL = "https://ssd.jpl.nasa.gov/api/horizons.api"

# Get requested NAIF-ID from commandline:
if (len(sys.argv)) == 1:
    print("Please input planet NAIF-ID on command line.")
    sys.exit(2)
naifid = sys.argv[1:] or [199]

def main() -> int:
    results = {}
    for cmd in naifid:
        results[cmd] = fetch_horizons_data(cmd)
    return results
