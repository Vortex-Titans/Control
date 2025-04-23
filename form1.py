# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formNHDAUb.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame{\n"
"  border-radius: 0px\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QFrame(self.centralwidget)
        self.Header.setObjectName(u"Header")
        self.Header.setMinimumSize(QSize(0, 50))
        self.Header.setMaximumSize(QSize(16777215, 50))
        self.Header.setStyleSheet(u"background-color: #1c1c1c;")
        self.Header.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.Header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.navigation = QFrame(self.Header)
        self.navigation.setObjectName(u"navigation")
        self.navigation.setStyleSheet(u"QPushButton {\n"
" border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #255F38; \n"
"    border-color: #255F38; \n"
"}\n"
"")
        self.navigation.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.navigation)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sensor = QPushButton(self.navigation)
        self.sensor.setObjectName(u"sensor")
        self.sensor.setMinimumSize(QSize(100, 50))
        self.sensor.setMaximumSize(QSize(100, 50))
        self.sensor.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/icons/Sensorsmenu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.sensor.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.sensor)


        self.horizontalLayout.addWidget(self.navigation, 0, Qt.AlignmentFlag.AlignLeft)

        self.logo = QFrame(self.Header)
        self.logo.setObjectName(u"logo")
        self.logo.setStyleSheet(u" border-radius: 5px")
        self.logo.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.logo)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Titans = QLabel(self.logo)
        self.Titans.setObjectName(u"Titans")
        font = QFont()
        font.setFamilies([u"Sans Serif Collection"])
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        self.Titans.setFont(font)

        self.horizontalLayout_4.addWidget(self.Titans, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.logo)

        self.buttons = QFrame(self.Header)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setStyleSheet(u" border-radius: 5px")
        self.buttons.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.buttons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize = QPushButton(self.buttons)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(50, 50))
        self.minimize.setMaximumSize(QSize(50, 50))
        self.minimize.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: rgba(217, 217, 217, 0.3);\n"
"    border-color: rgba(217, 217, 217, 0.3);\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/chevron-down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.minimize.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.minimize)

        self.maximize = QPushButton(self.buttons)
        self.maximize.setObjectName(u"maximize")
        self.maximize.setMinimumSize(QSize(50, 50))
        self.maximize.setMaximumSize(QSize(50, 50))
        self.maximize.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: rgba(217, 217, 217, 0.3);\n"
"    border-color: rgba(217, 217, 217, 0.3);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/icons/maximize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.maximize.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.maximize)

        self.xbutton = QPushButton(self.buttons)
        self.xbutton.setObjectName(u"xbutton")
        self.xbutton.setMinimumSize(QSize(50, 50))
        self.xbutton.setMaximumSize(QSize(50, 50))
        self.xbutton.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: #7D0A0A; \n"
"    border-color: #FFB86C;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/icons/x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.xbutton.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.xbutton)


        self.horizontalLayout.addWidget(self.buttons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.Header)

        self.Body = QFrame(self.centralwidget)
        self.Body.setObjectName(u"Body")
        self.Body.setStyleSheet(u"background-color:#141414;")
        self.Body.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.Body)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.sensors = QFrame(self.Body)
        self.sensors.setObjectName(u"sensors")
        self.sensors.setMinimumSize(QSize(100, 0))
        self.sensors.setMaximumSize(QSize(100, 16777215))
        self.sensors.setStyleSheet(u"background-color:  #2e2e2e;")
        self.sensors.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.sensors)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.CameraMode = QFrame(self.sensors)
        self.CameraMode.setObjectName(u"CameraMode")
        self.CameraMode.setMaximumSize(QSize(100, 50))
        self.CameraMode.setStyleSheet(u" border-radius: 5px")
        self.CameraMode.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.CameraMode)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Onecamera = QPushButton(self.CameraMode)
        self.Onecamera.setObjectName(u"Onecamera")
        self.Onecamera.setMinimumSize(QSize(0, 50))
        self.Onecamera.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: rgba(217, 217, 217, 0.3);\n"
