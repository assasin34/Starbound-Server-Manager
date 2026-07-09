from PySide6.QtCore import QTimer, QObject, Signal
import psutil

class ResourceMonitor(QObject):
    resources_updated = Signal(float, float, float, float)
    
    def __init__(self, server_controller):
        super().__init__()
        self.timer = QTimer(interval=1000)
        self.timer.start()
        self.server_controller = server_controller
        self.timer.timeout.connect(self.update_resources)
        
        
    def update_resources(self):
        pid = self.server_controller.get_pid()
        if pid == 0:
            process_cpu, process_ram = 0, 0
        else:
            process = psutil.Process(pid)
            process_ram = process.memory_percent()
            process_cpu = process.cpu_percent()
        total_ram = psutil.virtual_memory().percent
        total_cpu = psutil.cpu_percent()
        self.resources_updated.emit(process_ram, total_ram, process_cpu, total_cpu)
        
        