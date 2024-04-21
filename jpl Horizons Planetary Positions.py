import numpy as np
import matplotlib.pyplot as plt
from astroquery.jplhorizons import Horizons
from astropy.time import Time
from astropy.constants import au

def get_planet_positions(planets, start_date, end_date, step):
    positions = {}
    times = Time(np.arange(start_date.mjd, end_date.mjd, step), format='mjd')
    for planet in planets:
        obj = Horizons(id=planet, epochs=times.jd, location='500')
        eph = obj.ephemerides()
        # Ensure ephemerides data is not empty
        if len(eph) > 0:
            # Check available columns in the ephemerides data
            available_columns = eph.columns
            # Choose appropriate columns for x and y positions
            if 'x' in available_columns and 'y' in available_columns:
                positions[planet] = (eph['x'] * au.value, eph['y'] * au.value)
            elif 'RA' in available_columns and 'DEC' in available_columns:
                # Convert RA and DEC to x and y positions
                ra_rad = np.radians(eph['RA'])
                dec_rad = np.radians(eph['DEC'])
                positions[planet] = (eph['delta'] * au.value * np.cos(dec_rad) * np.cos(ra_rad),
                                     eph['delta'] * au.value * np.cos(dec_rad) * np.sin(ra_rad))
            else:
                print(f"Could not find necessary columns for planet {planet}. Skipping.")
        else:
            print(f"No ephemerides data found for planet {planet}. Skipping.")
    return times, positions



def plot_orbits(positions):
    plt.figure(figsize=(10, 10))
    for planet, (x, y) in positions.items():
        plt.plot(x, y, label=planet)
    plt.title('Orbits of Planets in the Solar System')
    plt.xlabel('Distance from Sun in km (x-axis)')
    plt.ylabel('Distance from Sun in km (y-axis)')
    plt.axhline(0, color='grey', lw=0.5)
    plt.axvline(0, color='grey', lw=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

# Define planets and the time range
planets = ['199', '299', '399', '499', '599', '699', '799', '899']  # Mercury to Neptune
start_date = Time('2023-01-01')
end_date = Time('2023-12-31')
step = 5  # days

# Retrieve positions
times, positions = get_planet_positions(planets, start_date, end_date, step)

# Plot orbits
plot_orbits(positions)
