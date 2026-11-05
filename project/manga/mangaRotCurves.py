r'''
mangaRotCurves.py is a collection of python classes and functions 
useful for generating and fitting rotation curve models with MaNGA data.

These routines support the ASTR-119 MaNGA Rotation Curves Final Project.

HISTORY: They were adapted from material developed by K. Westfall and F. Belfiore by 
Kevin Bundy in March 2023.

'''

import astropy
import numpy as np


class velocity_field:
    def __init__(self, x, y, v, ve):
        self.x = x # The on-sky X coordinates (just pixels for now)
        self.y = y # On-sky Y
        self.v = v # Velocity measurements
        self.ve = ve # Velocity errors
        # Names of the parameters required by the model
        self.par_name = ['x0', 'y0', # Pointing of the IFU relative to the galaxy center
                         'PA', # Disk position angle
                         'inclination', # Disk inclination
                         'Asymptotic rotation', # Asymptotic rotation speed
                         'Rotation scale', # Rotation scale
                         'Bulk velocity'] # Bulk motion of the galaxy away from us
        self.npar = len(self.par_name)
        self.par = np.zeros(self.npar, dtype=float)
        self.fixed = np.zeros(self.npar, dtype=bool)


    def fix_par(self, par, fixed):
        if len(par) != self.npar:
            raise ValueError('Must provide {0} parameters'.format(self.npar))
        if len(fixed) != self.npar:
            raise ValueError('Must provide {0} fix flags'.format(self.npar))
        self.fixed = fixed
        if np.sum(self.fixed) > 0:
            self.par[self.fixed] = par[self.fixed]
            
    def free_par(self):
        self.fixed[:] = False
    
    def fill_par(self, iter_par):
        self.par[np.invert(self.fixed)] = iter_par

    def polar_coordinates(self, geometry_par):
        """
        Given the first 4 parameters (x0, y0, PA, inclination), this function
        calculates the polar coordinates of each velocity measurement with
        respect to the galaxy center.
        """
        xs = self.x + geometry_par[0]
        ys = self.y + geometry_par[1]
        phi0 = np.radians(geometry_par[2])
        inc = np.radians(geometry_par[3])
        xd = xs*np.sin(phi0) + ys*np.cos(phi0)
        yd = (ys*np.sin(phi0) - xs*np.cos(phi0))/np.cos(inc)
        r = np.sqrt(np.square(xd) + np.square(yd))
        theta = np.degrees(np.arctan2(-yd, xd))
        return r, theta
    
    def rotation_curve(self, r, rc_par):
        """
        Given the two rotation curve parameters, this computes
        the rotation velocity a the provided radii.
        """
        return rc_par[0] * np.ma.tanh(r/rc_par[1]).filled(0.0)

    def sample(self, iter_par, full=False):
        """
        Given the full set of parameters, this samples the full
        two-dimensional model. 
        """
        if not full:
            self.fill_par(iter_par)
        r, theta = self.polar_coordinates(self.par[:4])
        vlos = self.rotation_curve(r, self.par[4:6]) \
                    * np.cos(np.radians(theta)) \
                    * np.sin(np.radians(self.par[3])) \
                    + self.par[6]
        return vlos
    
    def chi(self, iter_par, full=False):
        """
        This is the function used by scipy.optimize.least_squares
        to determine the best fitting model.  It returns the
        residuals of the data with respect to the model, normalized
        by the errors.  scipy.optimize.least_squares constructs the
        merit function for the fit internally, which in our use
        below is equivalent to chi-square. 
        """
        return ((self.v-self.sample(iter_par, full=full))/self.ve).ravel()



