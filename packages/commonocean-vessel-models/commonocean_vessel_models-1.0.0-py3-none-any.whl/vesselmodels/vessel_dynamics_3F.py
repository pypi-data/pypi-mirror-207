import numpy as np
from vesselmodels.utils.input_constraints import general_bounded_constraint

__author__ = "Hanna Krasowski"
__copyright__ = "TUM Cyber-Physical Systems Group"
__version__ = "2022a"
__maintainer__ = "Hanna Krasowski"
__email__ = "commonocean@lists.lrz.de"
__status__ = "Released"


def vessel_dynamics_3f(x, uInit, p):
    """
    3f - three degrees of freedom dynamics
    reference point: center of mass

    Syntax:
        f = vesselDynamics_3f(x,u,p)

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
    #x4 = body-fixed velocity aligned with orientation
    #x5 = body-fixed velocity lateral to orientation
    #x6 = yaw


    #u1 = body-fixed force aligned with orientation
    #u2 = body-fixed force lateral to orientation
    #u3 = body-fixed yaw moment

    #consider acceleration constraints
    u = []
    u.append(general_bounded_constraint(uInit[0], p.surge_force_max))
    u.append(general_bounded_constraint(uInit[1], p.sway_force_max))
    u.append(general_bounded_constraint(uInit[2], p.yaw_moment_max))

    # right hand side of mass-spring-damper system

    M = np.array([[p.m,0,0 ], [0, p.m, p.m*p.x_g], [0, p.m*p.x_g, p.I_z]]) + \
        np.array([[-p.X_udot, 0, 0], [0, - p.Y_vdot, - p.Y_rdot], [0, - p.Y_rdot, - p.N_rdot]])
    D = np.array([[-p.X_u, 0, 0], [0, - p.Y_v, - p.Y_r], [0, - p.N_v, - p.N_r]])
    C = np.array([[0,0,-p.m*(x[4]+p.x_g*x[5])], [0, 0, p.m*x[5]], [p.m*(x[4]+p.x_g*x[5]), -p.m*x[5], 0]]) + \
        np.array([[0, 0, p.Y_rdot*x[5] + p.Y_vdot*x[4]], [0, 0, -p.X_udot*x[3]], [- p.Y_rdot*x[5] - p.Y_vdot*x[4], p.X_udot*x[3], 0]])
    velocities = np.squeeze(np.asarray(x[3:]))
    x_acclerations = np.dot(np.linalg.inv(M), (- np.dot(C,velocities) - np.dot(D,velocities) + np.asarray(u)))


    
    # system dynamics
    f = [np.cos(x[2]) *x[3] - np.sin(x[2]) *x[4],
        np.sin(x[2]) *x[3] + np.cos(x[2]) *x[4],
        x[5],
        x_acclerations[0],
        x_acclerations[1],
        x_acclerations[2]]

    return f
