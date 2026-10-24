# pixels_starter.py -- an image is an array (Pod 5). Copy this file to pixels.py and work on the copy.
# Run from the repository folder:  python module-3/pixels.py
import numpy as np
from matplotlib.pyplot import imread, imsave
import numpy as np

I = imread("clean_io_small.png")
     # rows, columns, 3 colour channels; values 0.0 to 1.0
J = I.copy()
x = (5+356)
y = (5+349)


def circle(r, pos_x, pos_y):
    for x in range(pos_x-r, pos_x+r+1):
        for y in range(pos_y-r, pos_y+r+1):
            if (x-pos_x)**2+(y-pos_y)**2<r**2:
                J[x, y, :] = 0
circle(50, 356, 450)
circle(50, 356, 250)


    


imsave("pixels_out.png", J)
if __name__ == "__main__":
    print("shape:", I.shape[1])
    print("size", I.size)
    print(I[356, 349, 0])
    print(I[0, 0])
    print(I[356,349])

J = 1 - J
