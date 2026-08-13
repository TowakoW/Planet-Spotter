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
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(projection="3d")
        ax.set_xlabel("$x$ (KM)")
        ax.set_ylabel("$y$ (KM)")
        ax.set_zlabel("$z$ (KM)")

        # plot initial
        for i in range(system.num_particles):
                ax.scatter(
                        system.x[i, 0], system.x[i, 1], system.x[i, 2], marker="o", color=colors[i], label=labels[i]
                )

        if legend: 
                ax.legend()

        plt.show()

