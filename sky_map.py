# Generating skymap based on coordinates
from planet_spherical import cart_to_sph
from steal_data import find_LST, fetch_coords
import numpy as np

def alt_azmuth(ra, dec):
    """
    Calculate hour angle, altitude, and azimuth using spherical coordinates
    
    Parameters
    -----
    
    Equations
    -----
    Hour angle (H) = LST - RA
    (where H >= 0)

    altitude (a) = arcsin(sin(dec)sin(lat) + cos(dec)cos(lat)cos(H))

    azimuth (A) = arccos((sin(dec)-sin(a)sin(lat))/cos(a)cos(lat))
    """
    coordinates = fetch_coords()
    LST = find_LST(coordinates)

    lat = coordinates[0]
    lon = coordinates[1]

    # calculate hour angle
    H = LST - ra

    # calculate altitude
    alt_ins = (np.sin(dec) * np.sin(lat)) + (np.cos(dec) * np.cos(lat) * np.cos(H))
    altitude = np.arcsin(alt_ins)

    # calculate azimuth
    az_top = (np.sin(dec) - np.sin(altitude) * np.sin(lat))
    az_bot = (np.cos(altitude) * np.cos(lat))
    azimuth = np.arccos(az_top/az_bot)

    print(altitude, azimuth)
    return np.array([altitude, azimuth])

