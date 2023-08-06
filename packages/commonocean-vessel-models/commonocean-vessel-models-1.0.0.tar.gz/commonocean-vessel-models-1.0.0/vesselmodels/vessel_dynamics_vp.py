import math
from vesselmodels.utils.input_constraints import acceleration_constraints, velocity_constraints

__author__ = "Hanna Krasowski"
__copyright__ = "TUM Cyber-Physical Systems Group"
__version__ = "2022a"
__maintainer__ = "Hanna Krasowski"
__email__ = "commonocean@lists.lrz.de"
__status__ = "Released"


def vessel_dynamics_vp(x, uInit, p, dt):
    """
    vesselDynamics_vp - velocity-constrained point mass dynamics
    reference point: center of mass

    Syntax:
        f = vesselDynamics_vp(x,u,p,dt)

    Inputs:
        :param x: vessel state vector
        :param uInit: vessel input vector
        :param p: vessel parameter vector
        :param dt: time step size

    Outputs:
        :return f: right-hand side of differential equations
    """

    #states
    #x1 = x-position in a global coordinate system
    #x2 = y-position in a global coordinate system
    #x3 = velocity in x-direction
    #x4 = velocity in y-direction

    #u1 = acceleration in x-direction
    #u2 = acceleration in y-direction

    #consider acceleration constraints
    u = acceleration_constraints(uInit, p)

    #consider veclocity constraints
    u = velocity_constraints(x[2:], u, p, dt)

    # system dynamics
    f = [x[2],
        x[3],
        u[0],
        u[1]]

    return f
