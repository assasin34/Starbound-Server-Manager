# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StarboundServerGUI.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(862, 597)
        MainWindow.setMinimumSize(QSize(862, 597))
        MainWindow.setMaximumSize(QSize(862, 597))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 0, 861, 571))
        self.tabWidget.setStyleSheet(u"QTabWidget { background-color: rgb(236, 236, 236) }\n"
"")
        self.tabWidget.setTabBarAutoHide(False)
        self.tabGeneral = QWidget()
        self.tabGeneral.setObjectName(u"tabGeneral")
        self.tabGeneral.setEnabled(True)
        self.txtConsole = QPlainTextEdit(self.tabGeneral)
        self.txtConsole.setObjectName(u"txtConsole")
        self.txtConsole.setGeometry(QRect(210, 30, 641, 381))
        self.txtConsole.setStyleSheet(u"QPlainTextEdit{border: 1px solid black; background-color: rgb(255, 255, 255);}\n"
"")
        self.txtConsole.setFrameShape(QFrame.Shape.StyledPanel)
        self.txtConsole.setFrameShadow(QFrame.Shadow.Sunken)
        self.txtConsole.setMidLineWidth(0)
        self.txtConsole.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.txtConsole.setReadOnly(True)
        self.listPlayers = QListWidget(self.tabGeneral)
        self.listPlayers.setObjectName(u"listPlayers")
        self.listPlayers.setGeometry(QRect(10, 30, 191, 381))
        self.listPlayers.setStyleSheet(u"QListWidget{border: 1px solid black; background-color: rgb(255, 255, 255);}\n"
"")
        self.labelPlayers = QLabel(self.tabGeneral)
        self.labelPlayers.setObjectName(u"labelPlayers")
        self.labelPlayers.setGeometry(QRect(10, 10, 49, 16))
        self.labelConsole = QLabel(self.tabGeneral)
        self.labelConsole.setObjectName(u"labelConsole")
        self.labelConsole.setGeometry(QRect(210, 10, 49, 16))
        self.groupServerInfo = QGroupBox(self.tabGeneral)
        self.groupServerInfo.setObjectName(u"groupServerInfo")
        self.groupServerInfo.setGeometry(QRect(210, 420, 311, 121))
        self.labelServerStatus_1 = QLabel(self.groupServerInfo)
        self.labelServerStatus_1.setObjectName(u"labelServerStatus_1")
        self.labelServerStatus_1.setGeometry(QRect(20, 24, 71, 20))
        self.labelServerStatus_2 = QLabel(self.groupServerInfo)
        self.labelServerStatus_2.setObjectName(u"labelServerStatus_2")
        self.labelServerStatus_2.setGeometry(QRect(20, 44, 81, 20))
        self.labelServerStatus_3 = QLabel(self.groupServerInfo)
        self.labelServerStatus_3.setObjectName(u"labelServerStatus_3")
        self.labelServerStatus_3.setGeometry(QRect(20, 64, 51, 20))
        self.ServerStatusInfo = QLabel(self.groupServerInfo)
        self.ServerStatusInfo.setObjectName(u"ServerStatusInfo")
        self.ServerStatusInfo.setGeometry(QRect(94, 24, 81, 20))
        self.ServerUptimeInfo = QLabel(self.groupServerInfo)
        self.ServerUptimeInfo.setObjectName(u"ServerUptimeInfo")
        self.ServerUptimeInfo.setGeometry(QRect(100, 44, 91, 20))
        self.ServerIPInfo = QLabel(self.groupServerInfo)
        self.ServerIPInfo.setObjectName(u"ServerIPInfo")
        self.ServerIPInfo.setGeometry(QRect(72, 64, 231, 20))
        self.ServerIPInfo.setOpenExternalLinks(False)
        self.ServerIPInfo.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)
        self.labelServerStatus_4 = QLabel(self.groupServerInfo)
        self.labelServerStatus_4.setObjectName(u"labelServerStatus_4")
        self.labelServerStatus_4.setGeometry(QRect(20, 84, 51, 20))
        self.ServerPlayersCountInfo = QLabel(self.groupServerInfo)
        self.ServerPlayersCountInfo.setObjectName(u"ServerPlayersCountInfo")
        self.ServerPlayersCountInfo.setGeometry(QRect(65, 84, 31, 20))
        self.groupServerControl = QGroupBox(self.tabGeneral)
        self.groupServerControl.setObjectName(u"groupServerControl")
        self.groupServerControl.setEnabled(True)
        self.groupServerControl.setGeometry(QRect(10, 420, 191, 121))
        self.btnStart = QPushButton(self.groupServerControl)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setEnabled(True)
        self.btnStart.setGeometry(QRect(10, 20, 171, 31))
        self.btnStart.setAutoDefault(False)
        self.btnRestart = QPushButton(self.groupServerControl)
        self.btnRestart.setObjectName(u"btnRestart")
        self.btnRestart.setEnabled(False)
        self.btnRestart.setGeometry(QRect(10, 80, 171, 31))
        self.btnStop = QPushButton(self.groupServerControl)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setEnabled(False)
        self.btnStop.setGeometry(QRect(10, 50, 171, 31))
        self.groupResourcesUsage = QGroupBox(self.tabGeneral)
        self.groupResourcesUsage.setObjectName(u"groupResourcesUsage")
        self.groupResourcesUsage.setGeometry(QRect(540, 420, 311, 121))
        self.line = QFrame(self.groupResourcesUsage)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 10, 311, 111))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.labelResourcesUsage_1 = QLabel(self.groupResourcesUsage)
        self.labelResourcesUsage_1.setObjectName(u"labelResourcesUsage_1")
        self.labelResourcesUsage_1.setGeometry(QRect(10, 18, 61, 16))
        self.labelResourcesUsage_2 = QLabel(self.groupResourcesUsage)
        self.labelResourcesUsage_2.setObjectName(u"labelResourcesUsage_2")
        self.labelResourcesUsage_2.setGeometry(QRect(160, 18, 71, 16))
        self.CPUServerProgressBar = QProgressBar(self.groupResourcesUsage)
        self.CPUServerProgressBar.setObjectName(u"CPUServerProgressBar")
        self.CPUServerProgressBar.setGeometry(QRect(50, 40, 91, 31))
        self.CPUServerProgressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #333;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #00aa00;\n"
