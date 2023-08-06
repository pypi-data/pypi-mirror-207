from vesselmodels.vessel_parameters import VesselParameters


def parameters_vessel_1():
    # parameters_vessel_1
    # values are taken from a SR 108 container ship
    # Syntax:  
    #    p = parameters_vessel_1()
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
    # -  S. Nomoto (1982). On the Coupled Motion of Steering and
    #    Rolling of a High Speed Container Ship, Naval Architect of
    #    Ocean Engineering 20:73-83. From J.S.N.A., Japan, Vol. 150, 1981.
    # -  T. I. Fossen and T. Perez (2004). Marine Systems Simulator (MSS)
    #    URL: https://github.com/cybergalactic/MSS
    # -  D. Clarke, P. Gelding and G. Hine (1983). The application of
    #    manoeuvring criteria in hull design using linear theory. Transactions
    #    of the Royal Institution of Naval Architects 125, 45-68.


    # Author:       Hanna Krasowski
    # Written:      2022-08-22

    # Last revision:---

    # ------------- BEGIN CODE --------------

    # init vehicle parameters
    p = VesselParameters()

    # vehicle body dimensions
    p.l = 175  # length [m]
    p.w = 25.4   # width [m]
    p.d = 9.0  # draft [m]

    # velocity and acceleration parameters
    p.v_max = 16.8  # maximum velocity [m/s]
    p.a_max = 0.24  # maximum acceleration [m/s^2]
    p.w_max = 0.03  # maximum yaw [rad/s]
    p.w_dot_max = 2.455465405069919e-05  # maximum yaw rate [rad/s^2]

    # masses
    p.m = 24562069.8750000  # mass [kg] - calculated with Clarke et al. 1983
    p.x_g = -2.55  # position of center of gravity along x axis (longitudinal axis) [m]
    p.I_z = 54996070984.6669  # moment of inertia around z axis [kg m^2] - calculated with Clarke et al. 1983

    # Various hydrodynamic parameters - calculated with Clarke et al. 1983
    p.X_udot = -1799893.02539637
    p.Y_vdot = -26543765.9872343
    p.Y_rdot = -283417813.927590
    p.N_rdot = -44854701237.0896
    p.N_vdot = -175519156.763611
    p.X_u = -150639.788002265
    p.Y_v = -218.602814490728
    p.Y_r = 9276.58982069771
    p.N_v = -14228.3163250072
    p.N_r = -1113465.73754500

    # maximum forces and torques estimated from accelerations and masses
    p.surge_force_max = p.m * p.a_max  # max allowed force in surge direction [N]
    p.sway_force_max = p.m * p.a_max  # max allowed force in sway direction [N]
    p.yaw_moment_max = p.I_z * p.w_dot_max # max allowed moment applied around z axis [Nm]

    return p

    # ------------- END OF CODE --------------
