from PySide6.QtCore import QObject, Slot
from mecord.windows.signal_center import SignalCenter


class PythonAdapter(QObject):

    def __init__(self):
        QObject.__init__(self)

    @Slot()
    def on_close_btn_clicked(self):
        SignalCenter().app_quit.emit('close btn clicked')

