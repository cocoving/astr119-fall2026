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
#
#
def site_location(site):
    location = EarthLocation(lat=site["lat"]*u.deg, lon=site["lon"]*u.deg, height=site["height"]*u.m)
    return location
#
#
def sun_alt(t, location):
    frame = AltAz(obstime=t, location=location)
    sun = get_sun(t).transform_to(frame)
    return sun.alt
#
#
def bisection(a, b, location, angle):
    sun_a = sun_alt(a, location)
    count = 0
    tolerance = 1*u.min
    while abs(a - b) > tolerance:
        count += 1
        mid = a + (b-a)/2
        if count == 20:
            print("Max loops reached")
            break
        sun_mid = sun_alt(mid, location)
        if (sun_a-angle)*(sun_mid-angle) < 0:
            b = mid
        else:
            a = mid
    return mid
#
#
def next_twilight(now, site, angle):
    local_now = now.to_datetime(timezone=ZoneInfo(site["tz"]))
    local_noon = datetime(local_now.year, local_now.month, local_now.day, 12, tzinfo=ZoneInfo(site["tz"]))
    local_mn = local_noon + timedelta(hours=12)
    location = site_location(site)
    a = local_now
    if local_now < local_noon:
        b = local_noon
    else:
        b = local_mn
    c = b + timedelta(hours=12)
    times = Time([a, b, c])
    sun = sun_alt(times, location)
    if (sun[0]-angle)*(sun[1]-angle) < 0:
        result = bisection(times[0], times[1], location, angle)
    else:
        result = bisection(times[1], times[2], location, angle)
    return result
#
#
def main():
    now = Time.now()
    value = next_twilight(now, sites["lick"], -18*u.deg)
    print(value)
    return value
#
#
if __name__ == "__main__":
    main()
#
#