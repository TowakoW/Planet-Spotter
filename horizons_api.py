#!/usr/bin/env python3
import requests

# Base URL for NASA JPL Horizons API
BASE_URL = "https://ssd.jpl.nasa.gov/api/horizons.api"

# Example parameters:
# - 'format': 'json'      -> Output in JSON
# - 'COMMAND': '199'      -> Identifier for the body (199 = Earth)
# - 'EPHEM_TYPE': 'OBSERVER' -> Type of ephemeris (OBSERVER target output)
# - 'OBSERVER': '@399'    -> Observer (399 = Earth)
# - 'START_TIME', 'STOP_TIME', 'STEP_SIZE' -> Time range and steps
params = {
    "format": "text",
    "COMMAND": "499",              # Target body (e.g., 199 = Earth)
    "OBJ_DATA": "YES",              # Target body (e.g., 199 = Earth)
    "MAKE_EPHEM": "YES",
    "EPHEM_TYPE": "OBSERVER",      # Type of ephemeris data
    "CENTER": "500@399",             # Observer location (500 = Solar System Barycenter)
    "START_TIME": "2026-06-07",    # Start date
    "STOP_TIME": "2026-06-08",     # End date
    "STEP_SIZE": "'1 d'",             # Step size (dail)y
    "QUANTITIES": "1,9,20,23,24,29"             # Step size (daily)
}

# Make the GET request
print(f"1")
response = requests.get(BASE_URL, params=params)

# Consider the following URL's.  The one on top, the second needs some tics aroudn Quantities.  
# https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=499&OBJ_DATA=YES&MAKE_EPHEM=YES&EPHEM_TYPE=OBSERVER&CENTER=500@399&START_TIME=2006-01-01&STOP_TIME=2006-01-20&STEP_SIZE='1%20d'&QUANTITIES='1,9,20,23,24,29'
# https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=499&OBJ_DATA=YES&MAKE_EPHEM=YES&EPHEM_TYPE=OBSERVER&CENTER=500%40399&START_TIME=2026-06-07&STOP_TIME=2026-06-08&STEP_SIZE=1+d&QUANTITIES=1%2C9%2C20%2C23%2C24%2C2

print(f"2")

print("Final URL:", response.url)
print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("First 300 chars of Response:", response.text[:300])
# Check response status
if response.status_code == 200:
    data = response.json()
    print("Request successful. Summary:")
    print(data.get("result") or data)  # Print result section or entire response
else:
    print(f"Error: {response.status_code}")
    print(response.text)
