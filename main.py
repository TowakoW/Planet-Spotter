from planet_data import get_initial_conditions
from horizons_parse import horizons_specifics
from planet_calc import plot_initial


INITIAL_CONDITIONS = "solar_system"

def main():
    system, labels, colors, legend = get_initial_conditions(INITIAL_CONDITIONS)
    print("Number of Objects:\n", system.num_particles)
    print("Initial Positions (km):\n", system.x)
    print("Initial Velocities (km/s):\n", system.v)
    print("Object GM (km^3/s^2):\n", system.Gm)

    plot_initial(
        system=system,
        labels=labels,
        colors=colors,
        legend=legend
    )

if __name__ == "__main__":
    main()