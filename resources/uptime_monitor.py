from PySide6.QtCore import QTimer, QObject, Signal
from resources.server_controller import ServerController
import time
from math import floor

class UpTimeMonitor(QObject):
    time_changed = Signal(str)
    
    def __init__(self, server_controller: ServerController):
        super().__init__()
        self.server = server_controller
        self.timer = QTimer(interval=900)
        
        self.server.server_status_changed.connect(self.start_timer)
        
        self.timer.timeout.connect(self.update_time)
        
        
    def start_timer(self, text):
        if text == "Online":
            self.timer.start()
            self.start_time = time.monotonic()
        elif text == "Stopped" or text == "Restarting":
            self.timer.stop()
            self.time_changed.emit('0h 0m 0s')
    
    def update_time(self):
        elapsed = time.monotonic() - self.start_time
        hours = elapsed / 60 / 60
        minutes = (elapsed / 60) - floor(hours) * 60
        seconds = elapsed - (floor(minutes) * 60) - (floor(hours) * 60 * 60)
        combined_time = f'{floor(hours)}h {floor(minutes)}m {floor(seconds)}s'
        self.time_changed.emit(combined_time)