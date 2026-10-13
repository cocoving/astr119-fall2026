# trap2.py -- predict both lines, then run it.
h_ice = 2.5e6


def oops():
    h_ice = 0.0
    return h_ice


print(oops())
print(h_ice)
