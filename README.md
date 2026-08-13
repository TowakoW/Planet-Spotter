# Planet Spotter
Planet Spotter is a simple program that pulls planet data from NASA JPL's Horizons API and creates a short term simulation based on initial values. The goal is to create a program that allows users to see current planet locations relative to their current location on earth, as well as one of my first endeavors to become more familar with Python programming!

## Method
### Step 1: Horizons API
> horizons_api.py

> horizons_parse.py

Real-time information is fetched from NASA JPL Horizons API for all planets in the solar system as well as the Sun and Pluto. 

- Hopefully moons will be added in the future

The recieved output is parsed to take only each object's GM (km^3/s^2) and ephemeris data (x, y, z, vx, vy, vz).

## Step 2: Initial Plotting
> planet_data.py
> planet_calc.py

The parsed data is plotted on a 3d graph with Matplotlib.pyplot. 

## Step 3: Physics Simulation
> planet_calc.py

Using the Semi-Implicit Euler method, the locations of the planets are calculated and updated on the graph. 

## Step 4: Translating to Local Perspectives
work in progress...

## Resources
NASA JPL Horizons API:
https://ssd.jpl.nasa.gov/horizons/

"5 steps to N-body simulation" by alvinng4:
https://alvinng4.github.io/grav_sim/5_steps_to_n_body_simulation/