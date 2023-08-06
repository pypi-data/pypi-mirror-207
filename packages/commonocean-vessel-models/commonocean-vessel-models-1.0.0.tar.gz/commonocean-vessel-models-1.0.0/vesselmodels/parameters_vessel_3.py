from vehiclemodels.utils import unitConversion
from vesselmodels.vessel_parameters import VesselParameters


def parameters_vessel_3():
    # parameters_vessel3 - CyberShip II
    # CyberShip II (CS2) is a 1:70 scale replica of a supply ship.
    # Syntax:
    #    p = parameters_vessel_3()
    #
    # Inputs:
    #    ---
    #
    # Outputs:
    #    p - parameter vector
    #
    # Example:
    #
    # Subfunctions: none
    #
    # Sources:
    # -   Skjetne, Roger & Smogeli, Oyvind & Fossen, Thor. (2004).
    #     Modeling, Identification, and Adaptive Maneuvering of
    #     CyberShip II: A complete design with experiments.
    # -   M. Wondergem, E. Lefeber, K. Y. Pettersen and H. Nijmeijer,
    #     "Output Feedback Tracking of Ships," in IEEE Transactions on Control Systems Technology,
    #     vol. 19, no. 2, pp. 442-448, March 2011, doi: 10.1109/TCST.2010.2045654

    # Author:       Hanna Krasowski
    # Written:      2022-08-22

    # Last revision:---

    # ------------- BEGIN CODE --------------

    # init vehicle parameters
    p = VesselParameters()

    # vehicle body dimensions
    p.l = 1.255  # length [m]
    p.w = 0.29  # width [m]
    p.d = 0.11  # estimated draft [m]

    # velocity and acceleration parameters
    p.v_max = 1  # maximum velocity [m/s]
    p.a_max = 0.084  # maximum acceleration [m/s^2] - estimated with mass and surge force
    p.w_max = 0.5  # maximum yaw [rad/s] - estimated from Wondergem 2011
    p.w_dot_max = 0.85  # maximum yaw rate [rad/s^2] - estimated with inertia and yaw moment

    # masses
    p.m = 23.8  # mass [kg]
    p.x_g = 0.046  # position of center of gravity along x axis (longitudinal axis) [m]
    p.I_z = 1.760  # moment of inertia around z axis [kg m^2]

    # Various hydrodynamic parameters
    p.X_udot = -2.0
    p.Y_vdot = -10.0
    p.Y_rdot = -0.0
    p.N_rdot = -1.0
    p.N_vdot = -0.0
    p.X_u = -0.72253
    p.Y_v = -0.88965
    p.Y_r = -7.250
    p.N_v = 0.03130
    p.N_r = -1.900

    p.surge_force_max = 2  # max allowed force in surge direction [N]
    p.sway_force_max = 1.5  # max allowed force in sway direction [N]
    p.yaw_moment_max = 1.5  # max allowed moment applied around z axis [Nm]

    return p

    # ------------- END OF CODE --------------
