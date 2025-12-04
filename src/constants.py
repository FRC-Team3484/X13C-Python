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
    class Operator:
        CONTROLLER_PORT: int = 1
        JOYSTICK_DEADBAND: float = 0.02

        LAUNCH_ANGLE: Input = ControllerMap.LEFT_JOY_Y
        LAUNCH_SPEED: Input = ControllerMap.RIGHT_TRIGGER
        

class Launcher:
    PITCH_MOTOR_PORT: int = 10
    PITCH_MOTOR_INVERTED: bool = False
    PITCH_LIMIT_SWITCH_LOW_PORT: int = 2
    PITCH_LIMIT_SWITCH_HIGH_PORT: int = 1

    LAUNCH_MOTOR_PORT_1:int = 7
    LAUNCH_MOTOR_PORT_2: int = 11
