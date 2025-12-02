from wpilib.drive import DifferentialDrive
from commands2 import Subsystem

from phoenix5 import WPI_TalonSRX

from src.constants import Drivetrain

class DrivetrainSubsystem(Subsystem):
    def __init__(self) -> None:
        """
        Drivetrain Subsystem base class
        
        Constants are pulled directly from the constants.py file.
        """
        super().__init__()

        left_motor: WPI_TalonSRX = WPI_TalonSRX(Drivetrain.LEFT_MOTOR_PORT)
        left_motor.configFactoryDefault()
        left_motor.setInverted(not Drivetrain.RIGHT_INVERTED)
        
        right_motor: WPI_TalonSRX = WPI_TalonSRX(Drivetrain.RIGHT_MOTOR_PORT)
        right_motor.configFactoryDefault()
        right_motor.setInverted(Drivetrain.RIGHT_INVERTED)

        self._drive: DifferentialDrive = DifferentialDrive(left_motor, right_motor)


    def periodic(self) -> None:
        pass

    def arcade_drive(self, forward: float, rotation: float) -> None:
        """
        Arcade drive method for differential drive

        Parameters:
            - forward: Forward speed
            - rotation: rotational speed 
        """
        self._drive.arcadeDrive(forward, rotation)

    def tank_drive(self, left_speed: float, right_speed: float)-> None:
        """
        
        Tank dirve method for differential drive

        Parameters:
            - left_speed: Left side speed
            - right_speed: Right side speed
        """

        self._drive.tankDrive(left_speed, right_speed)