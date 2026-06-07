import requests

# Base URL for NASA JPL Horizons API
BASE_URL = "https://ssd-api.jpl.nasa.gov/horizons.api"

# Example parameters:
# - 'format': 'json'      -> Output in JSON
# - 'COMMAND': '199'      -> Identifier for the body (199 = Earth)
# - 'EPHEM_TYPE': 'OBSERVER' -> Type of ephemeris (OBSERVER target output)
# - 'OBSERVER': '@399'    -> Observer (399 = Earth)
# - 'START_TIME', 'STOP_TIME', 'STEP_SIZE' -> Time range and steps
params = {
    "format": "json",
    "COMMAND": "199",              # Target body (e.g., 199 = Earth)
    "EPHEM_TYPE": "OBSERVER",      # Type of ephemeris data
    "OBSERVER": "500",             # Observer location (500 = Solar System Barycenter)
    "START_TIME": "2026-06-07",    # Start date
    "STOP_TIME": "2026-06-08",     # End date
    "STEP_SIZE": "1 d"             # Step size (daily)
}

# Make the GET request
response = requests.get(BASE_URL, params=params)

# Check response status
if response.status_code == 200:
    data = response.json()
    print("Request successful. Summary:")
    print(data.get("result") or data)  # Print result section or entire response
else:
    print(f"Error: {response.status_code}")
    print(response.text)
