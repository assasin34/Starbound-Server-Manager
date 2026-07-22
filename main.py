from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
import sys

from backend.server_controller import ServerController
from backend.resource_monitor import ResourceMonitor
from backend.player_monitor import PlayerMonitor
from backend.uptime_monitor import UpTimeMonitor
from backend.settings_manager import SettingsManager
from backend.config_manager import ConfigManager

from ui.MainWindow import Ui_MainWindow
from dialogs.settings_dialog import SettingsDialog
from dialogs.config_dialog import ConfigDialog

import qdarktheme


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.settings_manager = SettingsManager()
        self.config_manager = ConfigManager(self.settings_manager)
        self.server = ServerController(self.settings_manager, self.config_manager)
        self.resource_monitor = ResourceMonitor(self.server)
        self.player_monitor = PlayerMonitor(self.server)
        self.uptime_monitor = UpTimeMonitor(self.server)
        
        self.btnStart.clicked.connect(self.start_server)
        self.btnStop.clicked.connect(self.stop_server)
        self.btnRestart.clicked.connect(self.restart_server)
        self.btnSettings.clicked.connect(self.open_settings)
        self.btnConfig.clicked.connect(self.open_config)
        
        self.server.output.connect(self.add_console_line)
        self.server.server_status_changed.connect(self.update_server_status)
        self.server.ip_changed.connect(self.update_ip)
        
        self.resource_monitor.resources_updated.connect(self.update_resource_display)
        
        self.player_monitor.current_players.connect(self.update_player)
        
        self.uptime_monitor.time_changed.connect(self.update_time)
        
        self.settings_manager.open_settings.connect(self.open_settings)
    
    
    def start_server(self):
        self.txtConsole.clear()
        self.server.start()
           
        
    def stop_server(self):
        self.server.stop()
        
        
    def restart_server(self):
        self.txtConsole.clear()
        self.server.restart()


    def add_console_line(self, text):
        self.txtConsole.appendPlainText(text)

    
    def update_server_status(self, text):
        if text == "Online":
            self.ServerStatusInfo.setText("Online")
            self.ServerStatusInfo.setStyleSheet("color: green; font-weight: bold;")
            self.btnStop.setEnabled(True)
            self.btnRestart.setEnabled(True)
        elif text == "Starting":
            self.ServerStatusInfo.setText("Starting...")
            self.ServerStatusInfo.setStyleSheet("color: orange; font-weight: bold;")
            self.btnStart.setDisabled(True)
        elif text == "Stopped":
            self.ServerStatusInfo.setText("Offline")
            self.ServerStatusInfo.setStyleSheet("color: red; font-weight: bold;")
            self.btnStart.setEnabled(True) 
        elif text == "Stopping":
            self.ServerStatusInfo.setText("Stopping...")
            self.ServerStatusInfo.setStyleSheet("color: orange; font-weight: bold;")
            self.btnStop.setDisabled(True)
            self.btnRestart.setDisabled(True)
        elif text == "Restarting":
            self.ServerStatusInfo.setText("Restarting...")
            self.ServerStatusInfo.setStyleSheet("color: orange; font-weight: bold;")      
            self.btnStop.setDisabled(True)
            self.btnRestart.setDisabled(True)
    
    
    def update_resource_display(self, process_ram, total_ram, process_cpu, total_cpu):
        self.RAMServerProgressBar.setValue(process_ram)
        self.RAMTotalProgressBar.setValue(total_ram)
        self.CPUServerProgressBar.setValue(process_cpu)
        self.CPUTotalProgressBar.setValue(total_cpu)
    
    
    def update_ip(self, public_ip):
        self.ServerIPInfo.setText(public_ip)
        self.ServerIPInfo.setStyleSheet("color: Blue; font-weight: bold;")
    
    
    def update_player(self, players):
        self.listPlayers.clear()
        self.listPlayers.addItems(players)
        self.ServerPlayersCountInfo.setText(str(len(players)))
    
    
    def update_time(self, time):
        self.ServerUptimeInfo.setText(time)
        self.ServerUptimeInfo.setStyleSheet("font-weight: bold;")


    def open_settings(self):
        dialog = SettingsDialog(self.settings_manager)
        dialog.exec()
   
   
    def open_config(self):
        if self.config_manager.load_config():
            dialog = ConfigDialog(self.config_manager)  
            dialog.exec()
        else:
            QMessageBox.warning(
            self,
            "Config file not found",
            "Please make sure you chose the correct path to storage directory in settings."
        )
      
def main():
    try:
        import pyi_splash  # type: ignore
    except ImportError:
        pyi_splash = None
        
    app = QtWidgets.QApplication(sys.argv)
    # qdarktheme.setup_theme() #TODO Dark Theme

    window = MainWindow()
    window.show()
    
    if pyi_splash:
        pyi_splash.close()
        
    app.exec()
    
    
main()