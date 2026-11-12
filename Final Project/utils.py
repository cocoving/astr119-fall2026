import json
from pathlib import Path
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation
from zoneinfo import ZoneInfo
from astropy.table import Table
from urllib.parse import urlparse
import dataselector
#
#
BASE = Path(__file__).resolve().parent
DATA = BASE / "Data"
OBJECTS = DATA / "Objects"
#
#
def get_path():
    path = DATA / "sites.json"
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
def convert_to_csv(source):
    if source.startswith("http"):
        read_from = source
        file_name = "url_" + Path(urlparse(source).path).stem
    else:
        read_from = Path(source)
        file_name = read_from.stem
    save_path = OBJECTS / file_name
    save_path = save_path.with_suffix(".csv")
    t = Table.read(read_from, format="ascii.no_header", names=["name", "ra", "dec", "equinox", "comment"])
    t.write(save_path, format="csv", overwrite=True)
    return save_path
#
#
def get_data():
    source, kind = dataselector.data_selector(OBJECTS)
    if kind is None:
        path = None
    elif kind == "url":
        path = convert_to_csv(source)
    elif kind == "file":
        if Path(source).suffix.lower() == ".csv":
            if Path(source).parent == OBJECTS:
                path = Path(source)
            else:
                path = OBJECTS / Path(source).name
                t = Table.read(source, format="ascii.csv")
                t.write(path, format="csv", overwrite=True)
        else:
            path = convert_to_csv(source)
    return path
    
#
#
def main():
    url = "https://raw.githubusercontent.com/kcpatra45/nickel_starlists/refs/heads/main/nickel_targets_20261102"
    print(convert_to_csv(url))
#
#
if __name__ == "__main__":
    main()
#
#