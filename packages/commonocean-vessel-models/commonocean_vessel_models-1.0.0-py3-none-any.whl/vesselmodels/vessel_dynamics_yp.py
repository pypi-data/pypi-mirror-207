import numpy as np
from vesselmodels.utils.input_constraints import acceleration_constraints, yaw_constraints

__author__ = "Hanna Krasowski"
__copyright__ = "TUM Cyber-Physical Systems Group"
__version__ = "2022a"
__maintainer__ = "Hanna Krasowski"
__email__ = "commonocean@lists.lrz.de"
__status__ = "Released"


def vessel_dynamics_yp(x, uInit, p):
    """
    yp - yaw-constrained point mass dynamics
    reference point: center of mass

    Syntax:
        f = vesselDynamics_yp(x,u,p)

    Inputs:
        :param x: vessel state vector
        :param uInit: vessel input vector
        :param p: vessel parameter vector

    Outputs:
        :return f: right-hand side of differential equations
    """

    #states
    #x1 = x-position in a global coordinate system
    #x2 = y-position in a global coordinate system
    #x3 = orientation of vessel
    #x4 = velocity aligned with orientation

    #u1 = acceleration aligned with orientation
    #u2 = yaw aligned with orientation

    #consider acceleration constraints
    u = []
    u.append(acceleration_constraints(uInit[0], p))
    u.append(yaw_constraints(uInit[1], p))

    # system dynamics
    f = [np.cos(x[2]) *x[3],
        np.sin(x[2]) *x[3],
        u[1],
        u[0]]

    return f
