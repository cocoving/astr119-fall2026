# pixels_starter.py -- an image is an array (Pod 5). Copy this file to pixels.py and work on the copy.
# Run from the repository folder:  python module-3/pixels.py
import numpy as np
from matplotlib.pyplot import imread, imsave
import sys
from pathlib import Path

def circle(r, pos_x, pos_y, I):
    for x in range(pos_x-r, pos_x+r+1):
        for y in range(pos_y-r, pos_y+r+1):
            if (x-pos_x)**2+(y-pos_y)**2<r**2:
                I[x, y, :] = 0

def eyes(I):
    J = I
    circle(50, 356, 450, I)
    circle(50, 356, 250, I)


    



folder = Path(__file__).parent
pics = sorted(folder.glob("*.png"))
def _main():
    try:
        image_file = sys.argv[1]
    except IndexError:
        for i, name in enumerate(pics):
            print(i, name.name)
        choice = input("Enter a number: ")
        image_file = pics[int(choice)].name

    I = imread(image_file)
    I = eyes(I)
    imsave("pixels_out.png", I)
    print(f"Wrote fixed_{image_file}")


if __name__ == '__main__':
    _main()