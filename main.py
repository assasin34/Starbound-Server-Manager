from backend.server_controller import ServerController
from backend.resource_monitor import ResourceMonitor
from backend.player_monitor import PlayerMonitor
from backend.uptime_monitor import UpTimeMonitor
from backend.settings_manager import SettingsManager
from PySide6 import QtWidgets
from ui.MainWindow import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.settings_manager = SettingsManager()
        self.server = ServerController(self.settings_manager)
        self.resource_monitor = ResourceMonitor(self.server)
        self.player_monitor = PlayerMonitor(self.server)
        self.uptime_monitor = UpTimeMonitor(self.server)
        
        self.btnStart.clicked.connect(self.start_server)
        self.btnStop.clicked.connect(self.stop_server)
        self.btnRestart.clicked.connect(self.restart_server)
        
        self.server.output.connect(self.add_console_line)
        self.server.server_status_changed.connect(self.update_server_status)
        self.server.ip_changed.connect(self.update_ip)
        
        self.resource_monitor.resources_updated.connect(self.update_resource_display)
        
        self.player_monitor.current_players.connect(self.update_player)
        
        self.uptime_monitor.time_changed.connect(self.update_time)
    
    
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
    
    
    def add_console_line(self, text):
        self.txtConsole.appendPlainText(text)
        
        
    def start_server(self):
        self.txtConsole.clear()
        self.server.start()
           
        
    def stop_server(self):
        self.server.stop()
        
        
    def restart_server(self):
        self.txtConsole.clear()
        self.server.restart()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()