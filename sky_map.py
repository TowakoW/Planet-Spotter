# Generating skymap based on coordinates


# imports
from planet_spherical import alt_azmuth, find_RA_DEC, observer_loc
import numpy as np
from planet_data import System
import matplotlib.pyplot as plt
from datetime import datetime

def sph_calc(
        system: System,
        labels: list,
):
    observer = observer_loc()
    lat = observer["observer lat"]
    lon = observer["observer lon"]

    spherical_positions = find_RA_DEC(system, labels)

    # get altitude and azimuth
    alt_az_positions = []
    for radius, ra, dec in spherical_positions:
        altitude, azimuth = alt_azmuth(ra, dec, lat, lon)
        alt_az_positions.append([altitude, azimuth])

    return np.array(alt_az_positions)

def sky_plot(
        system: System,
        labels: list,
        colors: list,
        legend: bool,
        alt_az,
        ax):
    """
    Plot polar graph scatterplot showing locations where objects can be found for night sky
    """

    ax.clear()

    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_rmax(90)
    ax.set_rmin(0)
    ax.set_rticks([0, 30, 60, 90])
    ax.set_yticklabels(['90°', '60°', '30°', '0° (horizon)'])
    ax.set_xticks(np.arange(8) * (np.pi / 4))
    ax.set_xticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])

    filtered_labels = [name for name in labels if name != "Earth"]
    if len(filtered_labels) != len(alt_az):
        raise ValueError(
            f"Label and sky data length mismatch: {len(filtered_labels)} labels, {len(alt_az)} sky entries"
        )

    legend_handles = []
    for index, alt_az_data in enumerate(alt_az):
        name = filtered_labels[index]
        alt_rad, az_rad = alt_az_data[0], alt_az_data[1]
        alt_deg = np.degrees(alt_rad)

        if legend:
            color = colors[labels.index(name)]
            legend_handles.append(
                plt.Line2D(
                    [],
                    [],
                    linestyle='',
                    marker='o',
                    markersize=8,
                    markerfacecolor=color,
                    markeredgecolor=color,
                    label=name,
                )
            )

        if alt_deg < 0:
            print(f"Skipping {name}: Hidden below horizon (ALT: {alt_deg:.1f}°)")
            continue

        r_plot = 90.0 - alt_deg
        ax.scatter(az_rad, r_plot, c=colors[labels.index(name)], s=100, label=name, zorder=3)

    if legend:
        ax.legend(handles=legend_handles, loc='upper left')

    theta = np.linspace(0, 2 * np.pi, 360)
    ax.plot(theta, np.full_like(theta, 90), color="black", linewidth=1)

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ax.set_title(
        f"Local Sky View (Topocentric Polar Projection)\nTime: {time}",
        pad=18,
        fontsize=10,
    )
    plt.grid(True, linestyle='--', alpha=0.6)
    ax.figure.tight_layout()



if __name__ == "__main__":
    sky_plot()

