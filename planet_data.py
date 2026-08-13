import numpy as np
from typing import Tuple, List, Optional
from horizons_parse import horizons_specifics

'''
references:
https://alvinng4.github.io/grav_sim/5_steps_to_n_body_simulation/step1/
'''


class System:
    def __init__(self, num_particles: int | None = None, Gm: np.ndarray | None = None, m: np.ndarray | None = None, x: np.ndarray | None = None, v: np.ndarray | None = None) -> None:
        # Prefer to infer number of particles from provided position array
        if x is not None:
            self.num_particles = int(len(x))
        else:
            self.num_particles = int(num_particles) if num_particles is not None else 0

        # Store gravitational parameters and masses
        # keep attribute name `Gm` to match callers
        self.Gm = Gm
        # default masses to ones if not provided
        self.m = m if m is not None else (np.ones(self.num_particles) if self.num_particles > 0 else None)
        self.x = x
        self.v = v

    def center_of_mass_correction(self) -> None:
        """ Set center of mass of position and velocity to zero"""
        if self.x is None or self.v is None or self.m is None:
            return

        x_cm = np.zeros(3)
        v_cm = np.zeros(3)
        M = 0.0
        for i in range(self.num_particles):
            x_cm += self.m[i] * self.x[i]
            v_cm += self.m[i] * self.v[i]
            M += self.m[i]
        if M == 0:
            return
        x_cm /= M
        v_cm /= M
        self.x -= x_cm
        self.v -= v_cm




def get_initial_conditions(initial_condition: dict
                           ) -> Tuple[System, List[Optional[str]]]:
        """
        Returns initial conditions for objects in 
        Solar System in km and seconds:
            Num_particles
            Gm (mass * G constant) (km^3/s^2)
            x (position) (km)
            v (velocity) (km/s)
        
        
        Parameters
        -----
        initial_condition: str
            name for initial condition
            "solar_system" for solar system data
        
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


        # ephemeris rows: [jd, datetime, x, y, z, vx, vy, vz, ...]
        SOLAR_SYSTEM_POS = {
            "Sun": sun_eph[2:5],
            "Mercury": mercery_eph[2:5],
            "Venus": venus_eph[2:5],
            "Earth": earth_eph[2:5],
            "Mars": mars_eph[2:5],
            "Jupiter": jupiter_eph[2:5],
            "Saturn": saturn_eph[2:5],
            "Uranus": uranus_eph[2:5],
            "Neptune": neptune_eph[2:5],
            "Pluto": pluto_eph[2:5]
        }

        SOLAR_SYSTEM_VEL = {
            "Sun": sun_eph[5:8],
            "Mercury": mercery_eph[5:8],
            "Venus": venus_eph[5:8],
            "Earth": earth_eph[5:8],
            "Mars": mars_eph[5:8],
            "Jupiter": jupiter_eph[5:8],
            "Saturn": saturn_eph[5:8],
            "Uranus": uranus_eph[5:8],
            "Neptune": neptune_eph[5:8],
            "Pluto": pluto_eph[5:8]
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

            G1 = np.array(GM_AU_S["Sun"])
            G2 = np.array(GM_AU_S["Mercury"])
            G3 = np.array(GM_AU_S["Venus"])
            G4 = np.array(GM_AU_S["Earth"])
            G5 = np.array(GM_AU_S["Mars"])
            G6 = np.array(GM_AU_S["Jupiter"])
            G7 = np.array(GM_AU_S["Saturn"])
            G8 = np.array(GM_AU_S["Uranus"])
            G9 = np.array(GM_AU_S["Neptune"])
            G10 = np.array(GM_AU_S["Pluto"])
            
            R1 = np.array(SOLAR_SYSTEM_POS["Sun"], dtype=float)
            R2 = np.array(SOLAR_SYSTEM_POS["Mercury"], dtype=float)
            R3 = np.array(SOLAR_SYSTEM_POS["Venus"], dtype=float)
            R4 = np.array(SOLAR_SYSTEM_POS["Earth"], dtype=float)
            R5 = np.array(SOLAR_SYSTEM_POS["Mars"], dtype=float)
            R6 = np.array(SOLAR_SYSTEM_POS["Jupiter"], dtype=float)
            R7 = np.array(SOLAR_SYSTEM_POS["Saturn"], dtype=float)
            R8 = np.array(SOLAR_SYSTEM_POS["Uranus"], dtype=float)
            R9 = np.array(SOLAR_SYSTEM_POS["Neptune"], dtype=float)
            R10 = np.array(SOLAR_SYSTEM_POS["Pluto"], dtype=float)

            V1 = np.array(SOLAR_SYSTEM_VEL["Sun"], dtype=float)
            V2 = np.array(SOLAR_SYSTEM_VEL["Mercury"], dtype=float)
            V3 = np.array(SOLAR_SYSTEM_VEL["Venus"], dtype=float)
            V4 = np.array(SOLAR_SYSTEM_VEL["Earth"], dtype=float)
            V5 = np.array(SOLAR_SYSTEM_VEL["Mars"], dtype=float)
            V6 = np.array(SOLAR_SYSTEM_VEL["Jupiter"], dtype=float)
            V7 = np.array(SOLAR_SYSTEM_VEL["Saturn"], dtype=float)
            V8 = np.array(SOLAR_SYSTEM_VEL["Uranus"], dtype=float)
            V9 = np.array(SOLAR_SYSTEM_VEL["Neptune"], dtype=float)
            V10 = np.array(SOLAR_SYSTEM_VEL["Pluto"], dtype=float)

            Gm = np.array(
                   [
                         G1,
                         G2,
                         G3,
                         G4,
                         G5,
                         G6,
                         G7,
                         G8,
                         G9,
                         G10 
                   ]
            )

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
                        R10
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
                        V10
                    ]
                )

            system = System(
                num_particles= 9,
                Gm=Gm,
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