from src.constants import UserInterface
from src.FRC3484_Lib.SC_ControllerMaps import GenericController

_DRIVER_INPUTS: type[UserInterface.Driver] = UserInterface.Driver
_OPERATOR_INPUTS: type[UserInterface.Operator] = UserInterface.Operator
class DriverInterface:
    _controller: GenericController = GenericController(
        _DRIVER_INPUTS.CONTROLLER_PORT,
        axis_deadband=_DRIVER_INPUTS.JOYSTICK_DEADBAND
    )

    def __init__(self) -> None:
        pass

    def get_throttle(self) -> float:
        return self._controller.get_axis(_DRIVER_INPUTS.THROTTLE_AXIS)
    
    def get_steer(self) -> float:
        return self._controller.get_axis(_DRIVER_INPUTS.STEER_AXIS)
    
class OperatorInterface:
    _controller: GenericController = GenericController(
        _OPERATOR_INPUTS.CONTROLLER_PORT,
        axis_deadband=_OPERATOR_INPUTS.JOYSTICK_DEADBAND
    )

    def __init__(self) -> None:
        pass

    def get_pitch(self) -> float:
        return self._controller.get_axis(_OPERATOR_INPUTS.LAUNCH_ANGLE)
    def get_launch_speed(self) -> float:
        return self._controller.get_axis(_OPERATOR_INPUTS.LAUNCH_SPEED)