from PySide6.QtCore import QObject, QTimer, Signal
import json
import os

class SettingsManager(QObject):
    open_settings = Signal()
    
    SETTINGS_FILE = "settings.json"
    DEFAULT_SETTINGS = {
    "server_executable": "C:\\path\\to\\your\\starbound_server.exe",
    "server_directory": "C:\\path\\to\\your\\server_folder",
    "ngrok_executable": "C:\\path\\to\\your\\ngrok.exe",
    "ngrok_directory": "C:\\path\\to\\your\\ngrok_folder",
    "universe_path": "...",
    "assets_path": "...",
    "use_ngrok": False
}
    
    def __init__(self):
        super().__init__()
        
        if os.path.isfile(self.SETTINGS_FILE):
            self.load_settings()
        else:
            self.create_default_settings()     
            
                
    def create_default_settings(self):
        with open(self.SETTINGS_FILE, "w") as file:
                json.dump(self.DEFAULT_SETTINGS, file, indent=4)
                self.settings = self.DEFAULT_SETTINGS.copy()
        def open_settings():
            self.open_settings.emit()
        QTimer().singleShot(1000, open_settings)
    
    
    def load_settings(self):
        with open(self.SETTINGS_FILE, "r") as file:
            self.settings = json.load(file)           
                
                
    def save_settings(self):
        with open(self.SETTINGS_FILE, 'w') as file:
            json.dump(self.settings, file, indent=4)
            

    def update_settings(self, new_settings):
        self.settings = new_settings
        self.save_settings()