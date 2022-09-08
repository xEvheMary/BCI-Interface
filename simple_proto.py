# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_protoqRIsCp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import rsrc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1190, 626)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color:transparent;\n"
"	background:transparent;\n"
"	padding: 0px;\n"
"	margin: 0px;\n"
"	color:#fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color:rgb(31, 35, 42);\n"
"}\n"
"#LeftMenuSubContainer, #headerContainer, #footerContainer, #extraHeader{\n"
"	background-color:#16191d;\n"
"}\n"
"#LeftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 6px 8px;\n"
"}\n"
"#CenterMenuSubContainer{\n"
"	background-color:#2c313c;\n"
"}\n"
"#groupBox_3 QPushButton{\n"
"	text-align: center;\n"
"	padding: 8px 14px;\n"
"	background-color:#2c313c;\n"
"}\n"
"#AvStreams, #AvChannels, #ds_contents{\n"
"	background-color:#2c313c;\n"
"}\n"
"QHeaderView::section { \n"
"	background-color:#16191d;\n"
"}\n"
"#listView, #treeView, #extraContent {\n"
"	background-color:#2c313c;\n"
"}\n"
"#pathBox{\n"
"	background-color:#fff;\n"
"	color:#000;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(41, 45, 52, 150);\n"
"}\n"
"#LeftMenuContainer QPushButton:hover{\n"
"	background-color:rg"
                        "ba(41, 45, 52, 100);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.LeftMenuContainer.setObjectName(u"LeftMenuContainer")
        self.LeftMenuContainer.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.LeftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuSubContainer = QWidget(self.LeftMenuContainer)
        self.LeftMenuSubContainer.setObjectName(u"LeftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.frame = QFrame(self.LeftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons-w/Icons-w/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.menuBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.LeftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(2)

        self.verticalLayout_4.addWidget(self.label)

        self.RTbtn1 = QPushButton(self.frame_2)
        self.RTbtn1.setObjectName(u"RTbtn1")
        font1 = QFont()
        font1.setPointSize(10)
        self.RTbtn1.setFont(font1)
        self.RTbtn1.setStyleSheet(u"background-color:#1f232a;")
        self.RTbtn1.setIcon(icon)
        self.RTbtn1.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.RTbtn1)

        self.RTbtn2 = QPushButton(self.frame_2)
        self.RTbtn2.setObjectName(u"RTbtn2")
        self.RTbtn2.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons-w/Icons-w/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RTbtn2.setIcon(icon1)
        self.RTbtn2.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.RTbtn2)

        self.RTbtn3 = QPushButton(self.frame_2)
        self.RTbtn3.setObjectName(u"RTbtn3")
        self.RTbtn3.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons-w/Icons-w/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RTbtn3.setIcon(icon2)
        self.RTbtn3.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.RTbtn3)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.LeftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(2)

        self.verticalLayout_5.addWidget(self.label_2)

        self.OFFbtn1 = QPushButton(self.frame_3)
        self.OFFbtn1.setObjectName(u"OFFbtn1")
        self.OFFbtn1.setFont(font1)
        self.OFFbtn1.setIcon(icon)
        self.OFFbtn1.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.OFFbtn1)

        self.OFFbtn2 = QPushButton(self.frame_3)
        self.OFFbtn2.setObjectName(u"OFFbtn2")
        self.OFFbtn2.setFont(font1)
        self.OFFbtn2.setIcon(icon1)
        self.OFFbtn2.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.OFFbtn2)

        self.OFFbtn3 = QPushButton(self.frame_3)
        self.OFFbtn3.setObjectName(u"OFFbtn3")
        self.OFFbtn3.setFont(font1)
        self.OFFbtn3.setIcon(icon2)
        self.OFFbtn3.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.OFFbtn3)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_4 = QFrame(self.LeftMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.frame_4)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons-w/Icons-w/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon3)
        self.homeButton.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.homeButton)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.LeftMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.LeftMenuContainer)

        self.MainBodyContainer = QWidget(self.centralwidget)
        self.MainBodyContainer.setObjectName(u"MainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainBodyContainer.sizePolicy().hasHeightForWidth())
        self.MainBodyContainer.setSizePolicy(sizePolicy1)
        self.MainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.MainBodyContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.MainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_3 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 5, 0)

        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_4)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.headerContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minBtn = QPushButton(self.frame_8)
        self.minBtn.setObjectName(u"minBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons-w/Icons-w/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minBtn.setIcon(icon4)
        self.minBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.minBtn)

        self.expBtn = QPushButton(self.frame_8)
        self.expBtn.setObjectName(u"expBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons-w/Icons-w/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.expBtn.setIcon(icon5)
        self.expBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.expBtn)

        self.closeBtn = QPushButton(self.frame_8)
        self.closeBtn.setObjectName(u"closeBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons-w/Icons-w/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon6)
        self.closeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_3.addWidget(self.frame_8, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.headerContainer)

        self.contentContainer = QWidget(self.MainBodyContainer)
        self.contentContainer.setObjectName(u"contentContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.contentContainer.sizePolicy().hasHeightForWidth())
        self.contentContainer.setSizePolicy(sizePolicy2)
        self.verticalLayout_12 = QVBoxLayout(self.contentContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(2, 2, 2, 2)
        self.mainPages = QStackedWidget(self.contentContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.home_sprite = QWidget()
        self.home_sprite.setObjectName(u"home_sprite")
        self.verticalLayout_19 = QVBoxLayout(self.home_sprite)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.home_sprite)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_13.setFont(font3)
        self.label_13.setPixmap(QPixmap(u"D:/OneDrive/Pictures/rm218-bb-07.jpg"))
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_13)

        self.mainPages.addWidget(self.home_sprite)
        self.rt_stream = QWidget()
        self.rt_stream.setObjectName(u"rt_stream")
        self.verticalLayout_13 = QVBoxLayout(self.rt_stream)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.rt_stream)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_7, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.rt_stream)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.frame_5)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.AvStreams = QTableWidget(self.groupBox)
        if (self.AvStreams.columnCount() < 4):
            self.AvStreams.setColumnCount(4)
        font4 = QFont()
        font4.setPointSize(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.AvStreams.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.AvStreams.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.AvStreams.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.AvStreams.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.AvStreams.setObjectName(u"AvStreams")
        self.AvStreams.setShowGrid(False)
        self.AvStreams.setCornerButtonEnabled(False)
        self.AvStreams.horizontalHeader().setHighlightSections(False)
        self.AvStreams.horizontalHeader().setStretchLastSection(True)
        self.AvStreams.verticalHeader().setCascadingSectionResizes(False)

        self.horizontalLayout_11.addWidget(self.AvStreams)

        self.frame_11 = QFrame(self.groupBox)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 10, 0, 10)
        self.refrStreamList = QPushButton(self.frame_11)
        self.refrStreamList.setObjectName(u"refrStreamList")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.refrStreamList.sizePolicy().hasHeightForWidth())
        self.refrStreamList.setSizePolicy(sizePolicy4)
        icon7 = QIcon()
        icon7.addFile(u":/icons-w/Icons-w/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refrStreamList.setIcon(icon7)
        self.refrStreamList.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.refrStreamList, 0, Qt.AlignTop)

        self.applyStreamList = QPushButton(self.frame_11)
        self.applyStreamList.setObjectName(u"applyStreamList")
        icon8 = QIcon()
        icon8.addFile(u":/icons-w/Icons-w/check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.applyStreamList.setIcon(icon8)
        self.applyStreamList.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.applyStreamList)


        self.horizontalLayout_11.addWidget(self.frame_11)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.AvChannels = QListWidget(self.groupBox_2)
        self.AvChannels.setObjectName(u"AvChannels")

        self.horizontalLayout_12.addWidget(self.AvChannels)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cmdBtn1 = QPushButton(self.groupBox_3)
        self.cmdBtn1.setObjectName(u"cmdBtn1")
        self.cmdBtn1.setFont(font1)

        self.verticalLayout_3.addWidget(self.cmdBtn1)

        self.cmdBtn2 = QPushButton(self.groupBox_3)
        self.cmdBtn2.setObjectName(u"cmdBtn2")
        self.cmdBtn2.setFont(font1)

        self.verticalLayout_3.addWidget(self.cmdBtn2)


        self.horizontalLayout_2.addWidget(self.groupBox_3, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.frame_5)

        self.frame_10 = QFrame(self.rt_stream)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frame_10)

        self.mainPages.addWidget(self.rt_stream)
        self.rt_class = QWidget()
        self.rt_class.setObjectName(u"rt_class")
        self.verticalLayout_14 = QVBoxLayout(self.rt_class)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_8 = QLabel(self.rt_class)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_8)

        self.mainPages.addWidget(self.rt_class)
        self.rt_dunno = QWidget()
        self.rt_dunno.setObjectName(u"rt_dunno")
        self.verticalLayout_15 = QVBoxLayout(self.rt_dunno)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_9 = QLabel(self.rt_dunno)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_9)

        self.mainPages.addWidget(self.rt_dunno)
        self.off_ds = QWidget()
        self.off_ds.setObjectName(u"off_ds")
        self.verticalLayout_16 = QVBoxLayout(self.off_ds)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_10 = QLabel(self.off_ds)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setMargin(2)

        self.verticalLayout_16.addWidget(self.label_10, 0, Qt.AlignTop)

        self.frame_14 = QFrame(self.off_ds)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, 10, 10, 0)
        self.pathBox = QLineEdit(self.frame_14)
        self.pathBox.setObjectName(u"pathBox")

        self.horizontalLayout_14.addWidget(self.pathBox)

        self.resetPath = QPushButton(self.frame_14)
        self.resetPath.setObjectName(u"resetPath")
        icon9 = QIcon()
        icon9.addFile(u":/icons-w/Icons-w/refresh-ccw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resetPath.setIcon(icon9)
        self.resetPath.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.resetPath)

        self.browseBtn = QPushButton(self.frame_14)
        self.browseBtn.setObjectName(u"browseBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons-w/Icons-w/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.browseBtn.setIcon(icon10)
        self.browseBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_14.addWidget(self.browseBtn)


        self.verticalLayout_16.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.off_ds)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy2.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy2)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(10, 0, 10, 0)
        self.treeView = QTreeView(self.frame_13)
        self.treeView.setObjectName(u"treeView")

        self.horizontalLayout_13.addWidget(self.treeView)

        self.listView = QListView(self.frame_13)
        self.listView.setObjectName(u"listView")
        self.listView.setSelectionMode(QAbstractItemView.MultiSelection)

        self.horizontalLayout_13.addWidget(self.listView)


        self.verticalLayout_16.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.off_ds)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy2.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy2)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(10, 2, 10, 2)
        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.ds_contents = QTableWidget(self.frame_15)
        if (self.ds_contents.columnCount() < 4):
            self.ds_contents.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ds_contents.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ds_contents.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ds_contents.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.ds_contents.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.ds_contents.setObjectName(u"ds_contents")
        self.ds_contents.setColumnCount(4)

        self.horizontalLayout_16.addWidget(self.ds_contents)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_16)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 10, 0, 10)
        self.resContentSelect = QPushButton(self.frame_16)
        self.resContentSelect.setObjectName(u"resContentSelect")
        self.resContentSelect.setIcon(icon9)
        self.resContentSelect.setIconSize(QSize(22, 22))

        self.verticalLayout_9.addWidget(self.resContentSelect, 0, Qt.AlignTop)

        self.appContentSelect = QPushButton(self.frame_16)
        self.appContentSelect.setObjectName(u"appContentSelect")
        self.appContentSelect.setIcon(icon8)
        self.appContentSelect.setIconSize(QSize(22, 22))

        self.verticalLayout_9.addWidget(self.appContentSelect)


        self.horizontalLayout_16.addWidget(self.frame_16)


        self.horizontalLayout_15.addWidget(self.frame_15)

        self.listWidget = QListWidget(self.frame_12)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout_15.addWidget(self.listWidget)


        self.verticalLayout_16.addWidget(self.frame_12)

        self.mainPages.addWidget(self.off_ds)
        self.off_model = QWidget()
        self.off_model.setObjectName(u"off_model")
        self.verticalLayout_17 = QVBoxLayout(self.off_model)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_11 = QLabel(self.off_model)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)

        self.mainPages.addWidget(self.off_model)
        self.off_dunno = QWidget()
        self.off_dunno.setObjectName(u"off_dunno")
        self.verticalLayout_18 = QVBoxLayout(self.off_dunno)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_12 = QLabel(self.off_dunno)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_12)

        self.mainPages.addWidget(self.off_dunno)

        self.verticalLayout_12.addWidget(self.mainPages)


        self.verticalLayout_7.addWidget(self.contentContainer)

        self.extraContainer = QCustomSlideMenu(self.MainBodyContainer)
        self.extraContainer.setObjectName(u"extraContainer")
        self.extraContainer.setMaximumSize(QSize(16777215, 120))
        self.extraContainer.setFont(font4)
        self.verticalLayout_20 = QVBoxLayout(self.extraContainer)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.extraSubContainer = QWidget(self.extraContainer)
        self.extraSubContainer.setObjectName(u"extraSubContainer")
        self.verticalLayout_21 = QVBoxLayout(self.extraSubContainer)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.extraHeader = QFrame(self.extraSubContainer)
        self.extraHeader.setObjectName(u"extraHeader")
        self.extraHeader.setFrameShape(QFrame.StyledPanel)
        self.extraHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.extraHeader)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.extraHeader)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_14)

        self.pushButton_2 = QPushButton(self.extraHeader)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.extraHeader)

        self.extraContent = QWidget(self.extraSubContainer)
        self.extraContent.setObjectName(u"extraContent")
        self.verticalLayout_22 = QVBoxLayout(self.extraContent)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 0, 5, 0)
        self.logList = QListWidget(self.extraContent)
        self.logList.setObjectName(u"logList")
        self.logList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.logList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.logList.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.logList)


        self.verticalLayout_21.addWidget(self.extraContent)


        self.verticalLayout_20.addWidget(self.extraSubContainer)


        self.verticalLayout_7.addWidget(self.extraContainer, 0, Qt.AlignBottom)

        self.footerContainer = QWidget(self.MainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_7 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.footerContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_6)


        self.horizontalLayout_7.addWidget(self.frame_9)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(25, 25))
        self.sizeGrip.setMaximumSize(QSize(25, 25))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.sizeGrip)


        self.verticalLayout_7.addWidget(self.footerContainer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.MainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Real Time", None))
#if QT_CONFIG(tooltip)
        self.RTbtn1.setToolTip(QCoreApplication.translate("MainWindow", u"Stream", None))
#endif // QT_CONFIG(tooltip)
        self.RTbtn1.setText(QCoreApplication.translate("MainWindow", u"Stream", None))
#if QT_CONFIG(tooltip)
        self.RTbtn2.setToolTip(QCoreApplication.translate("MainWindow", u"Classifier", None))
#endif // QT_CONFIG(tooltip)
        self.RTbtn2.setText(QCoreApplication.translate("MainWindow", u"Classifier", None))
#if QT_CONFIG(tooltip)
        self.RTbtn3.setToolTip(QCoreApplication.translate("MainWindow", u"RT-Undecided", None))
#endif // QT_CONFIG(tooltip)
        self.RTbtn3.setText(QCoreApplication.translate("MainWindow", u"Undecided", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"OffLine", None))
#if QT_CONFIG(tooltip)
        self.OFFbtn1.setToolTip(QCoreApplication.translate("MainWindow", u"Dataset", None))
#endif // QT_CONFIG(tooltip)
        self.OFFbtn1.setText(QCoreApplication.translate("MainWindow", u"Dataset", None))
#if QT_CONFIG(tooltip)
        self.OFFbtn2.setToolTip(QCoreApplication.translate("MainWindow", u"Model", None))
#endif // QT_CONFIG(tooltip)
        self.OFFbtn2.setText(QCoreApplication.translate("MainWindow", u"Model", None))
#if QT_CONFIG(tooltip)
        self.OFFbtn3.setToolTip(QCoreApplication.translate("MainWindow", u"Off-Undecided", None))
#endif // QT_CONFIG(tooltip)
        self.OFFbtn3.setText(QCoreApplication.translate("MainWindow", u"Undecided", None))
#if QT_CONFIG(tooltip)
        self.homeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Bottom", None))
#endif // QT_CONFIG(tooltip)
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Title", None))
#if QT_CONFIG(tooltip)
        self.minBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minBtn.setText("")
#if QT_CONFIG(tooltip)
        self.expBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Resize Window", None))
#endif // QT_CONFIG(tooltip)
        self.expBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_13.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"RT-Stream", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.AvStreams.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Stream Name(s)", None));
        ___qtablewidgetitem1 = self.AvStreams.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Signal(s)", None));
        ___qtablewidgetitem2 = self.AvStreams.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Marker(s)", None));
        ___qtablewidgetitem3 = self.AvStreams.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Info", None));
#if QT_CONFIG(tooltip)
        self.refrStreamList.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.refrStreamList.setText("")
        self.applyStreamList.setText("")
        self.groupBox_2.setTitle("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Commands", None))
        self.cmdBtn1.setText(QCoreApplication.translate("MainWindow", u"Plot Signal", None))
        self.cmdBtn2.setText(QCoreApplication.translate("MainWindow", u"Pre - Process", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"RT-Classifier", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"RT-Undecided", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"OFF-Dataset", None))
