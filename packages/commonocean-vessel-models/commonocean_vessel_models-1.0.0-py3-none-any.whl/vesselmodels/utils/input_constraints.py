import numpy as np

__author__ = "Hanna Krasowski"
__copyright__ = "TUM Cyber-Physical Systems Group"
__version__ = "2022a"
__maintainer__ = "Hanna Krasowski"
__email__ = "commonocean@lists.lrz.de"
__status__ = "Released"

def yaw_constraints(yaw, p):
    y = yaw
    # yaw limit reached?
    if y <= -p.w_max:
        yaw = - p.w_max
    elif y >= p.w_max:
        yaw = p.w_max

    return yaw

def acceleration_constraints(acceleration, p):
    
    a = np.linalg.norm(acceleration)

    # acceleration limit reached?
    if a >= p.a_max:
        acceleration = (acceleration/a) * p.a_max

    return acceleration

def velocity_constraints(velocity_prev, acceleration, p, dt):

    # Velocity at next time step
    velocity = velocity_prev + (acceleration*dt)
    v = np.linalg.norm(velocity)

    if v >= p.v_max:
        velocity_new = (velocity/v) * p.v_max
        # correction of acceleration inputs
        acc_limits = (velocity_new - velocity_prev) / dt
        for idx, limit in enumerate(acc_limits):
            if velocity_new[idx] < 0.0:
                acceleration[idx] = np.clip(acceleration[idx], limit, p.a_max)
            else:
                acceleration[idx] = np.clip(acceleration[idx], -p.a_max, limit)
        return acceleration
    else:
        return acceleration

def general_bounded_constraint(u,limit):

    if u <= - limit:
        u = - limit
    elif u >= limit:
        u = limit

    return u


