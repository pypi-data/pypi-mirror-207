import numpy as np

def init_3f(init_state):
    # init_3f - generates the initial state vector for the 3F model

    # Syntax:
    #     x0 = init_3f(init_state)
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

    #x1 = x-position in a global coordinate system
    #x2 = y-position in a global coordinate system
    #x3 = orientation of vessel
    #x4 = body-fixed velocity aligned with orientation
    #x5 = body-fixed velocity lateral to orientation
    #x6 = yaw


    #u1 = body-fixed force aligned with orientation
    #u2 = body-fixed force lateral to orientation
    #u3 = body-fixed yaw moment

    # obtain initial states from vector
    sx0 = init_state[0]
    sy0 = init_state[1]
    Psi0 = init_state[2]
    velx0 = init_state[3]
    vely0 = 0.0
    yaw0 = init_state[4]

    # sprung mass states
    x0 = []  # init initial state vector
    x0.append(sx0)  # x-position in a global coordinate system
    x0.append(sy0)  # y-position in a global coordinate system
    x0.append(Psi0)  # orientation of vessel
    x0.append(velx0)  # body-fixed velocity aligned with orientation
    x0.append(vely0)  # body-fixed velocity lateral to orientation
    x0.append(yaw0)  # yaw

    return x0

    # ------------- END OF CODE --------------
