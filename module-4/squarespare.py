# Visualize equimaterial zones on a rolled cylinder

import numpy as np
import matplotlib.pyplot as plt
r0 = 1.0 # radius of cardboard cylinder in units of r0
R_new = 3.0 * r0 # radius of roll when new, in units of r0

def product_remaining(r, R_new=R_new, r0=r0):
    """Fraction of product remaining by visible roll radius.

    Parameters
    ----------
    r : float, 1 <= r
        Visible radius of roll in units of r0, the cardboard cylinder radius.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0.

    Returns
    -------
    Current remaining length as fraction of original length of new roll.
    """
    x = r/R_new
    f = ((x**2)*(R_new**2) - r**2) / (R_new**2 - r0**2)
    return f 

def product_visible(el_frac, R_new=R_new, r0=r0):
    """Visible roll radius by fraction of remaining product.

    Parameters
    ----------
    el_frac : float, 0 <= el_frac <= 1
        Current remaining length as fraction of original length of new roll.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0, the cardboard cylinder radius.

    Returns
    -------
    Current visible radius of roll, in units of r0, the cardboard cylinder
    radius.
    """
    f = el_frac
    x = (f+((r0)/(R_new))*(1-f))**0.5
    return x

def visualize_danger(n, R_new=R_new, r0=r0, saveas=''):
    """Use n line segments of equal product to visualize paradox of the roll.

    Parameters
    ----------
    n : int scalar
        Number of line segments to display.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0, the cardboard cylinder radius.
    r0 : scalar, optional, default: 1
        Radius of cardboard cylinder, in units of r0.
    saveas : str, optional, default: empty
        If not empty save figure to file 

    Returns
    -------
    None
    """

    # Start with a new figure window
    plt.close('all') # this helps get rid of old figures you forgot to close
    fh = plt.figure(figsize=(8,6)) # my favorite figure size

    ### YOUR CODE HERE ###

    # Do the core plotting commands here
    ## use the functions defined above to calculate the line segments to plot

    # Set axes properties here for a better view
    ## things like axis limits and tick marks

    # Stylize and annotate
    ## things like axes labels, font sizes, or any other finishing touches

    ######################

    # Finally, show on screen and/or save to file
    if saveas:
        plt.savefig(saveas)
    plt.close()   # figures in this course are files: look at the saved PNG (plt.show() would pop a window instead)

if __name__ == '__main__':
    visualize_danger(5, saveas='roll_paradox_5.png')
    visualize_danger(3, saveas='roll_paradox_3.png')
    visualize_danger(9, saveas='roll_paradox_9.png')