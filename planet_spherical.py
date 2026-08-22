# Converting from cartesian coordinates (x,y,z) to spherical (right ascension, declination, r)

# import
from astropy import constants as const
import numpy as np
from planet_data import System
import matplotlib.pyplot as plt
from datetime import datetime
# from planet_data import System
# from typing import Literal


def cart_to_sph(system: System) -> np.ndarray:
    """
    Converting cartesian coordinates to RA/DEC from the perspective of a location on Earth

    Parameters
    -----
    system: System
        system object ("solar_system").
    
    Equations
    -----
    r = sqrt(x**2 + y**2 + z**2)

    dec = arcsin(z/r)

    asc = atan2(y, x)
    """
    # Defining x, y, and z within system.x for convenience:
    x_pos = system.x[0]
    y_pos = system.x[1]
    z_pos = system.x[2]
    
   # conversions
    r = np.sqrt(x_pos**2 + y_pos**2 + z_pos**2)
    dec = np.arcsin(z_pos/r)
    asc = np.atan2(y_pos, x_pos)
    return np.array(r, asc, dec)


def center_observer(system: System, labels):
    """
    Converts system center to a point on Earth (topocentric coordinates). 

    Parameters
    -----
    system: System
        system object ("solar_system")
    location: str
        latitude/longitude/LST coordinates on the Earth to be the obervation site
    """
    # Defining x, y, and z within system.x for convenience:
    # x_pos = system.x[0]
    # y_pos = system.x[1]
    # z_pos = system.x[2]

    earth_index = labels.index("Earth")
    earth_pos = system.x[earth_index]

    earth_center_pos = system.x - earth_pos

    return earth_center_pos