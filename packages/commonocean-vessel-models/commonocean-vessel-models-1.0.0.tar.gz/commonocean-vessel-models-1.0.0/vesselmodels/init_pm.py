import numpy as np

def init_pm(init_state):
    # init_pm - generates the initial state vector for the point mass model

    # Syntax:
    #     x0 = init_pm(init_state)
    #
    # Inputs:
    #     init_state - core initial states
    #
    # Outputs:
    #     x0 - initial state vector
    #
    # Example:
    #
    # See also: ---

    # Author:       Hanna Krasowski
    # Written:      26-August-2022
    # Last update:  ---
    # Last revision:---

    # ------------- BEGIN CODE --------------

    #states
    #x1 = x-position in a global coordinate system
    #x2 = y-position in a global coordinate system
    #x3 = velocity in x-direction
    #x4 = velocity in y-direction

    #u1 = acceleration in x-direction
    #u2 = acceleration in y-direction

    # obtain initial states from vector
    sx0 = init_state[0]
    sy0 = init_state[1]
    velx0 = init_state[2] * np.cos(init_state[3])
    vely0 = init_state[2] * np.sin(init_state[3])

    # sprung mass states
    x0 = []  # init initial state vector
    x0.append(sx0)  # x-position in a global coordinate system
    x0.append(sy0)  # y-position in a global coordinate system
    x0.append(velx0)  # velocity in x-direction
    x0.append(vely0)  # velocity in y-direction

    return x0

    # ------------- END OF CODE --------------
