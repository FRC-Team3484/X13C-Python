from wpilib.drive import DifferentialDrive
from commands2 import Subsystem

from phoenix5 import WPI_TalonSRX

from src.constants import Drivetrain

class DrivetrainSubsystem(Subsystem):
    def __init__(self):
        """
        Drivetrain Subsystem base class
        
        Constants are pulled directly from the constants.py file.
        """
        pass