import astropy.units as u
from astropy.time import Time
#
#
def time_remaining(time, now):
    tr = int(round((time - now).to(u.s).value, 3))
    if tr < 0:
        return 0, 0, 0
    s, m, h= tr % 60, (tr // 60) % 60, tr // 3600
    return h, m, s
#
#