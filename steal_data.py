# Taking IP address and assigns to a location to be used for reference in sky visualizer
import geopy
import requests
from urllib.parse import urlencode
import json
import sys
import numpy as np

def fetch_IP():
    """
    Fetches IP address to use for relative location
    
    Resources
    -----
    ipify: https://www.ipify.org/
    """
    # Submit API request and decode JSON
    response = requests.get("https://api64.ipify.org?format=json")
    # print("URL:", response)
    try:
        data = json.loads(response.text)
    except ValueError:
        print("unable to decode JSON results.")

    
    # if response.status_code != 200:
        # raise RuntimeError(f"Error: {response.status_code}\n{response.text}")
        sys.exit(1)

    print("IP request successful.")

    # Parses IP address taken from fetch_IP
    address = data['ip']
    # print(address)
    return address
   
def ip_to_coords(address):
    """
    Finds latitude/longitude from ip address, parses to only return latitude and longitude

    Resources
    -----
    ip-api.com: https://ip-api.com/
    """
    BASE_URL = "http://ip-api.com/json/"
    url = f"{BASE_URL}{address}?"
    response = requests.get(url)
    try:
            data = json.loads(response.text)
    except ValueError:
            print("unable to decode JSON results.")

    print("Coordinate request sucessful.")

    # Parses JSON for Lat/Lon
    lat = data['lat']
    lon = data['lon']
    coords = np.array([lat, lon])
    print(coords)
    return coords

# testing
addr = fetch_IP()
ip_to_coords(addr)

    

# if __name__ == "__main__":
#     # fetch_IP()
