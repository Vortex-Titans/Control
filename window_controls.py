from PySide6.QtCore import Qt , QTimer
from PySide6.QtGui import QPixmap
import pyttsx3
import winsound

class WindowControls:
    def __init__(self, main_window):
        self.main_window = main_window
        self.timer = QTimer(self.main_window) 
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = 15 * 60
        self.main_window.is_maximized = False
        self.main_window.is_hidden = False
        self.main_window.xbutton.clicked.connect(self.main_window.close)
        self.main_window.maximize.clicked.connect(self.minimizer)
        self.main_window.minimize.clicked.connect(self.main_window.showMinimized)
        self.main_window.sensor.clicked.connect(self.hide_sensor)
        self.main_window.Onecamera.clicked.connect(self.show_single_camera)
        self.main_window.Fourcameras.clicked.connect(self.show_four_cameras)
        self.main_window.start.clicked.connect(self.start_timer)
        self.main_window.pause.clicked.connect(self.pause_timer)
        self.main_window.reset.clicked.connect(self.reset_timer)
        self.engine = pyttsx3.init()


    def hide_sensor(self):
        if self.main_window.is_hidden:
            self.main_window.sensors.setFixedWidth(0)
        else:
            self.main_window.sensors.setFixedWidth(100)
        
        self.main_window.is_hidden = not self.main_window.is_hidden

    def minimizer(self):
        if self.main_window.is_maximized:
            self.main_window.showNormal()
        else:
            self.main_window.showFullScreen()

        self.main_window.is_maximized = not self.main_window.is_maximized 
    def show_single_camera(self):
       self.main_window.Cameraswidget.setCurrentWidget(self.main_window.Singleecamera)

    def show_four_cameras(self):
        self.main_window.Cameraswidget.setCurrentWidget(self.main_window.fourcameras)
    def update_timer(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            self.main_window.timer_label.setText(f"{minutes:02}:{seconds:02}")

        else:
            self.timer.stop()
            winsound.Beep(1000, 1000)
            

    def start_timer(self):
        self.timer.start(1000)
        self.engine = pyttsx3.init()
        self.engine.say("Timer Started!")
        self.engine.runAndWait()


    def pause_timer(self):
        self.timer.stop()
        self.engine.say("Timer Paused!")
        self.engine.runAndWait()
    def reset_timer(self):
        self.timer.stop()
        self.time_remaining = 15 * 60
        self.main_window.timer_label.setText("15:00")
        self.engine.say("Timer Reset!")
        self.engine.runAndWait()
