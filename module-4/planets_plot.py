# planets_plot_starter.py -- the ten planets as arrays, ready to plot (Pod 6). Copy this file to planets_plot.py and work on the copy.
# Run from the repository folder:  python module-4/planets_plot.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
import sys

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

SIGMA = 5.67e-8          # Stefan-Boltzmann constant, W m^-2 K^-4
L_SUN = 3.8e26           # solar luminosity, W
AU = 1.496e11            # meters per AU

name = np.array(["Earth", "Mars", "HD 209458 b", "51 Peg b", "TRAPPIST-1 e",
                 "Kepler-22 b", "55 Cnc e", "HD 189733 b", "Kepler-452 b", "Proxima b"])
lum = np.array([1.0, 1.0, 1.6, 1.3, 0.00055, 0.79, 0.58, 0.34, 1.2, 0.0016])        # star luminosity, solar units
dist = np.array([1.000, 1.524, 0.047, 0.052, 0.029, 0.85, 0.0154, 0.031, 1.046, 0.0485])   # distance, AU

def t_eq(L, d):
    """Equilibrium temperature (K) at distance d (m) from a star of luminosity L (W)."""
    return (L / (16 * np.pi * SIGMA * d**2)) ** 0.25

def three_d_graph():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    # Make data.
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap="coolwarm",
                        linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.02f}')

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

def scatter():
    T = t_eq(lum * L_SUN, dist * AU)
    d = np.linspace(0.01, 2.0, 200)
    T_curve = t_eq(L_SUN, d * AU)
    fig, ax = plt.subplots()
    ax.set_ylabel("Eq Temp(K)")
    ax.set_xlabel("D(AU)")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.scatter(dist, T)
    ax.plot(d, T_curve)
    for n, x, y in zip(name, dist, T): ax.annotate(n, (x, y), fontsize=7)
    return fig

graphs = {"2D Scatter":scatter, "3D Graph":three_d_graph}
names = list(graphs)

def _main():
    try:
        graph = sys.argv[2]
    except IndexError:
        while True:
            for i, name in enumerate(graphs.items()):
                print(i+1, name)
            choice = get_int_input("Enter a number: ")
            if choice == 0:
                break
            else:
                choice -= 1
                graph = graphs[names[choice]]
                fig = graph()
                fig.savefig("module-4/planets.png", dpi=150)
                print("wrote module-4/planets.png")

if __name__ == "__main__":
    _main()