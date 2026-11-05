#------------------------------------------------------------------------------
# Solve and animate the double compound pendulum
# Run:
# python pendpend.py <teta1> <teta2>
#------------------------------------------------------------------------------
import sys
import numpy as np
import matplotlib.pyplot as plt
import celluloid

### Physical parameters used throughout
earth_g = 9.8 # m/s^2 (acceleration due to gravity)
pend_el = 0.25 # m (pendulum arm length)

### Pendulum ODE ###
def single_pendulum_ode():
    """You decide how to implement this."""
    return 0

def double_pendulum_ode():
    """You decide how to implement this."""
    return 0

### ODE solver(s)
# USE AN ODE SOLVER FROM CLASS OR FROM SCIPY

### Tests/examples ###
def solve_simple_pendulum(teta0):
    """YOU DECIDE ON THE DETAILS. THIS FUNCTION SHOULD RETURN THREE ARRAYS:
    TIME, ANGLE, ANGLE-RATE-OF-CHAGE
    """
    # placeholders for starter code:
    t = np.arange(0,100)
    teta = np.zeros(t.size)
    tetadot = np.zeros(t.size)
    return (t, teta, tetadot)

def solve_double_pendulum(teta10,teta20):
    """YOU DECIDE ON THE DETAILS. THIS FUNCTION SHOULD RETURN THREE ARRAYS:
    TIME, ANGLES, ANGLE-RATE-OF-CHAGE
    """
    # placeholders for starter code:
    t = np.arange(0,100)
    teta = np.zeros((t.size,2))
    tetadot = np.zeros((t.size,2))
    return (t, teta, tetadot)

def plot_simple_pendulum(t, teta, tetadot, name=''):
    # Plot the solutions
    plt.figure(figsize=(16,6))
    plt.subplot(1,2,1)
    plt.plot(t, teta, label=name)
    plt.xlabel("$t$ [sec]", fontsize=14)
    plt.ylabel(r"$\theta$", fontsize=14)
    if name:
        plt.legend(fontsize=12)

    # And energy conservation
    plt.subplot(1,2,2)
    K = 0.5*(pend_el*tetadot)**2
    U = earth_g*(pend_el - pend_el*np.cos(teta))
    E = K + U
    plt.plot(t, np.abs((E - E[0])/(E[0]+1e-10)), label=name)
    plt.xlabel("$t$ [sec]", fontsize=14)
    plt.ylabel("Mechanical energy $|E - E(t=0)|/E(t=0)$", fontsize=14)
    if name:
        plt.legend()
    plt.show()
    return

def animate_simple_pendulum(t, teta, fps_mul=1.0):
    dt = t[1] - t[0]
    el = pend_el
    x = el*np.sin(teta.squeeze())
    y = -el*np.cos(teta.squeeze())

    fig = plt.figure(figsize=(8,6))
    plt.xlim((-1.1*el, 1.1*el))
    plt.axis('equal')
    cam = celluloid.Camera(fig)
    for k in range(t.size):
        plt.plot([0,x[k]],[0,y[k]],'k-',linewidth=4)
        plt.plot(x[k],y[k],'o', markersize=14,color='r')
        cam.snap()
    anim = cam.animate(interval=dt*fps_mul,repeat=False)
    plt.show()
    return anim

def plot_double_pendulum(t, teta, tetadot, name=''):
    tet1 = teta[:,0] % 2*np.pi
    tet2 = teta[:,1] % 2*np.pi
    phi = tet1 - tet2
    t1dot = tetadot[:,0]
    t2dot = tetadot[:,1]
    T = (1/6)*pend_el**2*(
        4*t1dot**2 + t2dot**2 + 3*np.cos(phi)*t1dot*t2dot)
    V = -(1/2)*earth_g*pend_el*(
        3*np.cos(tet1) + np.cos(tet2))
    E = T + V

    # Plot the solutions
    plt.figure(figsize=(16,6))
    plt.subplot(1,2,1)
    plt.plot(t, tet1, label=r'$\theta_1$')
    plt.plot(t, tet2, label=r'$\theta_2$')
    plt.xlabel("$t$ [sec]", fontsize=14)
    plt.ylabel(r"$\theta$", fontsize=14)
    plt.legend(fontsize=12)

    # And energy conservation
    plt.subplot(1,2,2)
    plt.plot(t, np.abs((E - E[0])/E[0]))
    plt.xlabel("$t$ [sec]", fontsize=14)
    plt.ylabel("Mechanical energy $|E - E(t=0)|/E(t=0)$", fontsize=14)

    plt.show()
    return

def animate_double_pendulum(t, teta, fps_mul=1.0):
    """Animate the solution (found by solve_double_pendulum())."""
    tet1 = teta[:,0]
    tet2 = teta[:,1]
    dt = t[1] - t[0]
    el = pend_el
    x1 = el*np.sin(tet1)
    y1 = -el*np.cos(tet1)
    x2 = x1 + el*np.sin(tet2)
    y2 = y1 - el*np.cos(tet2)

    fig = plt.figure(figsize=(8,6))
    plt.xlim((-2.1*el, 2.1*el))
    plt.axis('equal')
    cam = celluloid.Camera(fig)
    for k in range(t.size):
        plt.plot([0,x1[k]],[0,y1[k]],'b-',linewidth=4)
        plt.plot([x1[k],x2[k]],[y1[k],y2[k]],'r-',linewidth=4)
        cam.snap()
    anim = cam.animate(interval=dt*fps_mul,repeat=False)
    plt.show()
    return anim

if __name__ == '__main__':
    t, teta, tetadot = solve_double_pendulum(sys.argv[1], sys.argv[2])
    animate_double_pendulum(t,teta)
