from commands2 import Command

from src.oi import OperatorInterface
from src.subsystems.launcher_subsystem import LauncherSubsystem

class TeleopLauncherCommand(Command):
    def __init__(self, launcher:LauncherSubsystem, oi: OperatorInterface):
        super().__init__()
        self._launcher = launcher
        self._oi = oi
        self.addRequirements(launcher)
    
    def initialize(self):
        pass

    def execute(self):
        self._launcher.spool(self._oi.get_launch_speed())
        self._launcher.pitch(self._oi.get_pitch())

    def end(self, interrupted: bool):
        self._launcher.spool(0)
        self._launcher.pitch(0)
    
    def isFinished(self) -> bool:
        return False