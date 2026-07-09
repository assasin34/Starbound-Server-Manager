from PySide6.QtCore import QProcess, QTimer, Signal, QObject
from resources.settings_manager import SettingsManager
import urllib.request
import json

class ServerController(QObject):
    output = Signal(str)
    server_status_changed = Signal(str)
    ip_changed = Signal(str)

    def __init__(self, settings_manager: SettingsManager):
        super().__init__()
        self.starbound_server_process = QProcess()
        self.ngrok_process = QProcess()
        self.settings_manager = settings_manager
        self.restart_requested = False

        self.starbound_server_process.readyReadStandardOutput.connect(self.read_output)
        self.starbound_server_process.finished.connect(self.on_process_finished)
        self.ngrok_process.started.connect(self.get_public_ip)
        

    def start(self):
        if self.starbound_server_process.state() != QProcess.NotRunning:
            return
        
        self.starbound_server_process.setWorkingDirectory(
            self.settings_manager.settings["server_path"]
        )

        self.starbound_server_process.start(
            self.settings_manager.settings["server_executable_path"]
        )
        
        self.server_status_changed.emit("Starting")
        
        
    def start_ngrok(self):
        arguments = ("tcp", "21025")
        
        self.ngrok_process.setWorkingDirectory(
            self.settings_manager.settings["ngrok_path"]
        )
        
        self.ngrok_process.start(
            self.settings_manager.settings["ngrok_executable_path"], arguments=arguments
        )
              
        
    def stop(self):
        if self.starbound_server_process.state() == QProcess.Running:
            self.server_status_changed.emit("Stopping")

            self.starbound_server_process.terminate()
            
            if not self.restart_requested:
                self.ngrok_process.terminate()
            
            def _force_kill():
                if self.starbound_server_process.state() == QProcess.Running:
                    self.starbound_server_process.kill()
                    
                if not self.restart_requested:
                    if self.ngrok_process.state() == QProcess.Running:
                        self.ngrok_process.kill()
                    
            # if it doesn't stop in 3 seconds → force kill
            QTimer.singleShot(3000, _force_kill)
        
        
    def restart(self):
        self.restart_requested = True
        self.stop()
        self.server_status_changed.emit("Restarting")
        
        
    def read_output(self):
        data = self.starbound_server_process.readAllStandardOutput().data().decode()

        for line in data.splitlines():
            if "listening for incoming TCP connections" in line:
                self.server_status_changed.emit("Online")
                if self.settings_manager.settings["use_ngrok"] == True:
                    if self.ngrok_process.state() != QProcess.Running:
                        self.start_ngrok()
                else:
                    public_ip = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf8')
                    self.ip_changed.emit(f"{public_ip}:21025")
            
            self.output.emit(line)
                
                
    def on_process_finished(self):
        if self.restart_requested:
            self.restart_requested = False
            self.start()
        else:
            self.server_status_changed.emit("Stopped")
            self.ip_changed.emit("")
                
    
    def get_pid(self):
        return self.starbound_server_process.processId()  
       

    def get_public_ip(self):
        def retrieve():
            try:
                content = urllib.request.urlopen("http://127.0.0.1:4040/api/tunnels")
                content = json.load(content)
                for tunnel in content["tunnels"]:
                    if tunnel["proto"] == "tcp":
                        self.ip_changed.emit(tunnel["public_url"][6:])
            except urllib.error.URLError:
                self.ip_changed.emit("Couldn't Retrieve")
        QTimer.singleShot(3000, retrieve)
    