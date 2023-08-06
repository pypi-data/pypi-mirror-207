from PySide6.QtWidgets import QApplication
from mecord.windows.window_manager import WindowManager
from mecord.windows.signal_center import SignalCenter


class IApplication(QApplication):

    def __init__(self, args):
        super().__init__(args)
        self.windows_manager = WindowManager()
        SignalCenter().app_quit.connect(self.app_quit)

    def app_quit(self, rs):
        self.quit()


