import tkinter as tk              # window, labels, and the after() timer
from astropy.time import Time     # Time.now() is passed to the twilight functions
from pathlib import Path          # to find the icon file next to this script
import sys                        # to tell Python where the project scripts are
from astropy.coordinates import EarthLocation   # only for the filler location

# twilight.py and utils.py live one folder up (twilight/), not in gui/.
# Adding that folder to Python's search path lets us import them.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from twilight import next_twilight, sites
from utils import time_remaining

# FILLER: Lick is hard-coded until the location selector exists.
# from_geodetic reads plain numbers as degrees and metres.
lick = sites["lick"]
location = EarthLocation.from_geodetic(lick["lon"], lick["lat"], lick["height"])

root = tk.Tk()                        # the main window

# Size of everything in Tk. The value is pixels per point: 1.333 is a
# plain 96-dpi screen, times 1.25 for the 125% Windows display scale.
# Must come before the widgets are created. Raise it if still too small.
root.tk.call("tk", "scaling", 1.333 * 1.25)
root.title("Next twilight")           # text in the window's title bar
root.configure(bg="black")            # window background colour

# Window icon. The path is built from this script's own folder, so the
# icon is found no matter which folder you run the script from.
icon = tk.PhotoImage(file=Path(__file__).parent / "pixels_out.png")
root.iconphoto(True, icon)            # True: also use it for any later windows

# The big clock display. Courier is monospaced, so every digit is the
# same width and the text doesn't jiggle as the numbers change.
label = tk.Label(root, text="00:00:00", font=("Courier", 72),
                 fg="lime", bg="black")
label.pack(padx=20, pady=20)          # place it, with a 20-pixel margin


def tick(target):
    """Show the time left until `target`, then run again in 1 second."""
    h, m, s = time_remaining(target, Time.now())
    if (h, m, s) == (0, 0, 0):        # reached it: ask for the next twilight
        target = next_twilight(Time.now(), location)
        h, m, s = time_remaining(target, Time.now())
    label.config(text=f"{h:02d}:{m:02d}:{s:02d}")   # 02d: two digits, zero-padded
    root.after(1000, tick, target)    # call tick(target) again in 1000 ms


tick(next_twilight(Time.now(), location))   # first calculation, starts the loop
root.mainloop()                       # keep the window open until closed


# ---------------------------------------------------------------------
# Written by Claude (Anthropic AI assistant, Claude Code) at Nathaniel's
# direction, as part of a personal twilight-clock project.
#
# References:
#   Python tkinter documentation:
#     https://docs.python.org/3/library/tkinter.html
#   TkDocs tutorial (Mark Roseman):
#     https://tkdocs.com/tutorial/
#   Tcl/Tk 8.6 reference manual (what tkinter calls underneath):
#     https://www.tcl.tk/man/tcl8.6/
#   Tk tk command (tk scaling, pixels per point):
#     https://www.tcl.tk/man/tcl8.6/TkCmd/tk.htm
#   Tk photo image command (tk.PhotoImage, PNG support):
#     https://www.tcl.tk/man/tcl8.6/TkCmd/photo.htm
#   Tk wm iconphoto command (root.iconphoto):
#     https://www.tcl.tk/man/tcl8.6/TkCmd/wm.htm
#   Python pathlib documentation (Path, __file__ folder):
#     https://docs.python.org/3/library/pathlib.html
#   Python sys.path documentation (module search path):
#     https://docs.python.org/3/library/sys.html#sys.path
#   Python format specification mini-language (the :02d in f-strings):
#     https://docs.python.org/3/library/string.html#formatspec
#   Tcl after command (what root.after calls underneath):
#     https://www.tcl.tk/man/tcl8.6/TclCmd/after.htm
#   Astropy EarthLocation documentation (from_geodetic):
#     https://docs.astropy.org/en/stable/api/astropy.coordinates.EarthLocation.html
#   Astropy Time documentation:
#     https://docs.astropy.org/en/stable/time/