"    border-color: rgba(217, 217, 217, 0.3);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/icons/camera.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Onecamera.setIcon(icon4)

        self.horizontalLayout_9.addWidget(self.Onecamera)

        self.Fourcameras = QPushButton(self.CameraMode)
        self.Fourcameras.setObjectName(u"Fourcameras")
        self.Fourcameras.setMinimumSize(QSize(0, 50))
        self.Fourcameras.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: rgba(217, 217, 217, 0.3);\n"
"    border-color: rgba(217, 217, 217, 0.3);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/icons/plus-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Fourcameras.setIcon(icon5)

        self.horizontalLayout_9.addWidget(self.Fourcameras)


        self.verticalLayout_3.addWidget(self.CameraMode)

        self.Readings = QFrame(self.sensors)
        self.Readings.setObjectName(u"Readings")
        self.Readings.setMaximumSize(QSize(100, 16777215))
        self.Readings.setStyleSheet(u"background-color: rgba(121, 121, 121, 150);")
        self.Readings.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.Readings)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.Readings)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"border-radius: 0px\n"
"")
        self.nosocket = QWidget()
        self.nosocket.setObjectName(u"nosocket")
        self.frame = QFrame(self.nosocket)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 100, 831))
        self.frame.setMinimumSize(QSize(100, 831))
        self.frame.setMaximumSize(QSize(100, 831))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/Icons/icons/alert-triangle.svg"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.stackedWidget.addWidget(self.nosocket)
        self.socket = QWidget()
        self.socket.setObjectName(u"socket")
        self.socket.setStyleSheet(u"background-color: rgba(121, 121, 121, 150);")
        self.verticalLayout_9 = QVBoxLayout(self.socket)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.PHFrame = QFrame(self.socket)
        self.PHFrame.setObjectName(u"PHFrame")
        self.PHFrame.setMinimumSize(QSize(0, 100))
        self.PHFrame.setMaximumSize(QSize(16777215, 100))
        self.PHFrame.setStyleSheet(u"background-color: rgba(121, 121, 121, 150);")
        self.PHFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PHFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.PHFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.PHlabel = QLabel(self.PHFrame)
        self.PHlabel.setObjectName(u"PHlabel")
        self.PHlabel.setPixmap(QPixmap(u":/Icons/icons/PH.png"))
        self.PHlabel.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.PHlabel)

        self.PHValue = QLabel(self.PHFrame)
        self.PHValue.setObjectName(u"PHValue")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.PHValue.setFont(font1)
        self.PHValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.PHValue)


        self.verticalLayout_9.addWidget(self.PHFrame)

        self.PressureFrame = QFrame(self.socket)
        self.PressureFrame.setObjectName(u"PressureFrame")
        self.PressureFrame.setMinimumSize(QSize(0, 100))
        self.PressureFrame.setMaximumSize(QSize(16777215, 100))
        self.PressureFrame.setStyleSheet(u"background-color: rgba(121, 121, 121, 150);")
        self.PressureFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PressureFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.PressureFrame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.PressureLabel = QLabel(self.PressureFrame)
        self.PressureLabel.setObjectName(u"PressureLabel")
        font2 = QFont()
        font2.setBold(False)
        self.PressureLabel.setFont(font2)
        self.PressureLabel.setPixmap(QPixmap(u":/Icons/icons/Pressure.png"))
        self.PressureLabel.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.PressureLabel)

        self.PressureValue = QLabel(self.PressureFrame)
        self.PressureValue.setObjectName(u"PressureValue")
        self.PressureValue.setFont(font1)
        self.PressureValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.PressureValue)


        self.verticalLayout_9.addWidget(self.PressureFrame)

        self.IMUFrame = QFrame(self.socket)
        self.IMUFrame.setObjectName(u"IMUFrame")
        self.IMUFrame.setMinimumSize(QSize(0, 100))
        self.IMUFrame.setMaximumSize(QSize(16777215, 100))
        self.IMUFrame.setStyleSheet(u"background-color: rgba(121, 121, 121, 150);")
        self.IMUFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.IMUFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.IMUFrame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.IMUlabel = QLabel(self.IMUFrame)
        self.IMUlabel.setObjectName(u"IMUlabel")
        self.IMUlabel.setPixmap(QPixmap(u":/Icons/icons/IMU.png"))
        self.IMUlabel.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.IMUlabel)

        self.IMUValue = QLabel(self.IMUFrame)
        self.IMUValue.setObjectName(u"IMUValue")
        self.IMUValue.setFont(font1)
        self.IMUValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.IMUValue)


        self.verticalLayout_9.addWidget(self.IMUFrame)

        self.LeakageFrame = QFrame(self.socket)
        self.LeakageFrame.setObjectName(u"LeakageFrame")
        self.LeakageFrame.setMinimumSize(QSize(0, 100))
        self.LeakageFrame.setMaximumSize(QSize(16777215, 100))
        self.LeakageFrame.setStyleSheet(u"background-color: rgba(121, 121, 121, 150);")
        self.LeakageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LeakageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.LeakageFrame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.LeakageLabel = QLabel(self.LeakageFrame)
        self.LeakageLabel.setObjectName(u"LeakageLabel")
        self.LeakageLabel.setFont(font2)
        self.LeakageLabel.setPixmap(QPixmap(u":/Icons/icons/leakeage.png"))
        self.LeakageLabel.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.LeakageLabel)

        self.LeakageValue = QLabel(self.LeakageFrame)
        self.LeakageValue.setObjectName(u"LeakageValue")
        self.LeakageValue.setFont(font1)
        self.LeakageValue.setStyleSheet(u"color: rgb(0, 85, 0);")
        self.LeakageValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.LeakageValue)


        self.verticalLayout_9.addWidget(self.LeakageFrame)

        self.stackedWidget.addWidget(self.socket)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.Readings)


        self.horizontalLayout_5.addWidget(self.sensors)

        self.Cameraswidget = QStackedWidget(self.Body)
        self.Cameraswidget.setObjectName(u"Cameraswidget")
        self.fourcameras = QWidget()
        self.fourcameras.setObjectName(u"fourcameras")
        self.verticalLayout_2 = QVBoxLayout(self.fourcameras)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Camerasframe = QFrame(self.fourcameras)
        self.Camerasframe.setObjectName(u"Camerasframe")
        self.Camerasframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.Camerasframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Camerasframe)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.leftcamera = QLabel(self.Camerasframe)
        self.leftcamera.setObjectName(u"leftcamera")
        self.leftcamera.setMaximumSize(QSize(908, 880))
        self.leftcamera.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.leftcamera)

        self.rightcamera = QLabel(self.Camerasframe)
        self.rightcamera.setObjectName(u"rightcamera")
        self.rightcamera.setMaximumSize(QSize(908, 880))
        self.rightcamera.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.rightcamera)


        self.verticalLayout_2.addWidget(self.Camerasframe)

        self.Cameraswidget.addWidget(self.fourcameras)
        self.Singleecamera = QWidget()
        self.Singleecamera.setObjectName(u"Singleecamera")
        self.horizontalLayout_6 = QHBoxLayout(self.Singleecamera)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Camera = QFrame(self.Singleecamera)
        self.Camera.setObjectName(u"Camera")
        self.Camera.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(9)
        self.Camera.setFont(font3)
        self.Camera.setFrameShape(QFrame.Shape.NoFrame)
        self.cameraview = QLabel(self.Camera)
        self.cameraview.setObjectName(u"cameraview")
        self.cameraview.setGeometry(QRect(0, 0, 1831, 881))
        self.cameraview.setFont(font3)
        self.cameraview.setScaledContents(True)
        self.cameraview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cameraview.setIndent(0)

        self.horizontalLayout_6.addWidget(self.Camera)

        self.Cameraswidget.addWidget(self.Singleecamera)

        self.horizontalLayout_5.addWidget(self.Cameraswidget)


        self.verticalLayout.addWidget(self.Body)

        self.Controls = QFrame(self.centralwidget)
        self.Controls.setObjectName(u"Controls")
        self.Controls.setMinimumSize(QSize(0, 150))
        self.Controls.setMaximumSize(QSize(16777215, 150))
        self.Controls.setStyleSheet(u"")
        self.Controls.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_10 = QHBoxLayout(self.Controls)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.leftstickframe = QFrame(self.Controls)
        self.leftstickframe.setObjectName(u"leftstickframe")
        self.leftstickframe.setMinimumSize(QSize(180, 150))
        self.leftstickframe.setMaximumSize(QSize(180, 150))
        self.leftstickframe.setStyleSheet(u"background-color: #1c1c1c;")
        self.leftstickframe.setFrameShape(QFrame.Shape.NoFrame)
        self.LeftStick = QLabel(self.leftstickframe)
        self.LeftStick.setObjectName(u"LeftStick")
        self.LeftStick.setGeometry(QRect(10, 0, 161, 141))
        self.LeftStick.setStyleSheet(u"")
        self.LeftStick.setPixmap(QPixmap(u":/Icons/icons/Left Stick.png"))
        self.LeftStick.setScaledContents(True)
        self.LeftStick.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.leftstickframe)

        self.movements = QFrame(self.Controls)
        self.movements.setObjectName(u"movements")
        self.movements.setMinimumSize(QSize(300, 0))
        self.movements.setMaximumSize(QSize(200, 16777215))
        self.movements.setStyleSheet(u"background-color: #1c1c1c;")
        self.movements.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_11 = QHBoxLayout(self.movements)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Updown = QFrame(self.movements)
        self.Updown.setObjectName(u"Updown")
        self.Updown.setMinimumSize(QSize(150, 0))
        self.Updown.setFrameShape(QFrame.Shape.NoFrame)
        self.layoout = QVBoxLayout(self.Updown)
        self.layoout.setSpacing(0)
        self.layoout.setObjectName(u"layoout")
        self.layoout.setContentsMargins(0, 0, 0, 0)
        self.up = QLabel(self.Updown)
        self.up.setObjectName(u"up")
        self.up.setMinimumSize(QSize(150, 0))
        self.up.setMaximumSize(QSize(150, 16777215))
        font4 = QFont()
        font4.setPointSize(24)
        self.up.setFont(font4)
        self.up.setStyleSheet(u"border: 2px solid #2e2e2e;\n"
"background-color: rgb(28, 28, 28);")
        self.up.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layoout.addWidget(self.up)

        self.down = QLabel(self.Updown)
        self.down.setObjectName(u"down")
        self.down.setMinimumSize(QSize(150, 0))
        self.down.setMaximumSize(QSize(150, 16777215))
        self.down.setFont(font4)
        self.down.setStyleSheet(u"border: 2px solid #2e2e2e;\n"
"background-color: rgb(28, 28, 28);")
        self.down.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layoout.addWidget(self.down)


        self.horizontalLayout_11.addWidget(self.Updown)

        self.Yaw = QFrame(self.movements)
        self.Yaw.setObjectName(u"Yaw")
        self.Yaw.setMaximumSize(QSize(143, 150))
        self.Yaw.setFrameShape(QFrame.Shape.NoFrame)
        self.yaw = QLabel(self.Yaw)
        self.yaw.setObjectName(u"yaw")
        self.yaw.setGeometry(QRect(0, 0, 143, 150))
        self.yaw.setMinimumSize(QSize(143, 150))
        self.yaw.setMaximumSize(QSize(143, 20))
        self.yaw.setPixmap(QPixmap(u":/Icons/icons/YAW (1).png"))
        self.yaw.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.Yaw)


        self.horizontalLayout_10.addWidget(self.movements)

        self.gripperframe = QFrame(self.Controls)
        self.gripperframe.setObjectName(u"gripperframe")
        self.gripperframe.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_13 = QHBoxLayout(self.gripperframe)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.grippers = QFrame(self.gripperframe)
        self.grippers.setObjectName(u"grippers")
        self.grippers.setMinimumSize(QSize(200, 150))
        self.grippers.setStyleSheet(u"background-color: #1c1c1c;")
        self.grippers.setFrameShape(QFrame.Shape.StyledPanel)
        self.grippers.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.grippers)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gripper1 = QLabel(self.grippers)
        self.gripper1.setObjectName(u"gripper1")
        self.gripper1.setMinimumSize(QSize(75, 0))
        self.gripper1.setMaximumSize(QSize(80, 90))
        self.gripper1.setPixmap(QPixmap(u":/Icons/icons/gripper1.png"))
        self.gripper1.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.gripper1)

        self.gripper2 = QLabel(self.grippers)
        self.gripper2.setObjectName(u"gripper2")
        self.gripper2.setMinimumSize(QSize(75, 0))
        self.gripper2.setMaximumSize(QSize(75, 75))
        self.gripper2.setPixmap(QPixmap(u":/Icons/icons/gripper1 white.png"))
        self.gripper2.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.gripper2)


        self.horizontalLayout_13.addWidget(self.grippers)

        self.Servo = QFrame(self.gripperframe)
        self.Servo.setObjectName(u"Servo")
        self.Servo.setStyleSheet(u"background-color: #1c1c1c;")
        self.Servo.setFrameShape(QFrame.Shape.StyledPanel)
        self.Servo.setFrameShadow(QFrame.Shadow.Raised)
        self.circularProgressBarBase = QFrame(self.Servo)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 141, 131))
        self.circularProgressBarBase.setFrameShape(QFrame.Shape.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Shadow.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(16, 0, 118, 118))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	border-radius: 59px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.Shape.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Shadow.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(16, 0, 118, 118))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 59px;\n"
