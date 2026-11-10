import numpy as np
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz, get_sun
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta
import time
import json
from pathlib import Path
import utils
#
#
path = utils.get_path()
with open(path) as f:
    sites = json.load(f)
#
#
twilight_types = {"astronomical": {"morning": -18*u.deg, "evening": -12*u.deg},
                  "nautical": {"morning": -12*u.deg, "evening": -6*u.deg},
                  "civil": {"morning": -6*u.deg, "evening": -0.833*u.deg}
}
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
    tolerance = 1*u.s
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
    location = utils.site_location(site)
    a = local_now
    if local_now < local_noon:
        b = local_noon
        angle_one = angle["morning"]
        angle_two= angle["evening"]
    else:
        angle_one = angle["evening"]
        angle_two = angle["morning"]
        b = local_mn
    c = b + timedelta(hours=12)
    times = Time([a, b, c])
    sun = sun_alt(times, location)
    if (sun[0]-angle_one)*(sun[1]-angle_one) < 0:
        result = bisection(times[0], times[1], location, angle_one)
    else:
        result = bisection(times[1], times[2], location, angle_two)
    return result
#
#
def countdown(target):
    try:
        while True:
            left = (target - datetime.now(tz=target.tzinfo))
            secs = int(left.total_seconds())
            text = str(timedelta(seconds=secs))
            print(f"{text} ", end="\r", flush=True)
            if secs <= 0:
                break
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
#
#
def main():
    site = utils.index_dict(sites, "Select a site: ")
    angle = utils.index_dict(twilight_types, "Select a twilight type: ")
    now = Time.now()
    value = next_twilight(now, site, angle)
    value.precision = 0
    print(value.iso)
    value = value.to_datetime(timezone=ZoneInfo(site["tz"]))
    countdown(value)
    return value
#
#
if __name__ == "__main__":
    main()
#
#