import numpy as np
from typing import Tuple, List, Optional
from main import horizons_specifics

'''
references:
https://alvinng4.github.io/grav_sim/5_steps_to_n_body_simulation/step1/
'''


class System:
    def __init__ (self, num_particles: np.ndarray, MG: np.ndarray, m: np.ndarray, x: np.ndarray, v: np.ndarray) -> None:
                  self.num_particles = num_particles
                  self.MG = MG
                  self.m = m
                  self.x = x
                  self.v = v

    def center_of_mass_correction(self) -> None:
            """ Set center of mass of position and velocity to zero"""
            x_cm = np.zeroes(3)
            v_cm = np.zeroes(3)
            M = 0.0
            for i in range(self.num_particles):
                x_cm += self.m[i] * self.x[i]
                v_cm += self.m[i] * self.v[i]
                M += self.m[i]
            x_cm /= M
            v_cm /= M
            self.x -= x_cm
            self.v -= v_cm




def get_initial_conditions(initial_condition: dict
                           ) -> Tuple[System, List[Optional[str]]]:
        """
        Returns initial conditions for objects in 
        Solar System in AU, days, and M_sun
        
        
        Parameters
        -----
        initial_condition: str
            name for initial condition
        
        Returns
        -----
        system: System
            name of system
        labels: list
            Lables for objects
        colors: list
            colors for objects
        legend: bool
            whether to show legend
        """

        # GM values (AU^3/s^2)
        GM_AU_S = {
                "Sun": horizons_specifics(10, 'gm'),
                "Mercury": horizons_specifics(199, 'gm'),
                "Venus": horizons_specifics(299, 'gm'),
                "Earth": horizons_specifics(399, 'gm'),
                "Mars": horizons_specifics(499, 'gm'),
                "Jupiter": horizons_specifics(599, 'gm'),
                "Saturn": horizons_specifics(699, 'gm'),
                "Uranus": horizons_specifics(799, 'gm'),
                "Neptune": horizons_specifics(899, 'gm'),
                "Pluto": horizons_specifics(999, 'gm')
        }

        