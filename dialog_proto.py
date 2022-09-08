# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_protoOMjicL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget

import rsrc_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(884, 503)
        Dialog.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color:transparent;\n"
"	background:transparent;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"	color:#fff;\n"
"}\n"
"#Dialog{\n"
"	background-color:rgb(31, 35, 42);\n"
"}\n"
"#frame, #frame_2{\n"
"	background-color:#16191d;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#262b32;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dialogPages = QStackedWidget(Dialog)
        self.dialogPages.setObjectName(u"dialogPages")
        self.dial1 = QWidget()
        self.dial1.setObjectName(u"dial1")
        self.verticalLayout = QVBoxLayout(self.dial1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.dial1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 2, 0, 2)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u":/icons-w/Icons-w/activity.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.dial1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(8, 8, 8, 8)
        self.graphicsView = PlotWidget(self.frame_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_3.addWidget(self.graphicsView)


        self.verticalLayout.addWidget(self.frame_3)

        self.dialogPages.addWidget(self.dial1)
        self.dial2 = QWidget()
        self.dial2.setObjectName(u"dial2")
        font1 = QFont()
        font1.setPointSize(8)
        self.dial2.setFont(font1)
        self.verticalLayout_3 = QVBoxLayout(self.dial2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.dial2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 2, 0, 2)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(30, 30))
        self.label_3.setPixmap(QPixmap(u":/icons-w/Icons-w/activity.svg"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.dial2)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_3.addWidget(self.widget_2)

        self.frame_4 = QFrame(self.dial2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setPointSize(10)
        self.pushButton.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons-w/Icons-w/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/icons-w/Icons-w/check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_3.addWidget(self.frame_4, 0, Qt.AlignBottom)

        self.dialogPages.addWidget(self.dial2)

        self.verticalLayout_2.addWidget(self.dialogPages)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Signal Plot", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Dialog 2", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

