# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(651, 513)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(651, 513))
        Dialog.setMaximumSize(QSize(651, 16777215))
        Dialog.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        Dialog.setStyleSheet(u"QDialog { background-color: rgb(236, 236, 236) }\n"
"")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(0, 480, 621, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setCenterButtons(True)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 7, 191, 41))
        self.label.setStyleSheet(u"font: 700 18pt \"Arial\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 40, 651, 441))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, -2, 81, 31))
        self.label_2.setStyleSheet(u"font: 15pt \"Segoe UI\";")
        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 20, 651, 21))
        self.line_2.setStyleSheet(u"")
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(110, 30, 441, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEditServerExecutable = QLineEdit(self.verticalLayoutWidget)
        self.lineEditServerExecutable.setObjectName(u"lineEditServerExecutable")

        self.verticalLayout.addWidget(self.lineEditServerExecutable)

        self.lineEditServerExecutableFolder = QLineEdit(self.verticalLayoutWidget)
        self.lineEditServerExecutableFolder.setObjectName(u"lineEditServerExecutableFolder")

        self.verticalLayout.addWidget(self.lineEditServerExecutableFolder)

        self.lineEditUniverseFolder = QLineEdit(self.verticalLayoutWidget)
        self.lineEditUniverseFolder.setObjectName(u"lineEditUniverseFolder")

        self.verticalLayout.addWidget(self.lineEditUniverseFolder)

        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(550, 29, 83, 201))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.btnServerExecutableBrowse = QPushButton(self.verticalLayoutWidget_2)
        self.btnServerExecutableBrowse.setObjectName(u"btnServerExecutableBrowse")

        self.verticalLayout_2.addWidget(self.btnServerExecutableBrowse)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btnServerExecutableFolderBrowse = QPushButton(self.verticalLayoutWidget_2)
        self.btnServerExecutableFolderBrowse.setObjectName(u"btnServerExecutableFolderBrowse")

        self.verticalLayout_2.addWidget(self.btnServerExecutableFolderBrowse)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.btnUniverseFolderBrowse = QPushButton(self.verticalLayoutWidget_2)
        self.btnUniverseFolderBrowse.setObjectName(u"btnUniverseFolderBrowse")

        self.verticalLayout_2.addWidget(self.btnUniverseFolderBrowse)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 230, 81, 31))
        self.label_5.setStyleSheet(u"font: 15pt \"Segoe UI\";")
        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 253, 651, 21))
        self.line_3.setStyleSheet(u"")
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 101, 20))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 120, 101, 20))
        self.verticalLayoutWidget_5 = QWidget(self.groupBox)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(550, 299, 83, 141))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_10)

        self.btnNgrokExecutableBrowse = QPushButton(self.verticalLayoutWidget_5)
        self.btnNgrokExecutableBrowse.setObjectName(u"btnNgrokExecutableBrowse")

        self.verticalLayout_7.addWidget(self.btnNgrokExecutableBrowse)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_11)

        self.btnNgrokExecutableFolderBrowse = QPushButton(self.verticalLayoutWidget_5)
        self.btnNgrokExecutableFolderBrowse.setObjectName(u"btnNgrokExecutableFolderBrowse")

        self.verticalLayout_7.addWidget(self.btnNgrokExecutableFolderBrowse)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_12)

        self.verticalLayoutWidget_6 = QWidget(self.groupBox)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(110, 300, 441, 141))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEditNgrokExecutable = QLineEdit(self.verticalLayoutWidget_6)
        self.lineEditNgrokExecutable.setObjectName(u"lineEditNgrokExecutable")

        self.verticalLayout_8.addWidget(self.lineEditNgrokExecutable)

        self.lineEditNgrokExecutableFolder = QLineEdit(self.verticalLayoutWidget_6)
        self.lineEditNgrokExecutableFolder.setObjectName(u"lineEditNgrokExecutableFolder")

        self.verticalLayout_8.addWidget(self.lineEditNgrokExecutableFolder)

        self.checkBoxUseNgrok = QCheckBox(self.groupBox)
        self.checkBoxUseNgrok.setObjectName(u"checkBoxUseNgrok")
        self.checkBoxUseNgrok.setGeometry(QRect(10, 280, 99, 24))
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 330, 101, 20))
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 390, 101, 20))
        self.line_6 = QFrame(self.groupBox)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(0, 224, 651, 21))
        self.line_6.setStyleSheet(u"")
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_6.setLineWidth(1)
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 180, 101, 20))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Settings", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Server", None))
        self.btnServerExecutableBrowse.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.btnServerExecutableFolderBrowse.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.btnUniverseFolderBrowse.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Network", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Executable:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Executable Folder:", None))
        self.btnNgrokExecutableBrowse.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.btnNgrokExecutableFolderBrowse.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.checkBoxUseNgrok.setText(QCoreApplication.translate("Dialog", u"Use Ngrok", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Executable:", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Executable Folder:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Universe Folder:", None))
    # retranslateUi

