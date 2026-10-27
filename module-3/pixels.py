import numpy as np
from matplotlib.pyplot import imread, imsave
import sys
from pathlib import Path

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def circle(r, pos_x, pos_y, I):
    for x in range(pos_x-r, pos_x+r+1):
        for y in range(pos_y-r, pos_y+r+1):
            if (x-pos_x)**2+(y-pos_y)**2<r**2:
                I[x, y, :] = 0

def eyes(I):
    circle(50, 356, 450, I)
    circle(50, 356, 250, I)
    return I

def edges(I):
    v = .9
    J = np.ones_like(I)
    K = I.copy()
    for i in range(1, I.shape[0]-1):
        for j in range(1, I.shape[1]-1):
            if abs(any(I[i, j, :] - K[i-1, j, :])) > v:               
                J[i, j, :] = 0
            if abs(any(I[i, j, :] - K[i+1, j, :])) > v:
                J[i, j, :] = 0
            if abs(any(I[i, j, :] - K[i, j-1, :])) > v:
                J[i, j, :] = 0
            if abs(any(I[i, j, :] - K[i, j+1, :])) > v:
                J[i, j, :] = 0
    return J

def edges_grad(I):
    v = .9
    J = np.ones_like(I)
    K = I.copy()
    for i in range(1, I.shape[0]-1):
        for j in range(1, I.shape[1]-1):
            total = 0
            if any(I[i, j, :] - K[i-1, j, :]) > v:               
                total += abs(any(I[i, j, :] - K[i-1, j, :]))
            if any(I[i, j, :] - K[i+1, j, :]) > v:
                total += abs(any(I[i, j, :] - K[i-1, j, :]))
            if any(I[i, j, :] - K[i, j-1, :]) > v:
                total += abs(any(I[i, j, :] - K[i-1, j, :]))
            if any(I[i, j, :] - K[i, j+1, :]) > v:
                total += abs(any(I[i, j, :] - K[i-1, j, :]))
            total /= 4
            J[i, j] = total
    J /= J.max()
    return J

def b_w(I):
    I = (I[:, :, 0]*(0.299) + I[:, :, 1]*(0.587) + I[:, :, 2]*(0.114))
    return I

def null(I):
    return I

def inverted(I):
    I = 1-I
    return I


def blur(I):
    for n in range(100):
        J = I.copy()
        I[1:, :, :] += J[:-1, :, :]
        I[:-1, :, :] += J[1:, :, :]
        I[:, 1:, :] += J[:, :-1, :]
        I[:, :-1, :] += J[:, 1:, :]
        I /= 5
    return I

folder = Path(__file__).parent
pics = sorted(folder.glob("*.png"))
edits = {"eyes": eyes, "nothing": null, "inverted": inverted, "blur": blur, "edges":edges, "edges2": edges_grad, "Black & White":b_w}
names = list(edits)

def _main():
    try:
        image_file = sys.argv[1]
    except IndexError:
        for i, name in enumerate(pics):
            print(i, name.name)
        choice = get_int_input("Enter a number: ")
        image_file = pics[int(choice)].name

    I = imread(image_file)

    try:
        edit = sys.argv[2]
        I = edit(I)
        imsave("pixels_out.png", I)
        print(f"Wrote {image_file}")
    except IndexError:
        while True:
            print(f"{0}, Exit")
            for i, name in enumerate(edits.items()):
                print(i+1, name)
            choice = get_int_input("Enter a number: ")
            if choice == 0:
                break
            else:
                choice -= 1
                edit = edits[names[choice]]
                I = edit(I)
                    
                imsave("pixels_out.png", I, cmap="grey")
                print(f"Wrote {image_file}")


if __name__ == '__main__':
    _main()