import sys
import os
# ensure project root is on sys.path when running from scripts/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from planet_data import get_initial_conditions
from planet_calc import plot_initial
from horizons_parse import horizons_specifics
from horizons_api import fetch_horizons_data


if __name__ == "__main__":
    print(horizons_specifics(999, "all"))
    # system, labels, colors, legend = get_initial_conditions("solar_system")
    # print(system)
    # plot_initial(system, labels, colors, legend)
