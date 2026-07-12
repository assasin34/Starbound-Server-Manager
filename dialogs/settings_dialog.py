from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog
from PySide6.QtCore import Signal
from ui.SettingsWindow import Ui_Dialog
from backend.settings_manager import SettingsManager

class SettingsDialog(QDialog, Ui_Dialog):
    settings_changed = Signal(dict)
    
    def __init__(self, settings_manager: SettingsManager):
        super().__init__()
        self.setupUi(self)

        self.settings_manager = settings_manager
        self.settings = settings_manager.settings.copy()
        
        self.lineEditServerExecutable.setText(self.settings["server_executable"])
        self.lineEditServerExecutableFolder.setText(self.settings["server_directory"])
        self.lineEditUniverseFolder.setText(self.settings["universe_path"])
        self.lineEditNgrokExecutable.setText(self.settings["ngrok_executable"])
        self.lineEditNgrokExecutableFolder.setText(self.settings["ngrok_directory"])
        self.checkBoxUseNgrok.setChecked(self.settings["use_ngrok"])
        
        self.disable_ngrok_settings(self.checkBoxUseNgrok.isChecked())
        
        self.btnServerExecutableBrowse.clicked.connect(lambda: self.browse_file(self.lineEditServerExecutable))
        self.btnServerExecutableFolderBrowse.clicked.connect(lambda: self.browse_folder(self.lineEditServerExecutableFolder))
        self.btnUniverseFolderBrowse.clicked.connect(lambda: self.browse_folder(self.lineEditUniverseFolder))
        self.btnNgrokExecutableBrowse.clicked.connect(lambda: self.browse_file(self.lineEditNgrokExecutable))
        self.btnNgrokExecutableFolderBrowse.clicked.connect(lambda: self.browse_folder(self.lineEditNgrokExecutableFolder))
        
        self.checkBoxUseNgrok.toggled.connect(self.disable_ngrok_settings)
        self.buttonBox.accepted.connect(self.accept_changes)
    
    
    def browse_file(self, setting_name):
        path = QFileDialog.getOpenFileName()[0]
        setting_name.setText(path)
        
        
    def browse_folder(self, setting_name):
        path = QFileDialog.getExistingDirectory()
        setting_name.setText(path) 
    
        
    def accept_changes(self):
        self.settings["server_executable"] = self.lineEditServerExecutable.text()
        self.settings["server_directory"] = self.lineEditServerExecutableFolder.text()
        self.settings["ngrok_executable"] = self.lineEditNgrokExecutable.text()
        self.settings["ngrok_directory"] = self.lineEditNgrokExecutableFolder.text()
        self.settings["universe_path"] = self.lineEditUniverseFolder.text()
        self.settings["use_ngrok"] = self.checkBoxUseNgrok.isChecked()
        
        self.settings_manager.update_settings(self.settings)
        
        
    def disable_ngrok_settings(self, checked):
            ngrok_settings = [
            self.lineEditNgrokExecutable,
            self.lineEditNgrokExecutableFolder,
            self.btnNgrokExecutableBrowse,
            self.btnNgrokExecutableFolderBrowse,
            ]
            for widget in ngrok_settings:
                widget.setDisabled(not checked)
                
    
    # def popup(self):
    #     msgBox = QMessageBox()
    #     msgBox.setText("The document has been modified.")
    #     msgBox.exec()