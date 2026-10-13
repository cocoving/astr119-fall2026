# cometlife_ref.py -- how many orbits does a sublimating comet have left?
# Reference version of the Pod 0 program, used in Pod 1B. Everything in SI units.
# Pod 1B works on a copy of this file (cometlife.py). Leave this one as it is, so you can always go back to it.
from math import sqrt, pi

L = 3.8e26          # solar luminosity, J/s
GM = 1.3271e20      # G times the Sun's mass, m^3/s^2
h_ice = 2.5e6       # energy to sublimate 1 kg of ice, J/kg
AU = 1.49e11        # meters per AU

R = 2000.0          # comet radius, m (2 km)
rho = 500.0         # comet density, kg/m^3
A = 0.0             # albedo
a = 3.12 * AU       # semi-major axis, m
e = 0.5             # eccentricity

H_sol = (pi / 2) * (1 - A) * R**2 * L / sqrt(GM) / sqrt(a * (1 - e**2))   # J absorbed per orbit
dM = H_sol / h_ice                                                       # kg lost per orbit
dr = dM / (4 * pi * rho * R**2)                                          # m of radius lost per orbit

print("dr =", dr, "m per orbit")
print("orbits left =", R / dr)