#if QT_CONFIG(tooltip)
        self.resetPath.setToolTip(QCoreApplication.translate("MainWindow", u"Reset", None))
#endif // QT_CONFIG(tooltip)
        self.resetPath.setText("")
#if QT_CONFIG(tooltip)
        self.browseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Browse", None))
#endif // QT_CONFIG(tooltip)
        self.browseBtn.setText("")
        ___qtablewidgetitem4 = self.ds_contents.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Name(s)", None));
        ___qtablewidgetitem5 = self.ds_contents.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Shape(s)", None));
        ___qtablewidgetitem6 = self.ds_contents.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Signal(s)", None));
        ___qtablewidgetitem7 = self.ds_contents.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Labels", None));
#if QT_CONFIG(tooltip)
        self.resContentSelect.setToolTip(QCoreApplication.translate("MainWindow", u"Reset", None))
#endif // QT_CONFIG(tooltip)
        self.resContentSelect.setText("")
#if QT_CONFIG(tooltip)
        self.appContentSelect.setToolTip(QCoreApplication.translate("MainWindow", u"Apply", None))
#endif // QT_CONFIG(tooltip)
        self.appContentSelect.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"OFF-Model", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"OFF-Undecided", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Extra Window", None))
        self.pushButton_2.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Footer Text", None))
    # retranslateUi

