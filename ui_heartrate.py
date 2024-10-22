######################################################################################################################################################################
###  UI HEART RATE                                                      ##############################################################################################
###  AUTHOR: FEBRI PRASETIYO                                            ##############################################################################################
######################################################################################################################################################################


######################################################################################################################################################################
###  LIBRARY IMPORT
######################################################################################################################################################################
import pandas as pd
import datetime
import time
import sys
import pyqtgraph as pg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5.QtGui import QIcon, QColor
import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QEventLoop


######################################################################################################################################################################
###  GUI CLASS
######################################################################################################################################################################
class Ui_MainWindow(object):

    ##################################################################################################################################################################
    ###  GUI SET-UP
    ##################################################################################################################################################################
    def setupUi(self, MainWindow):

        ###  Untuk menampilkan frame utama
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1096, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        ###  Untuk mengatur style GUI (contoh: warna teks, radius, warna backround, dll)
        self.centralwidget.setStyleSheet("*{\n"
        "    color:#000;\n"
        "    border:none;\n"
        "\n"
        "}\n"
        "#centralwidget{\n"
        "    background-color:#e1f9fe;\n"
        "}\n"
        "\n"
        "#frameHome{\n"
        "    background-color:#2596be;\n"
        "}\n"
        "\n"
        "QLineEdit{\n"
        "    background: transparent;\n"
        "    color:#2596be;\n"
        "}\n"
        "\n"
        "#searchFrame{\n"
        "    border-radius: 10px;\n"
        "    border: 2px solid #2596be;\n"
        "}\n"
        "\n"
        "#dashLabel, #bpmLabel{\n"
        "    color: #2596be;\n"
        "}\n"
        "\n"
        "#card1, #card2, #card3, #card4{\n"
        "    background-color: #fefeff;\n"
        "    border-radius: 20px;\n"
        "}\n"
        "\n"
        "#textEdit{\n"
        "    border-radius: 20px;\n"
        "}\n"
        "\n"
        "#profileCont, #frameProfile, #pushButton{\n"
        "    background-color: #fefeff;\n"
        "    border-radius: 20px;\n"
        "}\n"
        "\n"
        "#homeButton{\n"
        "    background-color: #fefeff;\n"
        "    padding: 10px 5px;\n"
        "    text-align: left;\n"
        "    border-top-left-radius: 20px;\n"
        "}\n"
        "\n"
        "QPushButton{\n"
        "    padding: 10px 5px;\n"
        "    text-align: left;\n"
        "}")

        ###  Mengatur central widget
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        ###  Mengatur menu samping kiri
        self.leftMenu = QtWidgets.QWidget(self.centralwidget)
        self.leftMenu.setMinimumSize(QtCore.QSize(195, 0))
        self.leftMenu.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        ###  Mengatur frame menu home utama
        self.frameHome = QtWidgets.QFrame(self.leftMenu)
        self.frameHome.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHome.setObjectName("frameHome")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameHome)
        self.verticalLayout_3.setContentsMargins(0, 0, 15, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        ###  Mengatur frame HEART RATE GUI
        self.frameGui = QtWidgets.QFrame(self.frameHome)
        self.frameGui.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameGui.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameGui.setObjectName("frameGui")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frameGui)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelGui = QtWidgets.QLabel(self.frameGui)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        ###  Mengatur label nama HEART RATE GUI
        self.labelGui.setFont(font)
        self.labelGui.setObjectName("labelGui")
        self.horizontalLayout_7.addWidget(self.labelGui, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.frameGui, 0, QtCore.Qt.AlignTop)

        ###  Mengatur frame home ke-1
        self.frame_1 = QtWidgets.QFrame(self.frameHome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_1.sizePolicy().hasHeightForWidth())
        self.frame_1.setSizePolicy(sizePolicy)
        self.frame_1.setMinimumSize(QtCore.QSize(195, 0))
        self.frame_1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        ###  Mengatur frame home ke-2
        self.frame_2 = QtWidgets.QFrame(self.frame_1)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        ###  Mengatur push button home
        self.homeButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.homeButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/blue_icon/blue_icon/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QtCore.QSize(24, 24))
        self.homeButton.setObjectName("homeButton")
        self.verticalLayout_6.addWidget(self.homeButton)
        self.verticalLayout_7.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.frame_1)
        self.verticalLayout_2.addWidget(self.frameHome)
        self.horizontalLayout.addWidget(self.leftMenu)

        ###  Mengatur widget untuk menu dashboard utama
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setAcceptDrops(False)
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBody)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QWidget(self.mainBody)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.headerFrame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        ###  Mengatur push button menu dashboard
        self.menuButton = QtWidgets.QPushButton(self.widget)
        self.menuButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/blue_icon/blue_icon/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton.setIcon(icon1)
        self.menuButton.setIconSize(QtCore.QSize(35, 35))
        self.menuButton.setObjectName("menuButton")
        self.horizontalLayout_4.addWidget(self.menuButton)

        ###  Mengatur label dashboard
        self.dashLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.dashLabel.setFont(font)
        self.dashLabel.setObjectName("dashLabel")
        self.horizontalLayout_4.addWidget(self.dashLabel)
        self.horizontalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignLeft)
        self.widget_2 = QtWidgets.QWidget(self.headerFrame)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        ###  Mengatur frame search
        self.searchFrame = QtWidgets.QFrame(self.widget_2)
        self.searchFrame.setMinimumSize(QtCore.QSize(160, 0))
        self.searchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchFrame.setObjectName("searchFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.searchFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        ### Mengatur icon search
        self.searchIcon = QtWidgets.QLabel(self.searchFrame)
        self.searchIcon.setMinimumSize(QtCore.QSize(30, 30))
        self.searchIcon.setMaximumSize(QtCore.QSize(30, 30))
        self.searchIcon.setText("")
        self.searchIcon.setPixmap(QtGui.QPixmap(":/blue_icon/blue_icon/search.svg"))
        self.searchIcon.setObjectName("searchIcon")
        self.horizontalLayout_3.addWidget(self.searchIcon)

        ###  Mengatur text pada kolom search
        self.searchHere = QtWidgets.QLineEdit(self.searchFrame)
        self.searchHere.setObjectName("searchHere")
        self.horizontalLayout_3.addWidget(self.searchHere)
        self.horizontalLayout_5.addWidget(self.searchFrame)
        self.horizontalLayout_2.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter)
        self.widget_3 = QtWidgets.QWidget(self.headerFrame)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        ###  Mengatur label untuk menampilkan output heart rate
        self.bpmLabel = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.bpmLabel.setFont(font)
        self.bpmLabel.setObjectName("bpmLabel")
        self.horizontalLayout_6.addWidget(self.bpmLabel)

        ### Mengatur icon heart rate
        self.heartIcon = QtWidgets.QPushButton(self.widget_3)
        self.heartIcon.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/blue_icon/blue_icon/heart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.heartIcon.setIcon(icon2)
        self.heartIcon.setIconSize(QtCore.QSize(35, 35))
        self.heartIcon.setObjectName("heartIcon")
        self.horizontalLayout_6.addWidget(self.heartIcon)
        self.horizontalLayout_2.addWidget(self.widget_3, 0, QtCore.Qt.AlignRight)
        self.widget.raise_()
        self.widget_3.raise_()
        self.widget_2.raise_()
        self.verticalLayout.addWidget(self.headerFrame, 0, QtCore.Qt.AlignTop)

        ### Mengatur frame untuk output dari pemrosesan data input (proses_input)
        self.cardsFrame = QtWidgets.QFrame(self.mainBody)
        self.cardsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cardsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cardsFrame.setObjectName("cardsFrame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.cardsFrame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        ###  Mengatur frame untuk detik
        self.card1 = QtWidgets.QFrame(self.cardsFrame)
        self.card1.setMinimumSize(QtCore.QSize(160, 0))
        self.card1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card1.setObjectName("card1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.card1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_3 = QtWidgets.QFrame(self.card1)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

        ###  Mengatur label untuk detik
        self.detikLabel = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.detikLabel.setFont(font)
        self.detikLabel.setObjectName("detikLabel")
        self.horizontalLayout_9.addWidget(self.detikLabel)

        ###  Mengatur icon detik
        self.clockIcon = QtWidgets.QLabel(self.frame_3)
        self.clockIcon.setMaximumSize(QtCore.QSize(40, 40))
        self.clockIcon.setText("")
        self.clockIcon.setPixmap(QtGui.QPixmap(":/blue_icon/blue_icon/clock.svg"))
        self.clockIcon.setScaledContents(True)
        self.clockIcon.setObjectName("clockIcon")
        self.horizontalLayout_9.addWidget(self.clockIcon, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_8.addWidget(self.frame_3, 0, QtCore.Qt.AlignTop)

        ###  Mengatur label untuk menampilkan output detik
        self.none1 = QtWidgets.QLabel(self.card1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.none1.setFont(font)
        self.none1.setObjectName("none1")
        self.verticalLayout_8.addWidget(self.none1, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_8.addWidget(self.card1)

        ###  Mengatur frame untuk umur
        self.card2 = QtWidgets.QFrame(self.cardsFrame)
        self.card2.setMinimumSize(QtCore.QSize(160, 0))
        self.card2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card2.setObjectName("card2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.card2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_4 = QtWidgets.QFrame(self.card2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        ###  Mengatur label untuk umur
        self.umurLabel = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.umurLabel.setFont(font)
        self.umurLabel.setObjectName("umurLabel")
        self.horizontalLayout_10.addWidget(self.umurLabel)

        ###  Mengatur icon umur
        self.umurIcon = QtWidgets.QLabel(self.frame_4)
        self.umurIcon.setMaximumSize(QtCore.QSize(40, 40))
        self.umurIcon.setText("")
        self.umurIcon.setPixmap(QtGui.QPixmap(":/blue_icon/blue_icon/users.svg"))
        self.umurIcon.setScaledContents(True)
        self.umurIcon.setObjectName("umurIcon")
        self.horizontalLayout_10.addWidget(self.umurIcon, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_11.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)

        ###  Mengatur label untuk menampilkan output umur dari input user
        self.none2 = QtWidgets.QLabel(self.card2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.none2.setFont(font)
        self.none2.setObjectName("none2")
        self.verticalLayout_11.addWidget(self.none2, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_8.addWidget(self.card2)

        ###  Mengatur frame untuk persentase
        self.card3 = QtWidgets.QFrame(self.cardsFrame)
        self.card3.setMinimumSize(QtCore.QSize(160, 0))
        self.card3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card3.setObjectName("card3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.card3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_5 = QtWidgets.QFrame(self.card3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        ###  Mengatur label untuk persentase
        self.persenLabel = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.persenLabel.setFont(font)
        self.persenLabel.setObjectName("persenLabel")
        self.horizontalLayout_11.addWidget(self.persenLabel)

        ###  Mengatur icon persentase
        self.persenIcon = QtWidgets.QLabel(self.frame_5)
        self.persenIcon.setMaximumSize(QtCore.QSize(40, 40))
        self.persenIcon.setText("")
        self.persenIcon.setPixmap(QtGui.QPixmap(":/blue_icon/blue_icon/percent.svg"))
        self.persenIcon.setScaledContents(True)
        self.persenIcon.setObjectName("persenIcon")
        self.horizontalLayout_11.addWidget(self.persenIcon, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_10.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)

        ###  Mengatur label untuk menampilkan output persentase
        self.none3 = QtWidgets.QLabel(self.card3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.none3.setFont(font)
        self.none3.setObjectName("none3")
        self.verticalLayout_10.addWidget(self.none3, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_8.addWidget(self.card3)

        ###  Mengatur frame untuk intensitas
        self.card4 = QtWidgets.QFrame(self.cardsFrame)
        self.card4.setMinimumSize(QtCore.QSize(160, 0))
        self.card4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card4.setObjectName("card4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.card4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_6 = QtWidgets.QFrame(self.card4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")

        ###  Mengatur label untuk intensitas
        self.intensLabel = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.intensLabel.setFont(font)
        self.intensLabel.setObjectName("intensLabel")
        self.horizontalLayout_12.addWidget(self.intensLabel)

        ###  Mengatur icon intensitas
        self.intensIcon = QtWidgets.QLabel(self.frame_6)
        self.intensIcon.setMaximumSize(QtCore.QSize(40, 40))
        self.intensIcon.setText("")
        self.intensIcon.setPixmap(QtGui.QPixmap(":/blue_icon/blue_icon/trending-up.svg"))
        self.intensIcon.setScaledContents(True)
        self.intensIcon.setObjectName("intensIcon")
        self.horizontalLayout_12.addWidget(self.intensIcon, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_9.addWidget(self.frame_6, 0, QtCore.Qt.AlignTop)

        ###  Mengatur label untuk menampilkan output intensitas
        self.none4 = QtWidgets.QLabel(self.card4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.none4.setFont(font)
        self.none4.setObjectName("none4")
        self.verticalLayout_9.addWidget(self.none4, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_8.addWidget(self.card4)
        self.verticalLayout.addWidget(self.cardsFrame)

        ###  Mengatur frame utama untuk input user dan grafik plot
        self.mainFrame = QtWidgets.QWidget(self.mainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.widget_4 = QtWidgets.QWidget(self.mainFrame)
        self.widget_4.setObjectName("widget_4")

        ###  Mengatur frame untuk input user
        self.frame = QtWidgets.QFrame(self.widget_4)
        self.frame.setGeometry(QtCore.QRect(0, 0, 651, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")

        ###  Mengatur textbox untuk input user
        self.inputUmur = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.inputUmur.setFont(font)
        self.inputUmur.setAutoFillBackground(False)
        self.inputUmur.setOverwriteMode(False)
        self.inputUmur.setObjectName("inputUmur")
        self.horizontalLayout_14.addWidget(self.inputUmur)

        ###  Mengatur push button untuk input user
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.proses_input)
        self.horizontalLayout_14.addWidget(self.pushButton)

        ###  Mengatur grafik plot
        self.plot_widget = pg.PlotWidget(self.widget_4)
        self.plot_widget.setGeometry(QtCore.QRect(10, 70, 631, 361))
        self.plot_widget.setObjectName("plot_widget")
        self.plot_widget.setBackground("white")
        self.plot_widget.plotItem.setDownsampling(mode='peak')
        self.plot_widget.plotItem.setClipToView(True)
        self.plot_data = self.plot_widget.plot(pen='r', width='2')
        self.horizontalLayout_13.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.mainFrame)
        self.horizontalLayout.addWidget(self.mainBody)

        ###  Mengatur widget untuk frame profile
        self.profileCont = QtWidgets.QWidget(self.centralwidget)
        self.profileCont.setObjectName("profileCont")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.profileCont)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        ###  Mengatur frame profile
        self.frameProfile = QtWidgets.QFrame(self.profileCont)
        self.frameProfile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameProfile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameProfile.setObjectName("frameProfile")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameProfile)
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 465)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        ###  Mengatur label untuk nama kelompok
        self.kel2Label = QtWidgets.QLabel(self.frameProfile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kel2Label.setFont(font)
        self.kel2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.kel2Label.setObjectName("kel2Label")

        ###  Mengatur label mata kuliah
        self.verticalLayout_5.addWidget(self.kel2Label)
        self.alprogLabel = QtWidgets.QLabel(self.frameProfile)
        self.alprogLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.alprogLabel.setObjectName("alprogLabel")
        self.verticalLayout_5.addWidget(self.alprogLabel)

        ###  Mengatur gambar kucing pada profile menu
        self.catIcon = QtWidgets.QLabel(self.frameProfile)
        self.catIcon.setMinimumSize(QtCore.QSize(60, 60))
        self.catIcon.setMaximumSize(QtCore.QSize(60, 60))
        self.catIcon.setText("")
        self.catIcon.setPixmap(QtGui.QPixmap("cat.png"))
        self.catIcon.setScaledContents(True)
        self.catIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.catIcon.setObjectName("catIcon")
        self.verticalLayout_5.addWidget(self.catIcon, 0, QtCore.Qt.AlignHCenter)
        self.myprofileBtn = QtWidgets.QPushButton(self.frameProfile)

        ###  Mengatur icon user my profile
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/blue_icon/blue_icon/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.myprofileBtn.setIcon(icon3)
        self.myprofileBtn.setObjectName("myprofileBtn")
        self.verticalLayout_5.addWidget(self.myprofileBtn)
        self.logoutBtn = QtWidgets.QPushButton(self.frameProfile)

        ###  Mengatur icon logout pada menu profile
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/blue_icon/blue_icon/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoutBtn.setIcon(icon4)
        self.logoutBtn.setObjectName("logoutBtn")
        self.verticalLayout_5.addWidget(self.logoutBtn)
        self.verticalLayout_4.addWidget(self.frameProfile)
        self.horizontalLayout.addWidget(self.profileCont, 0, QtCore.Qt.AlignTop)

        ###  konfigurasi dan inisialisasi
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ###  Mengatur interval timer
        self.timer = QTimer(MainWindow)
        self.timer.start(1000)
        self.seconds = 0  # variabel untuk menyimpan nilai detik

        ###  Pembacaan file csv
        self.bpm_values = []
        self.df = pd.read_csv('data.csv')
        self.df = self.df.drop(self.df.columns[2:], axis=1)
        self.df = self.df[self.df['BPM'] != 0]


    ######################################################################################################################################################################
    ###  LABEL NAME
    ######################################################################################################################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HEART RATE UI"))
        self.labelGui.setText(_translate("MainWindow", "HEART RATE"))
        self.homeButton.setText(_translate("MainWindow", "Home"))
        self.dashLabel.setText(_translate("MainWindow", "Dashboard"))
        self.searchHere.setPlaceholderText(_translate("MainWindow", "Search here"))
        self.bpmLabel.setText(_translate("MainWindow", "None"))
        self.detikLabel.setText(_translate("MainWindow", "Second"))
        self.none1.setText(_translate("MainWindow", "None"))
        self.umurLabel.setText(_translate("MainWindow", "Age"))
        self.none2.setText(_translate("MainWindow", "None"))
        self.persenLabel.setText(_translate("MainWindow", "Percentage"))
        self.none3.setText(_translate("MainWindow", "None"))
        self.intensLabel.setText(_translate("MainWindow", "Intensity"))
        self.none4.setText(_translate("MainWindow", "None"))
        self.inputUmur.setAccessibleName(_translate("MainWindow", "search"))
        self.inputUmur.setAccessibleDescription(_translate("MainWindow", "<html><head/><body><p>search</p></body></html>"))
        self.inputUmur.setPlaceholderText(_translate("MainWindow", "Input your age"))
        self.pushButton.setText(_translate("MainWindow", "  OK  "))
        self.kel2Label.setText(_translate("MainWindow", "febrilym"))
        self.alprogLabel.setText(_translate("MainWindow", "Data Engineer"))
        self.myprofileBtn.setText(_translate("MainWindow", "My Profile"))
        self.logoutBtn.setText(_translate("MainWindow", "Logout"))


    ######################################################################################################################################################################
    ###  DATA PROCESSING
    ######################################################################################################################################################################
    def proses_input(self):

        ###  Dapatkan umur dari input
        umur_input = int(self.inputUmur.toPlainText())

        ###  Hitung HR Max
        hrMax = 220 - umur_input

        ###  Menghitung dan membatasi Presentase_HR_Max menjadi 2 angka dibelakang koma
        self.df['Presentase_HR_Max'] = (self.df['BPM'] / hrMax) * 100
        self.df['Presentase_HR_Max'] = self.df['Presentase_HR_Max'].apply('{:.2f}'.format)
        self.df['Intensitas_Olahraga'] = self.df['Presentase_HR_Max'].apply(self.intens_olrg)

        ###  Simpan umur ke label
        self.none2.setText(f"{umur_input}")

        ###  Membuat DataFrame baru untuk menyimpan data yang diproses
        output_df = pd.DataFrame(columns=['Seconds', 'BPM', 'Presentase_HR_Max', 'Intensitas_Olahraga'])
        waktu = datetime.datetime.now()
        new_file_name = f'{waktu.strftime("%d.%m.%Y_%H.%M.%S")}.csv'
        self.df.to_csv(new_file_name, index=False)
        
        ###  Iterasi melalui setiap baris dan update label sesuai detik
        for index, row in self.df.iterrows():
            detik = row['Seconds']
            bpm = row['BPM']
            presentase_hr_max = row['Presentase_HR_Max']
            intens = row['Intensitas_Olahraga']

            ###  Atur label sesuai detik, BPM, dan Presentase_HR_Max
            self.none1.setText(f"{detik}")
            self.bpmLabel.setText(f"{bpm}")
            self.none3.setText(f"{presentase_hr_max}%")
            self.none4.setText(f"{intens}")
            y_values = pd.to_numeric(self.df['Presentase_HR_Max'][:index + 1].tolist())
            self.plot_data.setData(self.df['Seconds'][:index + 1].tolist(), y_values)

            ###  Delay 1 detik
            QtWidgets.QApplication.processEvents()
            loop = QEventLoop()
            QTimer.singleShot(1000, loop.quit)
            loop.exec_()

            ###  Bersihkan label setelah detik berikutnya
            self.none1.clear()
            self.bpmLabel.clear()
            self.none3.clear()
            self.none4.clear()

        ###  Perintah untuk secara otomatis menyesuaikan rentang tampilan pada widget plot agar seluruh data yang ditampilkan dapat terlihat dengan optimal   
        self.plot_widget.plotItem.getViewBox().autoRange()


    ######################################################################################################################################################################
    ###  CONDITIONING EXERCISE INTENSITY (CATEGORY)
    ######################################################################################################################################################################
    def intens_olrg(self, x):
        x = float(x)
        if 50 <= x < 60:
            return 'Very Light'
        elif 60 <= x < 70:
            return 'Light'
        elif 70 <= x < 80:
            return 'Moderate'
        elif 80 <= x < 90:
            return 'Hard'
        elif x >= 90:
            return 'Maximum'
        else:
            return 'Unknown'


##########################################################################################################################################################################
###  GUI EXECUTING PROGRAM
##########################################################################################################################################################################
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    hr_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(hr_window)
    hr_window.show()
    sys.exit(app.exec_())