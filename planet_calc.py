# Calculating real time planet trajectory based on ephimeris data at time of call

# import
from astropy import constants as const
import numpy as np
from planet_data import System
import matplotlib.pyplot as plt
# from planet_data import System

# Constants:

# Needed Information:
# fetch_horizons_data(10) - Sun (GM)
# Target Planet position/velocity (x, y, z, vx, vy, vz)
# fetch_horizons_data(3) - earth barycenter data (x, y, z, vx, vy, vz)


# Physics Calc:
# F = G(m_1*m_2)/r**2
# a_planet = GM_sun/r**2


def plot_initial(
        system: System,
        labels: list,
        colors: list,
        legend: bool,
    ) -> None:
        """
        Plots the initial positions.
        Parameters:
        system: System
            system name ("solary_system")
        labels: list
            labels for objects
        colors: list
            list of colors used for objects
        legend: bool
            whether to show legend or not
        """

        # Create figure and 3d axes
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(projection="3d")
        ax.set_xlabel("$x$ (KM)")
        ax.set_ylabel("$y$ (KM)")
        ax.set_zlabel("$z$ (KM)")

        # Set self-centering graph size
        max_val = int(5.5e+09)

        ax.set_xlim(-max_val, max_val)
        ax.set_ylim(-max_val, max_val)
        ax.set_zlim(-max_val, max_val)

        # plot initial
        for i in range(system.num_particles):
                ax.scatter(
                        system.x[i, 0], system.x[i, 1], system.x[i, 2], marker="o", color=colors[i], label=labels[i]
                )

        if legend: 
                ax.legend()

        plt.show()


# PHYSICS!!
# Semi-implicit Euler method

def acceleration(
                a: np.ndarray,
                system: System
                ) -> None:
        """
        Computes the gravitational acceleration
        
        Parameters
        -----
        a: np.ndarray
            Gravitational acceleration array to be modified, shape (N, 3)
        system: System
            System object ("solar_system")
        
        Reference
        -----
        "5 Steps to N-body Simulation" by alvinng4: 
        https://alvinng4.github.io/grav_sim/5_steps_to_n_body_simulation/step2/#implementation-3-advanced
        """
        # Empty acceleration array
        a.fill(0.0)

        # Declare variables
        x = system.x
        GM = system.Gm

        # Displacement vector
        r_ij = x[:, np.newaxis, :] - x[np.newaxis, :, :]
