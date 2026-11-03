#!/home/natha/miniconda3/envs/twilight-cf/bin/python
import tkinter as tk              # window, labels, and the after() timer
from astropy.time import Time     # Time.now() is passed to the twilight functions
from pathlib import Path          # to find the icon file next to this script
import sys                        # to tell Python where the project scripts are
from tkinter import ttk           # themed widgets, including the dropdown (Combobox)

# twilight.py and utils.py live one folder up (twilight/), not in gui/.
# Adding that folder to Python's search path lets us import them.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from twilight import next_twilight, sites, twilight_types
from utils import time_remaining

# The current choices, looked up in the dictionaries from twilight.py.
# Fixed for now; the dropdowns will change these later.
site = sites["lick"]
angle = twilight_types["astronomical"]

root = tk.Tk()                        # the main window

# Size of everything in Tk. The value is pixels per point: 1.333 is a
# plain 96-dpi screen, times 1.25 for the 125% Windows display scale.
# Must come before the widgets are created. Raise it if still too small.
root.tk.call("tk", "scaling", 1.333 * 1.25)
root.title("Next twilight")           # text in the window's title bar
root.configure(bg="black")            # window background colour

# Window icon. The path is built from this script's own folder, so the
# icon is found no matter which folder you run the script from.
# resolve() follows links, so it also works when run as ~/bin/clock.
icon = tk.PhotoImage(file=Path(__file__).resolve().parent / "pixels_out.png")
root.iconphoto(True, icon)            # True: also use it for any later windows

# The big clock display. DejaVu Sans Mono is monospaced, so every digit
# is the same width and the text doesn't jiggle as the numbers change.
# (It is installed in the twilight-cf env; Courier is not.)
label = tk.Label(root, text="00:00:00", font=("DejaVu Sans Mono", 72),
                 fg="lime", bg="black")
label.pack(padx=20, pady=20)          # place it, with a 20-pixel margin

# Dropdown for choosing the site, filled with the names from `sites`.
# "readonly" means you can pick from the list but not type a new name.
site_box = ttk.Combobox(root, values=list(sites), state="readonly")
site_box.set("lick")                  # show the starting choice
site_box.pack(pady=(0, 20))           # under the clock, 20 px margin below


def tick(target):
    """Show the time left until `target`, then run again in 1 second."""
    global after_id                   # saved so change_site can cancel it
    h, m, s = time_remaining(target, Time.now())
    if (h, m, s) == (0, 0, 0):        # reached it: ask for the next twilight
        target = next_twilight(Time.now(), site, angle)
        h, m, s = time_remaining(target, Time.now())
    label.config(text=f"{h:02d}:{m:02d}:{s:02d}")   # 02d: two digits, zero-padded
    after_id = root.after(1000, tick, target)   # call tick(target) again in 1000 ms


def change_site(event):
    """Runs when a site is picked: switch `site` and restart the countdown."""
    global site                       # assign the file-level site, not a new local one
    site = sites[site_box.get()]
    root.after_cancel(after_id)       # stop the old countdown chain
    tick(next_twilight(Time.now(), site, angle))   # start a new one


site_box.bind("<<ComboboxSelected>>", change_site)   # run change_site on each pick


tick(next_twilight(Time.now(), site, angle))   # first calculation, starts the loop
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
#   Python tkinter.ttk documentation (Combobox):
#     https://docs.python.org/3/library/tkinter.ttk.html
#   Tk ttk::combobox manual (<<ComboboxSelected>> event):
#     https://www.tcl.tk/man/tcl8.6/TkCmd/ttk_combobox.htm
#   Tk bind command (connecting events to functions):
#     https://www.tcl.tk/man/tcl8.6/TkCmd/bind.htm
#   Tk font command (font families and sizes):
#     https://www.tcl.tk/man/tcl8.6/TkCmd/font.htm
#   DejaVu fonts project:
#     https://dejavu-fonts.github.io/
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
#   Astropy Time documentation:
#     https://docs.astropy.org/en/stable/time/