"	background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QFrame.Shape.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Shadow.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(26, 10, 98, 98))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 49px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QFrame.Shape.NoFrame)
        self.container.setFrameShadow(QFrame.Shadow.Raised)
        self.Servolabel = QLabel(self.container)
        self.Servolabel.setObjectName(u"Servolabel")
        self.Servolabel.setGeometry(QRect(20, 20, 71, 21))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        self.Servolabel.setFont(font5)
        self.Servolabel.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.Servolabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelPercentage = QLabel(self.container)
        self.labelPercentage.setObjectName(u"labelPercentage")
        self.labelPercentage.setEnabled(True)
        self.labelPercentage.setGeometry(QRect(14, 50, 81, 31))
        font6 = QFont()
        font6.setFamilies([u"Roboto Thin"])
        font6.setPointSize(19)
        font6.setBold(True)
        self.labelPercentage.setFont(font6)
        self.labelPercentage.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.labelPercentage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()

        self.horizontalLayout_13.addWidget(self.Servo)

        self.Titans_2 = QFrame(self.gripperframe)
        self.Titans_2.setObjectName(u"Titans_2")
        self.Titans_2.setStyleSheet(u"background-color: #1c1c1c;")
        self.Titans_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Titans_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.Titans_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 10, 51, 61))
        self.label_4.setPixmap(QPixmap(u":/Icons/icons/Hammerlogo.svg"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.Titans_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 151, 71))
        font7 = QFont()
        font7.setPointSize(34)
        font7.setBold(True)
        self.label_5.setFont(font7)
        self.label_6 = QLabel(self.Titans_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-70, 70, 351, 61))
        font8 = QFont()
        font8.setPointSize(9)
        font8.setBold(True)
        self.label_6.setFont(font8)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.Titans_2)

        self.Timer = QFrame(self.gripperframe)
        self.Timer.setObjectName(u"Timer")
        self.Timer.setMaximumSize(QSize(250, 16777215))
        self.Timer.setStyleSheet(u"background-color: #1c1c1c;")
        self.Timer.setFrameShape(QFrame.Shape.StyledPanel)
        self.Timer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Timer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.timer_label = QLabel(self.Timer)
        self.timer_label.setObjectName(u"timer_label")
        self.timer_label.setMaximumSize(QSize(200, 16777215))
        font9 = QFont()
        font9.setFamilies([u"Bahnschrift"])
        font9.setPointSize(49)
        font9.setBold(True)
        font9.setStrikeOut(False)
        font9.setKerning(True)
        self.timer_label.setFont(font9)
        self.timer_label.setStyleSheet(u"")
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_label.setMargin(0)

        self.verticalLayout_5.addWidget(self.timer_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.start = QPushButton(self.Timer)
        self.start.setObjectName(u"start")
        self.start.setMaximumSize(QSize(100, 16777215))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(13)
        font10.setBold(True)
        self.start.setFont(font10)

        self.verticalLayout_5.addWidget(self.start, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pause = QPushButton(self.Timer)
        self.pause.setObjectName(u"pause")
        self.pause.setMaximumSize(QSize(100, 16777215))
        font11 = QFont()
        font11.setPointSize(13)
        font11.setBold(True)
        self.pause.setFont(font11)
        self.pause.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pause.setCheckable(False)

        self.verticalLayout_5.addWidget(self.pause, 0, Qt.AlignmentFlag.AlignHCenter)

        self.reset = QPushButton(self.Timer)
        self.reset.setObjectName(u"reset")
        self.reset.setMaximumSize(QSize(100, 16777215))
        self.reset.setFont(font11)

        self.verticalLayout_5.addWidget(self.reset, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_13.addWidget(self.Timer)


        self.horizontalLayout_10.addWidget(self.gripperframe)

        self.MODES = QFrame(self.Controls)
        self.MODES.setObjectName(u"MODES")
        self.MODES.setMaximumSize(QSize(200, 16777215))
        self.MODES.setStyleSheet(u"background-color: #1c1c1c;")
        self.MODES.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.MODES)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gainlabel = QLabel(self.MODES)
        self.gainlabel.setObjectName(u"gainlabel")
        font12 = QFont()
        font12.setPointSize(18)
        font12.setBold(True)
        self.gainlabel.setFont(font12)
        self.gainlabel.setStyleSheet(u"border: 2px solid #2e2e2e;")
        self.gainlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.gainlabel)

        self.Depth = QLabel(self.MODES)
        self.Depth.setObjectName(u"Depth")
        font13 = QFont()
        font13.setPointSize(24)
        font13.setBold(True)
        self.Depth.setFont(font13)
        self.Depth.setStyleSheet(u"border: 2px solid #2e2e2e;\n"
"background-color: #c70606")
        self.Depth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.Depth)

        self.sampletool = QLabel(self.MODES)
        self.sampletool.setObjectName(u"sampletool")
        self.sampletool.setFont(font13)
        self.sampletool.setStyleSheet(u"border: 2px solid #2e2e2e;\n"
"background-color: #c70606")
        self.sampletool.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.sampletool)

        self.Stabilize = QLabel(self.MODES)
        self.Stabilize.setObjectName(u"Stabilize")
        self.Stabilize.setFont(font13)
        self.Stabilize.setStyleSheet(u"border: 2px solid #2e2e2e;\n"
"background-color: #c70606")
        self.Stabilize.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.Stabilize)


        self.horizontalLayout_10.addWidget(self.MODES)


        self.verticalLayout.addWidget(self.Controls)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.Cameraswidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sensor.setText("")
        self.Titans.setText(QCoreApplication.translate("MainWindow", u"TITANS", None))
        self.minimize.setText("")
        self.maximize.setText("")
        self.xbutton.setText("")
        self.Onecamera.setText("")
        self.Fourcameras.setText("")
        self.label.setText("")
        self.PHlabel.setText("")
        self.PHValue.setText(QCoreApplication.translate("MainWindow", u"PH", None))
        self.PressureLabel.setText("")
        self.PressureValue.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.IMUlabel.setText("")
        self.IMUValue.setText(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.LeakageLabel.setText("")
        self.LeakageValue.setText(QCoreApplication.translate("MainWindow", u"NO", None))
        self.leftcamera.setText("")
        self.rightcamera.setText("")
        self.cameraview.setText("")
        self.LeftStick.setText("")
        self.up.setText(QCoreApplication.translate("MainWindow", u"\u2b9d", None))
        self.down.setText(QCoreApplication.translate("MainWindow", u"\u2b9f", None))
        self.yaw.setText("")
        self.gripper1.setText("")
        self.gripper2.setText("")
        self.Servolabel.setText(QCoreApplication.translate("MainWindow", u"Servo ", None))
        self.labelPercentage.setText(QCoreApplication.translate("MainWindow", u"0\u00b0", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cronus", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Forged by Titans. Feared by the deep.", None))
        self.timer_label.setText(QCoreApplication.translate("MainWindow", u"15 : 00", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.gainlabel.setText(QCoreApplication.translate("MainWindow", u"GAIN : 0", None))
        self.Depth.setText(QCoreApplication.translate("MainWindow", u"DepthHold", None))
        self.sampletool.setText(QCoreApplication.translate("MainWindow", u"Sample", None))
        self.Stabilize.setText(QCoreApplication.translate("MainWindow", u"Stabilizer", None))
    # retranslateUi

