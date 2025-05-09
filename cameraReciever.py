from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtGui import QPixmap

class CameraViewer(QObject):
    def __init__(self, ui_instance):
        super().__init__()
        self.ui = ui_instance
        

    # def updateCamera(self, qimg):
    #     if qimg is None:
    #         return
        
    #     # Convert QImage to QPixmap and set it on QLabel
    #     pixmap = QPixmap.fromImage(qimg)
    #     self.ui.cameraview.setPixmap(pixmap)
    def updateCamera1(self, qimg):
        if qimg is None:
            return
        
        # Convert QImage to QPixmap and set it on QLabel
        pixmap = QPixmap.fromImage(qimg)
        self.ui.leftcamera.setPixmap(pixmap)
    def updateCamera2(self, qimg):
        if qimg is None:
            return
        
        # Convert QImage to QPixmap and set it on QLabel
        pixmap = QPixmap.fromImage(qimg)
        self.ui.rightcamera.setPixmap(pixmap)
        
