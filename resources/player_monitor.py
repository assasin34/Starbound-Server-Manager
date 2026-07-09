from PySide6.QtCore import QTimer, QObject, Signal
from resources.server_controller import ServerController

class PlayerMonitor(QObject):
    current_players = Signal(list)
    
    def __init__(self, server_controller: ServerController):  #! Delete ServerController
        super().__init__()
        self.server = server_controller
        
        self.players = []
        
        self.server.output.connect(self.process_console_line)
        self.server.server_status_changed.connect(self.clear_players)
        
    def process_console_line(self, line):
        if "Logged in" in line:
            self.players.append(line.split()[8].replace("'", ''))
            self.current_players.emit(self.players.copy())
            
        if "disconnected" in line:
            self.players.remove(line.split()[3].replace("'", ''))
            self.current_players.emit(self.players.copy())
            
            
    def clear_players(self, text):
        if text == "Stopped":
            self.players.clear()
            self.current_players.emit(self.players.copy())