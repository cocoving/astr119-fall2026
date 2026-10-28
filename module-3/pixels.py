import numpy as np
from matplotlib.pyplot import imread, imsave, imshow
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
    try:
        I = b_w(I)
    except:IndexError
    J = np.zeros_like(I)
    K = I.copy()
    L = np.zeros_like(I)
    I[1:, :] += K[:-1, :]
    I[:-1, :] += K[1:, :]
    I[:, 1:] += K[:, :-1]
    I[:, :-1] += K[:, 1:]
    L[:, :] = (I[:, :]-(5*K[:, :]))
    v = 1*np.std(L)
    sigma = 5*np.std(L)
    for i in range(1, I.shape[0]-1):
        for j in range(1, I.shape[1]-1):
            total = 0
            count = 0
            if abs(L[i, j] - L[i-1, j]) > v and L[i, j]*L[i-1, j] < 0:               
                total += abs(L[i, j] - L[i-1, j]); count += 1
            if abs(L[i, j] - L[i+1, j]) > v and L[i, j]*L[i+1, j] < 0:
                total += abs(L[i, j] - L[i+1, j]); count += 1
            if abs(L[i, j] - L[i, j-1]) > v and L[i, j]*L[i, j-1] < 0:
                total += abs(L[i, j] - L[i, j-1]); count += 1
            if abs(L[i, j] - L[i, j+1]) > v and L[i, j]*L[i, j+1] < 0:
                total += abs(L[i, j] - L[i, j+1]); count += 1
            if count > 0:
                x = total = total/count 
                L[i, j] = 1-np.exp((-(x)**2)/(2*(sigma)**2))
            else:
                L[i, j] = 0
    
    return L

def edges_grad_vII(I):
    try:
        I = b_w(I)
    except:IndexError
    J = np.zeros_like(I)
    K = I.copy()
    L = np.zeros_like(I)
    I[1:, :] += K[:-1, :]
    I[:-1, :] += K[1:, :]
    I[:, 1:] += K[:, :-1]
    I[:, :-1] += K[:, 1:]
    L[:, :] = (I[:, :]-(5*K[:, :]))
    v = 1*np.std(L)
    sigma = 5*np.std(L)
    total = np.zeros_like(L); count = np.zeros_like(L)
    mask = ((abs(L[1:, :] - L[:-1, :]) > v)) & (L[1:, :]*L[:-1, :] < 0)
    total[1:, :] += abs(L[1:, :] - L[:-1, :])*mask; count[1:, :] += mask
    mask = ((abs(L[:-1, :] - L[1:, :]) > v)) & (L[:-1, :]*L[1:, :] < 0)
    total[:-1, :] += abs(L[:-1, :] - L[1:, :])*mask; count[:-1, :] += mask
    mask = ((abs(L[:, 1:] - L[:, :-1]) > v)) & (L[:, 1:]*L[:, :-1] < 0)
    total[:, 1:] += abs(L[:, 1:] - L[:, :-1])*mask; count[:, 1:] += mask
    mask = ((abs(L[:, :-1] - L[:, 1:]) > v)) & (L[:, :-1]*L[:, 1:] < 0)
    total[:, :-1] += abs(L[:, :-1] - L[:, 1:])*mask; count[:, :-1] += mask
    x = np.where(count > 0,total/np.maximum(count, 1),0) 
    L[:, :] = 1-np.exp((-(x)**2)/(2*(sigma)**2))
    return L

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

def color_swap(I):
    J = I.copy()
    I[:, :, 0] = J[:, :, 2]
    I[:, :, 1] = J[:, :, 0]
    I[:, :, 2] = J[:, :, 1]
    return I

folder = Path(__file__).parent
pics = sorted(folder.glob("*.png"))
edits = {"eyes": eyes, "nothing": null, "inverted": inverted, "blur": blur, "edges":edges, "edges2": edges_grad, "Black & White":b_w, "Edges V-II":edges_grad_vII, "Color":color_swap}
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
                imshow(I)
                imsave("pixels_out.png", I, cmap="grey")
                print(f"Wrote {image_file}")


if __name__ == '__main__':
    _main()