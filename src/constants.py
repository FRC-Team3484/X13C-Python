from src.FRC3484_Lib.SC_ControllerMaps import Input
from src.FRC3484_Lib.SC_ControllerMaps import XboxControllerMap as ControllerMap


class Drivetrain:
    LEFT_MOTOR_PORT: int = 3
    RIGHT_MOTOR_PORT: int = 2

    RIGHT_INVERTED: bool = True

class UserInterface:
    class Driver:
        CONTROLLER_PORT: int = 0
        JOYSTICK_DEADBAND: float = 0.02

        THROTTLE_AXIS: Input = ControllerMap.LEFT_JOY_Y
        STEER_AXIS: Input = ControllerMap.LEFT_JOY_X