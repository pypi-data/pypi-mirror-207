__author__ = "Hanna Krasowski"
__copyright__ = "TUM Cyber-Physical Systems Group"
__version__ = "2022a"
__maintainer__ = "Hanna Krasowski"
__email__ = "commonocean@lists.lrz.de"
__status__ = "Released"

class VesselParameters:
    def __init__(self):

        # vehicle body dimensions
        self.l = None  # length [m]
        self.w = None  # width [m]
        self.d = None  # draft [m]

        # velocity and acceleration parameters
        self.v_max = None  # maximum velocity [m/s]
        self.a_max = None  # maximum acceleration [m/s^2]
        self.w_max = None  # maximum yaw [rad/s]
        self.w_dot_max = None  # maximum yaw rate [rad/s^2]

        # masses
        self.m = None  # mass [kg]
        self.x_g = None  # position of center of gravity along x axis (longitudinal axis) [m]
        self.I_z = None  # moment of inertia around z axis [kg m^2]

        # Various hydrodynamic parameters
        self.X_udot = None
        self.Y_vdot = None
        self.Y_rdot = None
        self.N_rdot = None
        self.N_vdot = None
        self.X_u = None
        self.Y_v = None
        self.Y_r = None
        self.N_v = None
        self.N_r = None

        self.surge_force_max = None  # max allowed force in surge direction [N]
        self.sway_force_max = None  # max allowed force in sway direction [N]
        self.yaw_moment_max = None  # max allowed moment applied around z axis [Nm]
