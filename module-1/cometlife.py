import numpy as np
    
#Code takes the radius of a comet and calculates the rate at which it will shrink and how many orbits it will last before it is gone.

pi = np.pi
# no units
e = 0.5
# no units
a = 4.65e11
#meters
L_sun = 3.8e26
#jouls per second
GM_sun = 1.3271e20
# meters cubed per second squared
Rho = 500
#kilograms per meter cubed
A = 0
#no units
h = 2.5e6
# jouls per kilogram

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

R = get_float_input("Enter the radius of the comet: ")

H_sol = (pi/2)*(1-A)*(R**2)*(L_sun/np.sqrt(GM_sun))*(1/np.sqrt(a*(1-e**2)))
delta_M = H_sol/h
delta_r = (delta_M)/(4*pi*Rho*R**2)

print(f"The comet will shrink {delta_r:.2f} meters every orbit and will last for {R/delta_r:.2f} orbits.")