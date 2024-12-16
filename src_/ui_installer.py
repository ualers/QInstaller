# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_installer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.Theme import QPushButton
from Custom_Widgets.Theme import QLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(658, 345)
        MainWindow.setMinimumSize(QSize(658, 345))
        MainWindow.setMaximumSize(QSize(658, 345))
        MainWindow.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QCustomQStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_5 = QGridLayout(self.page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer = QSpacerItem(360, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.Button_next = QPushButton(self.page)
        self.Button_next.setObjectName(u"Button_next")
        self.Button_next.setMinimumSize(QSize(0, 27))
        self.Button_next.setMaximumSize(QSize(16777215, 16777215))
        self.Button_next.setStyleSheet(u"            QPushButton {\n"
"                background-color: #EDEDED;\n"
"	\n"
"                border-radius: 11px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 11px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #EDEDED ;\n"
"            }\n"
"")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/navigate_next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_next.setIcon(icon)
        self.Button_next.setIconSize(QSize(28, 29))

        self.gridLayout_5.addWidget(self.Button_next, 4, 1, 1, 1)

        self.button_cancel = QPushButton(self.page)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setMinimumSize(QSize(0, 27))
        self.button_cancel.setStyleSheet(u"            QPushButton {\n"
"                background-color: #EDEDED;\n"
"	\n"
"                border-radius: 11px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 11px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #EDEDED ;\n"
"            }\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_cancel.setIcon(icon1)

        self.gridLayout_5.addWidget(self.button_cancel, 4, 2, 1, 1)

        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background:rgb(226, 226, 226)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer = QSpacerItem(20, 167, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_4.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.lineEdit_path_install = QTextEdit(self.frame_2)
        self.lineEdit_path_install.setObjectName(u"lineEdit_path_install")
        self.lineEdit_path_install.setMinimumSize(QSize(0, 46))
        self.lineEdit_path_install.setMaximumSize(QSize(16777215, 46))
        self.lineEdit_path_install.setStyleSheet(u"            QTextEdit {\n"
"                border: 1px solid #E0E0E0;\n"
"                padding: 10px;\n"
"                border-radius: 10px;\n"
"                background-color: #F7F7F7;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.gridLayout_4.addWidget(self.lineEdit_path_install, 2, 1, 1, 1)

        self.Tosearchfor = QPushButton(self.frame_2)
        self.Tosearchfor.setObjectName(u"Tosearchfor")
        self.Tosearchfor.setMinimumSize(QSize(100, 47))
        self.Tosearchfor.setStyleSheet(u"            QPushButton {\n"
"                background-color: rgb(226, 226, 226);\n"
"	\n"
"                border-radius: 11px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 11px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            \n"
"            QPushButton:hover {\n"
"                background-color: white;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #EDEDED ;\n"
"            }")
        icon2 = QIcon()
        icon2.addFile(u":/font_awesome_solid/icons/font_awesome/solid/magnifying-glass-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Tosearchfor.setIcon(icon2)
        self.Tosearchfor.setIconSize(QSize(11, 11))

        self.gridLayout_4.addWidget(self.Tosearchfor, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 2)

        self.label_space_required = QLabel(self.frame_2)
        self.label_space_required.setObjectName(u"label_space_required")

        self.gridLayout_4.addWidget(self.label_space_required, 5, 0, 1, 2)


        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 2, 0, 1, 3)

        self.line_2 = QFrame(self.page)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 3, 0, 1, 3)

        self.line = QFrame(self.page)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line, 1, 0, 1, 3)

        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_11 = QGridLayout(self.page_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_4 = QFrame(self.page_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background:rgb(226, 226, 226)")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_cancel_installing = QPushButton(self.frame_4)
        self.pushButton_cancel_installing.setObjectName(u"pushButton_cancel_installing")
        self.pushButton_cancel_installing.setMinimumSize(QSize(79, 23))
        self.pushButton_cancel_installing.setMaximumSize(QSize(79, 16777215))
        self.pushButton_cancel_installing.setStyleSheet(u"            QPushButton {\n"
"                background-color: #EDEDED;\n"
"	\n"
"                border-radius: 11px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 15px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #EDEDED ;\n"
"            }\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/font_awesome_solid/icons/font_awesome/solid/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_cancel_installing.setIcon(icon3)
        self.pushButton_cancel_installing.setIconSize(QSize(17, 13))

        self.gridLayout_9.addWidget(self.pushButton_cancel_installing, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.progressBar = QProgressBar(self.frame_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_10.addWidget(self.progressBar, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 167, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_10.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_path_src_installing = QLabel(self.frame_4)
        self.label_path_src_installing.setObjectName(u"label_path_src_installing")

        self.gridLayout_10.addWidget(self.label_path_src_installing, 1, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_10, 1, 0, 1, 2)


        self.gridLayout_11.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_3, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_14 = QGridLayout(self.page_3)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_5 = QFrame(self.page_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(200, 0))
        self.frame_5.setStyleSheet(u"background:rgb(14, 6, 109)")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout_14.addWidget(self.frame_5, 0, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_12.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_12.addWidget(self.label_8, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_3, 7, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 9, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_12.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_12.addWidget(self.label_9, 4, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 16, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_12.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.checkBoxRun = QCheckBox(self.page_3)
        self.checkBoxRun.setObjectName(u"checkBoxRun")
        self.checkBoxRun.setChecked(True)

        self.gridLayout_12.addWidget(self.checkBoxRun, 6, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.verticalSpacer_6, 5, 0, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_12, 0, 1, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalSpacer_3 = QSpacerItem(420, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.pushButton_finish_installer = QPushButton(self.page_3)
        self.pushButton_finish_installer.setObjectName(u"pushButton_finish_installer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_finish_installer.sizePolicy().hasHeightForWidth())
        self.pushButton_finish_installer.setSizePolicy(sizePolicy1)
        self.pushButton_finish_installer.setMinimumSize(QSize(64, 25))
        self.pushButton_finish_installer.setStyleSheet(u"            QPushButton {\n"
"                background-color: #EDEDED;\n"
"	\n"
"                border-radius: 11px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 15px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #DCDCDC;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #EDEDED ;\n"
"            }\n"
"")

        self.gridLayout_13.addWidget(self.pushButton_finish_installer, 0, 1, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_13, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Button_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.button_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.Tosearchfor.setText(QCoreApplication.translate("MainWindow", u"To search for...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"To Continue Click Next. If you would like to select a different folder,\n"
"Click Browse.", None))
        self.label_space_required.setText(QCoreApplication.translate("MainWindow", u"At least {} MBs of free disk space is required.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Select the Destination Location</span></p></body></html>", None))
        self.pushButton_cancel_installing.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Extracting Files...", None))
        self.label_path_src_installing.setText(QCoreApplication.translate("MainWindow", u"D:\\Save disk C\\Saas do site\\IVPN_auto_rotate\\Installer", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Installing </span><br/>Please wait while the installer installs {} on your computer.</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Installer {}", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The Installer has finished installing {} on your computer.  <br> The application can be launched by selecting installed shortcuts.</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Click Finish to exit the installer.", None))
        self.checkBoxRun.setText(QCoreApplication.translate("MainWindow", u"Run {}", None))
        self.pushButton_finish_installer.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
    # retranslateUi

