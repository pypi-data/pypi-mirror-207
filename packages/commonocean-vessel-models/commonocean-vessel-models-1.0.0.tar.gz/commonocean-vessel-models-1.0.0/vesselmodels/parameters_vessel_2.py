from vesselmodels.vessel_parameters import VesselParameters

def parameters_vessel_2():
    # parameters_vessel_2
    # values are taken from a tanker which is a lake freighter
    # Syntax:
    #    p = parameters_vessel_2()
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
    # -  T. I. Fossen and T. Perez (2004). Marine Systems Simulator (MSS)
    #    URL: https://github.com/cybergalactic/MSS
    # -  D. Clarke, P. Gelding and G. Hine (1983). The application of
    #    manoeuvring criteria in hull design using linear theory. Transactions
    #    of the Royal Institution of Naval Architects 125, 45-68.
    # -  Van Berlekom, W.B. and Goddard, T.A. (1972). Maneuvering of Large Tankers,
    #    Transaction of SNAME, 80:264-298


    # Author:       Hanna Krasowski
    # Written:      2022-08-22

    # Last revision:---

    # ------------- BEGIN CODE --------------

    # init vehicle parameters
    p = VesselParameters()

    # vehicle body dimensions
    p.l = 304.8  # length [m]
    p.w = 32.0   # width [m]
    p.d = 10.59  # draft [m]

    # velocity and acceleration parameters
    p.v_max = 7.0150  # maximum velocity [m/s]
    p.a_max = 0.0127  # maximum acceleration [m/s^2]
    p.w_max = 0.0078  # maximum yaw [rad/s]
    p.w_dot_max = 3.744858815208155e-06  # maximum yaw rate [rad/s^2]

    # masses
    p.m = 63417860.87  # mass [kg] - calculated with Clarke et al. 1983
    p.x_g = 0.0  # position of center of gravity along x axis (longitudinal axis) [m]
    p.I_z = 429505809549.96 # moment of inertia around z axis [kg m^2] - calculated with Clarke et al. 1983

    # Various hydrodynamic parameters - calculated with Clarke et al. 1983
    p.X_udot = - 2883172.16618208
    p.Y_vdot = - 67881333.7652016
    p.Y_rdot = - 674521167.312627
    p.N_rdot = - 406272307922.226
    p.N_vdot = 140993163.735816
    p.X_u = - 217523.074267002
    p.Y_v = - 311.296240396337
    p.Y_r = 28110.7809555544
    p.N_v = - 32107.5005844114
    p.N_r = - 5184423.65201309

    # maximum forces and torques estimated from accelerations and masses
    p.surge_force_max = p.m * p.a_max  # max allowed force in surge direction [N]
    p.sway_force_max = p.m * p.a_max  # max allowed force in sway direction [N]
    p.yaw_moment_max = p.I_z * p.w_dot_max # max allowed moment applied around z axis [Nm]

    return p

    # ------------- END OF CODE --------------
