import numpy as np
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation
from astropy.table import Table
import json
from pathlib import Path
import utils
#
#
def get_path():
    path = Path(__file__).parent / "stars.csv"
    return path
#
#
path = utils.get_path()
with open(path) as f:
    sites = json.load(f)
#
#
def main():
    path = utils.get_data()
    if path == None:
        print("error")
    else:
        t = Table.read(path, format="ascii.csv")
        coords = SkyCoord(t["ra"], t["dec"], unit=(u.hourangle, u.deg))
        lst = Time.now().sidereal_time("apparent", longitude=utils.site_location(sites["lick"]).lon)
        ha = (lst - coords.ra).wrap_at(12*u.hourangle)
        print(ha.hour)

if __name__ == "__main__":
    main()