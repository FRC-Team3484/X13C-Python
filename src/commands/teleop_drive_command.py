from commands2 import Command

from src.oi import DriverInterface
from src.subsystems.drivetrain_subsystem import DrivetrainSubsystem

class TeleopDriveCommand(Command):
    def __init__(self, drivetrain: DrivetrainSubsystem, oi: DriverInterface)-> None:
        super().__init__()
        self._drivetrain = drivetrain
        self._oi = oi

        self.addRequirements(drivetrain)

    def initialize(self) -> None:
        pass

    def execute(self):
        self._drivetrain.arcade_drive(
            self._oi.get_throttle(),
            self._oi.get_steer()
        )
    
    def end(self, interrupted:bool) -> None:
        self._drivetrain.tank_drive(0,0)

    def isFinished(self) -> bool:
        return super().isFinished()