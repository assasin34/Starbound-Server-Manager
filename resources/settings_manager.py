from PySide6.QtCore import QTimer, QObject, Signal
import json
import os

class SettingsManager(QObject):
    
    SETTINGS_FILE = "settings.json"
    
    DEFAULT_SETTINGS = {
    "server_path": "M:\\Starbound_Things\\OpenStarbound-Windows-Server\\win",
    "server_executable_path": "M:\\Starbound_Things\\OpenStarbound-Windows-Server\\win\\starbound_server.exe",
    "ngrok_path": "M:\\Starbound_Things\\OpenStarbound-Windows-Server\\win\\tools",
    "ngrok_executable_path": "M:\\Starbound_Things\\OpenStarbound-Windows-Server\\win\\tools\\ngrok.exe",
    "universe_path": "...",
    "assets_path": "...",
    "auto_start_ngrok": True
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
                
                
    def save_settings(self):
        with open(self.SETTINGS_FILE, 'w') as file:
            json.dump(self.settings, file, indent=4)
            
    
    def load_settings(self):
        with open(self.SETTINGS_FILE, "r") as file:
            self.settings = json.load(file)