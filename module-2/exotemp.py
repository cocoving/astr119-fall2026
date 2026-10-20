import math
import sys

from matplotlib.cm import hot

sb = 5.67*10**-8
pi = math.pi


def t_eq(L, D, A=0):
    T_eq = (L*(1-A)/((D**2)*16*pi*sb))**(1/4)
    
    return (T_eq)

planets = [   # name, luminosity (solar units), distance (AU)
    ["Earth",        1.0,     1.000],
    ["Mars",         1.0,     1.524],
    ["HD 209458 b",  1.6,     0.047],
    ["51 Peg b",     1.3,     0.052],
    ["TRAPPIST-1 e", 0.00055, 0.029],
    ["Kepler-22 b",  0.79,    0.85],
    ["55 Cnc e",     0.58,    0.0154],
    ["HD 189733 b",  0.34,    0.031],
    ["Kepler-452 b", 1.2,     1.046],
    ["Proxima b",    0.0016,  0.0485],
]

if __name__ == '__main__':
    for i in range(len(planets)):
        name = planets[i][0]
        L = planets[i][1]*3.8*10**26
        D = planets[i][2]*1.496*10**11
        T_eq = t_eq(L,D)
        how_hot = 'hot' if T_eq > 1000 else "not hot"
        print(f"{name}: {T_eq:.0f} K, {how_hot}")
        
        
