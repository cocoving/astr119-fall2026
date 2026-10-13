# trap1.py -- predict what this prints, then run it.
h_ice = 2.5e6          # J/kg, energy to sublimate ice


def energy(m):
    return m * h_ice


print(energy(2.0))
h_ice = 5.0e6
print(energy(2.0))