"}")
        self.CPUServerProgressBar.setValue(24)
        self.CPUTotalProgressBar = QProgressBar(self.groupResourcesUsage)
        self.CPUTotalProgressBar.setObjectName(u"CPUTotalProgressBar")
        self.CPUTotalProgressBar.setGeometry(QRect(50, 80, 91, 31))
        self.CPUTotalProgressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #333;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #00aa00;\n"
"}")
        self.CPUTotalProgressBar.setValue(24)
        self.label = QLabel(self.groupResourcesUsage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(7, 48, 49, 16))
        self.label_2 = QLabel(self.groupResourcesUsage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(7, 88, 49, 16))
        self.RAMServerProgressBar = QProgressBar(self.groupResourcesUsage)
        self.RAMServerProgressBar.setObjectName(u"RAMServerProgressBar")
        self.RAMServerProgressBar.setGeometry(QRect(203, 39, 91, 31))
        self.RAMServerProgressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #333;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #00aa00;\n"
"}")
        self.RAMServerProgressBar.setValue(24)
        self.RAMTotalProgressBar = QProgressBar(self.groupResourcesUsage)
        self.RAMTotalProgressBar.setObjectName(u"RAMTotalProgressBar")
        self.RAMTotalProgressBar.setGeometry(QRect(203, 79, 91, 31))
        self.RAMTotalProgressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #333;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #00aa00;\n"
"}")
        self.RAMTotalProgressBar.setValue(24)
        self.label_3 = QLabel(self.groupResourcesUsage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 87, 49, 16))
        self.label_4 = QLabel(self.groupResourcesUsage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 47, 49, 16))
        self.btnSettings = QPushButton(self.tabGeneral)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setGeometry(QRect(770, 0, 81, 26))
        self.tabWidget.addTab(self.tabGeneral, "")
        self.tabConfig = QWidget()
        self.tabConfig.setObjectName(u"tabConfig")
        self.tabWidget.addTab(self.tabConfig, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Starbound Server Manager", None))
        self.labelPlayers.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Players:</span></p></body></html>", None))
        self.labelConsole.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Console:</span></p></body></html>", None))
        self.groupServerInfo.setTitle(QCoreApplication.translate("MainWindow", u"Server Info", None))
        self.labelServerStatus_1.setText(QCoreApplication.translate("MainWindow", u"Server Status:  ", None))
        self.labelServerStatus_2.setText(QCoreApplication.translate("MainWindow", u"Server Uptime:", None))
        self.labelServerStatus_3.setText(QCoreApplication.translate("MainWindow", u"Server IP:", None))
        self.ServerStatusInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#ff0000;\">Offline</span></p></body></html>", None))
        self.ServerUptimeInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">0h 0m 0s</span></p></body></html>", None))
        self.ServerIPInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.labelServerStatus_4.setText(QCoreApplication.translate("MainWindow", u"Players:", None))
        self.ServerPlayersCountInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#000000;\">0</span></p></body></html>", None))
        self.groupServerControl.setTitle(QCoreApplication.translate("MainWindow", u"Server Controls", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btnRestart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.groupResourcesUsage.setTitle(QCoreApplication.translate("MainWindow", u"Resources Usage", None))
        self.labelResourcesUsage_1.setText(QCoreApplication.translate("MainWindow", u"CPU Usage:", None))
        self.labelResourcesUsage_2.setText(QCoreApplication.translate("MainWindow", u"RAM Usage:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Server:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Server:", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), QCoreApplication.translate("MainWindow", u"General", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfig), QCoreApplication.translate("MainWindow", u"Config", None))
    # retranslateUi

