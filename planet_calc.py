# Calculating real time planet trajectory based on ephimeris data at time of call
'''
references:
https://alvinng4.github.io/grav_sim/5_steps_to_n_body_simulation/step1/
'''

# import
from astropy import constants as const
import numpy as np

# Constants:

# Needed Information:
# fetch_horizons_data(10) - Sun (GM)
# Target Planet position/velocity (x, y, z, vx, vy, vz)
# fetch_horizons_data(3) - earth barycenter data (x, y, z, vx, vy, vz)


# Physics Calc:
# F = G(m_1*m_2)/r**2
# a_planet = GM_sun/r**2



