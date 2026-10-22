# pixels_starter.py -- an image is an array (Pod 5). Copy this file to pixels.py and work on the copy.
# Run from the repository folder:  python module-3/pixels.py
import numpy as np
from matplotlib.pyplot import imread, imsave

I = imread("module-3/clean_io_small.png")
     # rows, columns, 3 colour channels; values 0.0 to 1.0
J = I.copy()
J[20:40, 20:40, :] = 1
J[356, :, :] = 0
imsave("module-3/pixels_out.png", J)
if __name__ == "__main__":
    print("shape:", I.shape)
    print("size", I.size)
    print(I[0, 0])
    print(I[356,349])
