#!/usr/bin/env python3
import requests

# Base URL for NASA JPL Horizons API
BASE_URL = "https://ssd.jpl.nasa.gov/api/horizons.api"

commands = ["199", "299", "499", "599", "699", "799", "899", "999"]

for cmd in commands:
# Example parameters:
# - 'format': 'json'      -> Output in JSON
# - 'COMMAND': '499'      -> Identifier for the body (499 = Mars)
# - 'EPHEM_TYPE': 'OBSERVER' -> Type of ephemeris (OBSERVER target output)
# - 'CENTER': '399'    -> Observer (399 = Earth)
# - 'START_TIME', 'STOP_TIME', 'STEP_SIZE' -> Time range and steps
    params = {
        "format": "json",
        "COMMAND": cmd,              # Target body (e.g., 399 = Earth)
        "EPHEM_TYPE": "OBSERVER",      # Type of ephemeris data
        "CENTER": "675@399",             # Observer location (site = predifined observatory site, @399 = on Earth)
        "START_TIME": "2026-06-07",    # Start date
        "STOP_TIME": "2026-06-08",     # End date
        "STEP_SIZE": "1d"             # Step size (daily)
    }

# Make the GET request

response = requests.get(BASE_URL, params=params)
print("Request URL:", response.request.url)

# Check response status
if response.status_code == 200:
    data = response.json()
    print("Request successful. Summary:")
    print(data.get("result") or data)  # Print result section or entire response
else:
    print(f"Error: {response.status_code}")
    print(response.text)
