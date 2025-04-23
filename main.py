import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from form1 import Ui_MainWindow
from PySide6.QtCore import Qt , QTimer , QPoint
from movements import Movements
from window_controls import WindowControls
from joystickControl import JoystickController
from socketServer import socketServer
from sensorsReceiver import SensorsReceiver
from test import CameraStream
from cameraReciever import CameraViewer
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.is_maximized = False
        self.is_hidden= False
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.dragging = False
        self.offset = QPoint()
        self.setupUi(self)
        
        RTSP_URL = "rtspsrc latency=0 location=rtsp://admin:vortex2025@192.168.33.50:554/Streaming/Channels/102 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! videoflip video-direction=2 ! videoscale ! video/x-raw,width=640,height=360 ! appsink max-buffers=1 drop=false"
        RTSP_URL2 = "rtspsrc latency=0 location=rtsp://admin:vortex2025@192.168.33.52:554/Streaming/Channels/102 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! videoflip video-direction=2 ! videoscale ! video/x-raw,width=640,height=360 ! appsink max-buffers=1 drop=false"


 
 
        self.Camera = CameraStream(RTSP_URL)
        self.Camera2 = CameraStream(RTSP_URL2)
        self.joystick = JoystickController()
        self.movements = Movements(self)
        self.controls = WindowControls(self)
        self.timer = QTimer(self)
        self.sensor = SensorsReceiver(self)
        self.cameraviewer = CameraViewer(self)
        self.socket = socketServer()
        
        self.Camera.frame_ready.connect(self.cameraviewer.updateCamera1)
        self.Camera2.frame_ready.connect(self.cameraviewer.updateCamera2)
        self.Camera.start()
        self.Camera2.start()
        self.joystick.message_signal.connect(self.movements.update_movements)
        # self.joystick.message_signal.connect(self.movements.receive_data)
        self.joystick.message_signal.connect(self.sensor.update_label)
        self.joystick.message_signal.connect(self.socket.set_message)
        self.socket.sensors_signal.connect(self.sensor.update_label)
        self.joystick.connection_signal.connect(self.movements.update_joystick_connection)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.is_maximized:
                return  # Prevent resizing when in full screen
            # Detect if clicking on edges to resize
            if event.pos().x() >= self.width() - 10 and event.pos().y() >= self.height() - 10:
                self.resizing = True
            else:
                self.dragging = True
                self.offset = event.globalPosition().toPoint() - self.pos()
    def mouseMoveEvent(self, event):
        if self.is_maximized:
            return  # Disable resizing & moving in full-screen
        if self.resizing:
            new_width = max(640, event.pos().x())  # Prevent too small sizes
            new_height = max(480, event.pos().y())
            self.resize(new_width, new_height)
        elif self.dragging:
            self.move(event.globalPosition().toPoint() - self.offset)
        # Change cursor to indicate resizing
        if event.pos().x() >= self.width() - 10 and event.pos().y() >= self.height() - 10:
            self.setCursor(Qt.SizeFDiagCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            self.resizing = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
