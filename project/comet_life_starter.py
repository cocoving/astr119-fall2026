#------------------------------------------------------------------------------
# A comet's life.
# Simulation of a comet's gradual sublimation.
#------------------------------------------------------------------------------

import numpy as np
from scipy.optimize import root_scalar

def _main():
    """Execute the full calculation."""
    a, e, R, Rc, A = _get_inputs()

    dr_per_orbit = one_orbit_shrinkage(a, e, A)
    norbits = round((R - Rc)/dr_per_orbit)
    years_per_orbit = orbital_period(a)/3.14e7
    nyears = round(norbits*years_per_orbit)
    print(f"This comet will last about {nyears} years ({norbits} orbits).")

def _get_inputs():
    """Get the comet's specs from the user."""
    a = float(input("Orbit semi-major axis [AU]: "))
    e = float(input("Orbit eccentricity: "))
    R = float(input("Comet outer radius [km]: "))
    Rc = float(input("Comet core radius [km]: "))
    A = float(input("Surface albedo: "))

    AU = 149.6e9 # AU in m
    a = a*AU
    R = R*1e3
    Rc = Rc*1e3
    return a, e, R, Rc, A

def orbital_period(a):
    """Return period of elliptical Keplerian solar orbit."""
    P = 1 ### REPLACE WITH YOUR CODE
    return P

def orbit_radius(t, a, e):
    """Return orbit radius at time t from perihelion.

    Solve Kepler's equation at time t for an elliptical orbit with parameters
    a and e and return distance from focus.
    """
    # First define some orbit parameters
    P = orbital_period(a)
    n = 2*np.pi/P # mean motion
    tau = 0.0 # time at perihelion
    M = (n*(t - tau))%(2*np.pi) # mean anomaly

    # Now lion-hunt Kepler's equation for eccentric anomaly, E
    ### Kepler's equation is: E - e*sin(E) = M
    ### THE ROOT MUST BE IN THE INTERVAL [0,2PI], SO THIS IS AN EASY CASE FOR
    ### THE LION HUNT SLASH BISECTION ROOT FINDING ALGORITHM
    E = 0 ### REPLACE WITH THE RESULT OF THE ROOT FINDER

    # Return radius (distance from focus)
    r = a*(1 - e*np.cos(E))
    return r

def surface_temperature(d, A):
    """Return temperature at distance d from the sun.

    Solve energy balance for spherical surface with albedo A at solar distance
    d for equilibrium temperature.
    """
    # We need come constants
    sigma = 5.67e-8 # Stefan-Boltzmann constant [W m^-2 K^-4]
    L_sun = 3.8e26 # solar luminosity [W]
    H = 2.8345e6 # latent heat of ice sublimation [J/kg]

    # Lion hunt for equilibrium temperature
    ### TO USE THE BISECTION ALGORITHM WE NEED AN INITIAL BRACKET WHERE WE KNOW
    ### THE ROOT MUST BE. IN THIS CASE, THE ROOT IS THE TEMPERATURE. SO WITHOUT
    ### TOO MUCH HESITATION WE CAN ASSUME IT IS HOTTER THAN ABSOLUTE ZERO AND
    ### COLDER THAN THE SUN, SAY 6000 K.
    T = 0 ### REPLACE WITH THE RESULT OF THE ROOT FINDER

    # Return temperature
    return T

def sublimation_rate(T):
    """Return sublimation rate [kg m^-2 s^-2] from ice surface.
    
    The idea to use saturation vapor pressure is due to Einstein, I think.
    """
    # We need these constants
    H = 2.83e6 # latent heat of ice sublimation [J/kg]
    KB = 1.381e-23 # Boltzmann constant [J/K]
    alfa, beta = 3.56e12, 6141.667 # saturation pressure parameters [Pa, K]
    m = 0 ### REPLACE WITH MOLECULAR MASS OF WATER [kg]
    return 0 ### REPLACE WITH SUBLIMATION RATE

def shrinkage_rate(Sdot):
    """Return comet shrinkage rate dR/dt given sublimation rate.

    This is just geometry! If Sdot is the rate of mass loss [kg s^-1 m^-2] what
    is the rate of radius change? Assume a perfect sphere, of course.
    """
    dmdt = Sdot*4*np.pi
    rho_ice = 500
    drdt = 0 ### REPLACE WITH CORRECT SHRINKAGE RATE
    return drdt

def one_orbit_shrinkage(a, e, A):
    """Return total shrinkage during one orbit."""
    ### START AT TIME t=0, CHOOSE A REASONABLE SMALL TIME STEP dt 
    ### NOW, REPEAT UNTIL TIME IS ONE ORBITAL PERIOD
    ### IN THE LOOP:
    ###     CALCULATE HOW FAR AWAY IS THE SUN
    ###     CALCULATE THE SURFACE TEMPERATURE
    ###     CALCULATE THE SUBLIMATION RATE
    ###     CALCULATE THE SHRINKAGE RATE
    ###     HOW MUCH DID THE RADIUS CHANGE DURING THIS SMALL TIME STEP? ADD
    ###     THAT TO THE TOTAL SHRINKAGE
    ###     DON'T FORGET TO UPDATE THE TIME!
    total_shrinkage = 1 ### REPLACE WITH THE RESULT OF THE LOOP
    return total_shrinkage

### To run as script
if __name__ == '__main__':
    _main()