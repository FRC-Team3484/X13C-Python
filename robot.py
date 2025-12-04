import commands2
from src.subsystems.drivetrain_subsystem import DrivetrainSubsystem

from src.subsystems.launcher_subsystem import LauncherSubsystem

from src.oi import DriverInterface, OperatorInterface

from src.commands.teleop_drive_command import TeleopDriveCommand
from src.commands.teleop_launcher_command import TeleopLauncherCommand

class X13B(commands2.TimedCommandRobot):
    def __init__(self) -> None:
        super().__init__()

        self._drive_oi: DriverInterface = DriverInterface()
        self._operator_oi: OperatorInterface = OperatorInterface()


        self._drivetrain_subsystem: DrivetrainSubsystem = DrivetrainSubsystem()
        self._launcher_subsystem: LauncherSubsystem = LauncherSubsystem()

        self._teleop_drive_command: TeleopDriveCommand = TeleopDriveCommand(self._drivetrain_subsystem, self._drive_oi)
        self._teleop_launcher_command: TeleopLauncherCommand = TeleopLauncherCommand(self._launcher_subsystem, self._operator_oi)

    def teleopInit(self) -> None:
        self._teleop_drive_command.schedule()
        self._teleop_launcher_command.schedule()

    def teleopExit(self) -> None:
        self._teleop_drive_command.cancel()