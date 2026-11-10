import json
from pathlib import Path
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation
from zoneinfo import ZoneInfo
#
#
def get_path():
    path = Path(__file__).parent / "sites.json"
    return path
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
def site_location(site):
    location = EarthLocation(lat=site["lat"]*u.deg, lon=site["lon"]*u.deg, height=site["height"]*u.m)
    return location
#
#
def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")
#
#
def index_dict(options, prompt):
    while True:
        for i, name in enumerate(list(options)):
            print(i+1, name)
        index = get_int_input(prompt)
        if not 1 <= index <= len(options):
            print("Invalid selection. Please try again.")
        else:
            key = list(options)[index-1]
            option = options[key]
            break
    return option
#
#
def get_local_time(Time, tz):
    local_time = Time.to_datetime(timezone=ZoneInfo(site["tz"]))
    return local_time
#
#