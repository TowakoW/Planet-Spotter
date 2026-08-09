#!/usr/bin/env python3
import requests

# Base URL for NASA JPL Horizons API
BASE_URL = "https://ssd.jpl.nasa.gov/api/horizons.api"

# commands = ["199", "299", "499", "599", "699", "799", "899", "999"]
commands = ["199"]


def fetch_horizons_data(cmd: str = "199"):
    print(f"\n=== COMMAND {cmd} ===")

    params = {
        "format": "json",
        "COMMAND": cmd,              # Target body (e.g., 399 = Earth)
        "EPHEM_TYPE": "OBSERVER",      # Type of ephemeris data
        "CENTER": "675@399",             # Observer location (site = predifined observatory site, @399 = on Earth)
        "START_TIME": "2026-07-20",    # Start date
        "STOP_TIME": "2026-07-21",     # End date
        "STEP_SIZE": "1d",             # Step size (daily)
        "CSV_FORMAT": "YES"
    }

    response = requests.get(BASE_URL, params=params, timeout=30)
    print("Request URL:", response.request.url)

    if response.status_code != 200:
        raise RuntimeError(f"Error: {response.status_code}\n{response.text}")

    data = response.json()
    print("Request successful. Summary:")
    print(data.get("result") or data)
    return data


data = fetch_horizons_data(commands[0])


def main() -> int:
    for cmd in commands:
        fetch_horizons_data(cmd)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
