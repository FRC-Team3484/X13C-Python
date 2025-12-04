from wpilib import SmartDashboard, DigitalInput
from commands2 import Subsystem
from phoenix5 import WPI_TalonSRX, FollowerType, NeutralMode
from src.constants import Launcher

class LauncherSubsystem(Subsystem):
    def __init__(self) -> None:
        """
        Launcher subsystem

        :param self: Description
        """
        super().__init__()
        self._launcher_motor_1:WPI_TalonSRX = WPI_TalonSRX(Launcher.LAUNCH_MOTOR_PORT_1)
        self._launcher_motor_1.configFactoryDefault()

        self._launcher_motor_2: WPI_TalonSRX = WPI_TalonSRX(Launcher.LAUNCH_MOTOR_PORT_2)
        self._launcher_motor_2.configFactoryDefault()
        self._launcher_motor_2.follow(self._launcher_motor_1, FollowerType.PercentOutput)

        self._pitch_motor: WPI_TalonSRX = WPI_TalonSRX(Launcher.PITCH_MOTOR_PORT)
        self._pitch_motor.configFactoryDefault()
        self._pitch_motor.setNeutralMode(NeutralMode.Brake)

        self._pitch_limit_switch_low: DigitalInput = DigitalInput(Launcher.PITCH_LIMIT_SWITCH_LOW_PORT)
        self._pitch_limit_switch_high: DigitalInput = DigitalInput(Launcher.PITCH_LIMIT_SWITCH_HIGH_PORT)

    def periodic(self) -> None:
        SmartDashboard.putBoolean("Min Sensor", self.at_min_pitch())
        SmartDashboard.putBoolean("Max Sensor", self.at_max_pitch())

    def pitch(self, power:float)->None:
        if (power < 0 and self.at_min_pitch()) or (power > 0 and self.at_max_pitch()):
            power = 0
        self._pitch_motor.set(power)

    def at_min_pitch(self)->bool:
        return not self._pitch_limit_switch_low.get()
    
    def at_max_pitch(self)-> bool:
        return not self._pitch_limit_switch_high.get()
    

    def spool(self, speed: float)->None:
        self._launcher_motor_1.set(speed)