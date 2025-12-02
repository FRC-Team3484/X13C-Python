import commands2
from src.subsystems.drivetrain_subsystem import DrivetrainSubsystem

class X13B(commands2.TimedCommandRobot):
    def __init__(self) -> None:
        super().__init__()

        self._drivetrain_subsystem: DrivetrainSubsystem = DrivetrainSubsystem()
        