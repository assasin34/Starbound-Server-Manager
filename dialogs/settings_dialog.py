from PySide6.QtWidgets import QDialog
from ui.SettingsDialog import Ui_Dialog
from backend.settings_manager import SettingsManager

class SettingsDialog(QDialog, Ui_Dialog):
    def __init__(self, settings_manager: SettingsManager):
        super().__init__()
        self.setupUi(self)

        self.settings_manager = settings_manager
        self.lineEditServerExecutable.setText(self.settings_manager.settings["server_executable"])
        self.lineEditServerExecutableFolder.setText(self.settings_manager.settings["server_directory"])
        self.lineEditUniverseFolder.setText(self.settings_manager.settings["universe_path"])
        self.lineEditNgrokExecutable.setText(self.settings_manager.settings["ngrok_executable"])
        self.lineEditNgrokExecutableFolder.setText(self.settings_manager.settings["ngrok_directory"])
        self.checkBoxUseNgrok.setChecked(self.settings_manager.settings["use_ngrok"])
        self.disable_ngrok_settings(self.checkBoxUseNgrok.isChecked())
        
        self.checkBoxUseNgrok.toggled.connect(self.disable_ngrok_settings)
        
        
    def disable_ngrok_settings(self, checked):
            ngrok_settings = [
            self.lineEditNgrokExecutable,
            self.lineEditNgrokExecutableFolder,
            self.btnNgrokExecutableBrowse,
            self.btnNgrokExecutableFolderBrowse,
            ]
            for widget in ngrok_settings:
                widget.setDisabled(not checked)