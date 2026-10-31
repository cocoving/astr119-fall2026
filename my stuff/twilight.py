#!/home/natha/miniconda3/envs/twilight/bin/python
import numpy as np
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz, get_sun
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta
#
#
sites = {
    "lick": {"lat": 37.3411, "lon": -121.6430, "height": 1283, "tz": "America/Los_Angeles"},
    "made up": {"lat": 0, "lon": 0, "height": 0, "tz": "UTC"}
}
s = sites["lick"]
#
#
def sun_alt(t, location):
    frame = AltAz(obstime=t, location=location)
    sun = get_sun(t).transform_to(frame)
    return sun.alt
#
#
def bisection(a, b, location):
    sun_a = sun_alt(a, location)
    count = 0
    tolerance = 1*u.s
    while abs(a - b) > tolerance:
        count += 1
        mid = a + (b-a)/2
        if count == 20:
            print("Max loops reached")
            break
        sun_mid = sun_alt(mid, location)
        if (sun_a+18*u.deg)*(sun_mid+18*u.deg) < 0:
            b = mid
        else:
            a = mid
    return mid
#
#
def next_twilight(now, location):
    local_now = now.to_datetime(timezone=ZoneInfo(s["tz"]))
    local_noon = datetime(local_now.year, local_now.month, local_now.day, 12, tzinfo=ZoneInfo(s["tz"]))
    local_mn = local_noon + timedelta(hours=12)
    a = local_now
    if local_now < local_noon:
        b = local_noon
    else:
        b = local_mn
    c = b + timedelta(hours=12)
    times = Time([a, b, c])
    sun = sun_alt(times, location)
    print(times.iso)
    print(sun)
    if (sun[0]+18*u.deg)*(sun[1]+18*u.deg) < 0:
        result = bisection(times[0], times[1], location)
    else:
        result = bisection(times[1], times[2], location)
    return result
#
#
def main():
    location = EarthLocation(lat=s["lat"]*u.deg, lon=s["lon"]*u.deg, height=s["height"]*u.m)
    now = Time.now()
    value = next_twilight(now, location)
    print(value)
#
#
if __name__ == "__main__":
    main()
