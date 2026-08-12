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

        # Ephemeris data:
        sun_eph = horizons_specifics(10, 'ephemeris')
        mercery_eph = horizons_specifics(199, 'ephemeris')
        venus_eph = horizons_specifics(299, 'ephemeris')
        earth_eph = horizons_specifics(399, 'ephemeris')
        mars_eph = horizons_specifics(499, 'ephemeris')
        jupiter_eph = horizons_specifics(599, 'ephemeris')
        saturn_eph = horizons_specifics(699, 'ephemeris')
        uranus_eph =  horizons_specifics(799, 'ephemeris')
        neptune_eph = horizons_specifics(899, 'ephemeris')
        pluto_eph = horizons_specifics(999, 'ephemeris')


        SOLAR_SYSTEM_POS = {
                "Sun": sun_eph[1:4],
                "Mercury": mercery_eph[1:4],
                "Venus": venus_eph[1:4],
                "Earth": earth_eph[1:4],
                "Mars": mars_eph[1:4],
                "Jupiter": jupiter_eph[1:4],
                "Saturn": saturn_eph[1:4],
                "Uranus": uranus_eph[1:4],
                "Neptune": neptune_eph[1:4],
                "Pluto": pluto_eph[1:4]
        }

        SOLAR_SYSTEM_VEL = {
                "Sun": sun_eph[5:7],
                "Mercury": mercery_eph[5:7],
                "Venus": venus_eph[5:7],
                "Earth": earth_eph[5:7],
                "Mars": mars_eph[5:7],
                "Jupiter": jupiter_eph[5:7],
                "Saturn": saturn_eph[5:7],
                "Uranus": uranus_eph[5:7],
                "Neptune": neptune_eph[5:7],
                "Pluto": pluto_eph[5:7]
                }

        SOLAR_SYSTEM_COLORS = {
                "Sun": 'gold',
                "Mecury": 'tomato',
                "Venus": 'burlywood',
                "Earth": 'lightseagreen',
                "Mars": 'orangered',
                "Jupiiter": 'peru',
                "Saturn": 'slategrey',
                "Uranus": 'olive',
                "Neptune": 'teal',
                "Pluto": 'aquamarine'

        }


        if initial_condition == "solar_system":
        # m = np.array(
        #     [
        #         SOLAR_SYSTEM_MASSES["Sun"],
        #         SOLAR_SYSTEM_MASSES["Mercury"],
        #         SOLAR_SYSTEM_MASSES["Venus"],
        #         SOLAR_SYSTEM_MASSES["Earth"],
        #         SOLAR_SYSTEM_MASSES["Mars"],
        #         SOLAR_SYSTEM_MASSES["Jupiter"],
        #         SOLAR_SYSTEM_MASSES["Saturn"],
        #         SOLAR_SYSTEM_MASSES["Uranus"],
        #         SOLAR_SYSTEM_MASSES["Neptune"],
        #     ]
        # )

            R1 = np.array(SOLAR_SYSTEM_POS["Sun"])
            R2 = np.array(SOLAR_SYSTEM_POS["Mercury"])
            R3 = np.array(SOLAR_SYSTEM_POS["Venus"])
            R4 = np.array(SOLAR_SYSTEM_POS["Earth"])
            R5 = np.array(SOLAR_SYSTEM_POS["Mars"])
            R6 = np.array(SOLAR_SYSTEM_POS["Jupiter"])
            R7 = np.array(SOLAR_SYSTEM_POS["Saturn"])
            R8 = np.array(SOLAR_SYSTEM_POS["Uranus"])
            R9 = np.array(SOLAR_SYSTEM_POS["Neptune"])

            V1 = np.array(SOLAR_SYSTEM_VEL["Sun"])
            V2 = np.array(SOLAR_SYSTEM_VEL["Mercury"])
            V3 = np.array(SOLAR_SYSTEM_VEL["Venus"])
            V4 = np.array(SOLAR_SYSTEM_VEL["Earth"])
            V5 = np.array(SOLAR_SYSTEM_VEL["Mars"])
            V6 = np.array(SOLAR_SYSTEM_VEL["Jupiter"])
            V7 = np.array(SOLAR_SYSTEM_VEL["Saturn"])
            V8 = np.array(SOLAR_SYSTEM_VEL["Uranus"])
            V9 = np.array(SOLAR_SYSTEM_VEL["Neptune"])

            x = np.array(
                [  
                    R1,
                    R2,
                    R3,
                    R4,
                    R5,
                    R6,
                    R7,
                    R8,
                    R9,
                ]
            )
            v = np.array(
                [
                    V1,
                    V2,
                    V3,
                    V4,
                    V5,
                    V6,
                    V7,
                    V8,
                    V9,
                ]
            )

            system = System(
                num_particles= 9,
                x=x,
                v=v,
                # m=m,
                # G=G,
            )
            system.center_of_mass_correction()

            labels = list(SOLAR_SYSTEM_POS.keys())
            colors = list(SOLAR_SYSTEM_COLORS.values())
            legend = True

            return system, labels, colors, legend

        else:
            raise ValueError(f"Initial condition not recognized: {initial_condition}.")