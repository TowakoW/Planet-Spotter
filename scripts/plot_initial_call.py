import sys
import os
# ensure project root is on sys.path when running from scripts/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from planet_data import get_initial_conditions
from planet_calc import plot_initial


if __name__ == "__main__":
    system, labels, colors, legend = get_initial_conditions("solar_system")
    plot_initial(system, labels, colors, legend)
