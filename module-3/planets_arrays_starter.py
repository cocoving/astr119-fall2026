# planets_arrays_starter.py -- the ten planets from exotemp.py, ready to become numpy arrays (Pod 4).
# Copy this file to planets_arrays.py and work on the copy.
from math import pi

SIGMA = 5.67e-8          # Stefan-Boltzmann constant, W m^-2 K^-4
L_SUN = 3.8e26           # solar luminosity, W
AU = 1.496e11            # meters per AU

name = ["Earth", "Mars", "HD 209458 b", "51 Peg b", "TRAPPIST-1 e",
        "Kepler-22 b", "55 Cnc e", "HD 189733 b", "Kepler-452 b", "Proxima b"]
lum = [1.0, 1.0, 1.6, 1.3, 0.00055, 0.79, 0.58, 0.34, 1.2, 0.0016]          # star luminosity, solar units
dist_au = [1.000, 1.524, 0.047, 0.052, 0.029, 0.85, 0.0154, 0.031, 1.046, 0.0485]   # planet distance, AU


def t_eq(L, d):
    """Equilibrium temperature (K) of a planet at distance d (m) from a star of luminosity L (W).

    A perfectly absorbing sphere that radiates evenly over its whole surface.
    """
    return (L / (16 * pi * SIGMA * d**2)) ** 0.25


if __name__ == "__main__":
    # Last week's way: one planet at a time.
    for i in range(len(name)):
        T = t_eq(lum[i] * L_SUN, dist_au[i] * AU)
        print(f"{name[i]:14s} {T:7.1f} K")
