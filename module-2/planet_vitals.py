# This module holds some useful information about the solar system's planets
# https://ssd.jpl.nasa.gov/planets/phys_par.html

# my very energetic mother just sent us nine pies
name = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus',
         'Neptune', 'Pluto']

# Semi-major axes, in AU
semi_major_axis = [0.387, 0.723, 1.0, 1.52, 5.20, 9.58, 19.20, 30.05, 39.48]

# Does it have a moon?
has_moons = [False, False, True, True, True, True, True, True, True]

# Mass
mass = [0.330, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102, 0.0146] # in 10^24 kg

# diameter
diameter = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2370] # km

# rotation period
rotation = [58.65, 243.02, 0.999, 1.03, 0.41, 0.44, 0.72, 0.67, 6.38] # days