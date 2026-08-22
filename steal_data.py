# Taking IP address and assigns to a location to be used for reference in sky visualizer
# import geopy
import requests
from urllib.parse import urlencode
import json
import sys
import numpy as np
import datetime

def fetch_coords():
    """
    Fetches IP address to use for relative location, converts to coordinates.

    Resources
    -----
    ipify: https://www.ipify.org/
        fetches IP address
    ip-api.com: https://ip-api.com/
        fetches coordinates
    """
    # Submit API request and decode JSON
    ipresponse = requests.get("https://api64.ipify.org?format=json")
    # print("URL:", response)
    try:
        data = json.loads(ipresponse.text)
    except ValueError:
        print("unable to decode JSON results.")

    
    # if response.status_code != 200:
        # raise RuntimeError(f"Error: {response.status_code}\n{response.text}")
        sys.exit(1)

    print("IP request successful.")

    # Parses IP address taken from fetch_IP
    address = data['ip']
    # print(address)
    # return address
   
    BASE_URL = "http://ip-api.com/json/"
    url = f"{BASE_URL}{address}?"
    coordresponse = requests.get(url)
    try:
            coord = json.loads(coordresponse.text)
    except ValueError:
            print("unable to decode JSON results.")

    print("Coordinate request sucessful.")

    # Parses JSON for Lat/Lon
    lat = coord['lat']
    lon = coord['lon']
    coordinates = np.array([lat, lon])
    print(coordinates)
    return coordinates

# testing
# addr = fetch_IP()
# coords = ip_to_coords(addr)

def find_LST(coords):
    """
    Finding local sidereal time

    Parameters
    -----
    lon: float
        Longitude

    Other Variables
    -----
    d: float
        days elapsed since January 1, 2000, at 12:00 UT
    UT: float
        current Universal Time in decimal hours

     Equation
     -----
     LST = 100.46 + 0.985547 * d + lon + 15 * UT
     """
    # get current UTC time
    now = datetime.datetime.now(datetime.timezone.utc)

    # calculate Julian date relative to J2000.0
    j2000 = datetime.datetime(2000, 1, 1, 12, 0, tzinfo=datetime.timezone.utc)
    elapsed = (now - j2000).total_seconds()
    d = elapsed/86400.0 # convert to decimal time

    # calculate Universal Time hours for current day
    ut_hrs = now.hour + (now.minute / 60.0) + (now.second / 3600.0)

    # take longitude
    lon = coords[1]

    # Standard IAU LST formula
    lst = 100.46 + (0.98564736629 * d) + lon + (15.0 * ut_hrs)

    # limit angle to 360 degrees
    lst_deg = lst % 360

    print(lst_deg)
    return lst_deg

# find_LST(coords)

# if __name__ == "__main__":
#     # fetch_IP()
