#Sublimating the comets in class/homework assignment
import math

H_ice = 2.5e6 # Latent heat of sublimation for ice in J/kg
L_sol = 3.8e26 # Solar luminosity in watts
pi = math.pi
H_ice = 2.5e6 # Latent heat of sublimation for ice in J/kg
L_sol = 3.828e26 # Solar luminosity in watts
GM_sol = 1.3271e20 # Gravitational constant times solar mass in m^3/s^2

def dr_per_orbit(R, A, p, a, e):
    a = a*1.496e11 # Convert AU to meters
    H_sol = ((pi/2)*(1-A)*(R**2)*(L_sol/(math.sqrt(GM_sol)))*(1/(math.sqrt(a*(1-e**2)))))
    dm = H_sol/H_ice # Mass loss per orbit in kg
    dr = (dm/(4*pi*p*(R**2))) #Loss of radius of comet per orbit
    return dr

dr = dr_per_orbit(1000, 0, 500, 3.12, 0.5)
print(dr)
print(1000/dr) # Number of orbits before the comet completely sublimates