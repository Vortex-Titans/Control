from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtGui import QPixmap

class SensorsReceiver(QObject):
      def __init__(self, ui_instance):
        super().__init__()
        self.ui = ui_instance

      def update_label(self,data):
        ph=(data[0:5])
        pressure=(data[5:10])
        roll=(data[10:14])
        pitch=(data[14:18])
        yaw=(data[18:22])
        self.ui.PHValue.setText(ph)
        self.ui.PressureValue.setText(pressure)
        self.ui.IMUValue.setText(f"Roll: {roll}, Pitch: {pitch}, Yaw: {yaw}")
        # self.ui.IMUValue.setFont(self.ui.IMUValue.font().setPointSize(9))
        # self.ui.IMUValue.setText(f"X: {roll}, Y: {pitch}, Z: {yaw}")

        # pass
        # self.ui.sockettrial.setText(data)
        