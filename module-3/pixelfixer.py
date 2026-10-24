#------------------------------------------------------------------------------
# pixelfixer.py: a command-line utility that fixes red-corrupted pixels in an
# RGB image.
#
# Run with:
#   python pixelfixer.py easy_corrupt_io_small.png
# which writes fixed_easy_corrupt_io_small.png next to the input.
#------------------------------------------------------------------------------
import sys
import numpy as np
from matplotlib.pyplot import imread, imsave
from pathlib import Path

folder = Path(__file__).parent
pics = sorted(folder.glob("*.png"))

def pixelfix(I):
    """Replace bad pixels with the color averaged from their neighbors.

    Parameters
    ----------
    I : ndarray, shape (M, N, 3)
        A color image array in RGB format, values between 0 and 1.
        A bad pixel has red = 1, green = 0, blue = 0.

    Returns
    -------
    Iq : ndarray, same shape as I
        A copy of the image with the bad pixels fixed.
    """
    Iq = I.copy()
    k = 0
    for i in range(0, I.shape[0]):
        for j in range(0, I.shape[1]):
            if Iq[i, j, 0] == 1 and Iq[i, j, 1] == 0 and Iq[i, j, 2] == 0:
                Iq[i, j] = 1
                k += 1
                count, total = 0, 0
                if i - 1 >= 0 and Iq[i-1, j, 0] < 1:
                    count += 1; total += Iq[i-1, j]
                if i + 1 < Iq.shape[0] and Iq[i+1, j, 0] < 1:
                    count += 1; total += Iq[i+1, j]
                if j - 1 >= 0 and Iq[i, j-1, 0] < 1:
                    count += 1; total += Iq[i, j-1]
                if j + 1 < Iq.shape[1] and Iq[i, j+1, 0] < 1:
                    count += 1; total += Iq[i, j+1]
                Iq[i,j]=((total)/(count))           
    print(f"{k} Bad Pixels Found")
    return Iq

def _main():
    try:
        image_file = sys.argv[1]
    except IndexError:
        for i, name in enumerate(pics):
            print(i, name.name)
        choice = input("Enter a number: ")
        image_file = pics[int(choice)].name

    I = imread(image_file)
    I = pixelfix(I)
    imsave('fixed_' + image_file, I)
    print(f"Wrote fixed_{image_file}")


if __name__ == '__main__':
    _main()
