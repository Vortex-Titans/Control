from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtGui import QPixmap
from joystickControl import JoystickController
class Movements(QObject):
    def __init__(self, ui_instance):
        super().__init__()
        self.ui = ui_instance
        self.connection = None
        #self.data_signal.connect(self.receive_data)
    def update_joystick_connection(self, data) :
        #print(status)
        # print(f"Updating connection status to: {data}")
        if data=="no" :
          self.ui.LeftStick.setPixmap(QPixmap(u":/Icons/icons/Left Stick red.png"))
          self.ui.down.setStyleSheet("border: 2px solid #2E2E2E;background-color: #C70606;")
          self.ui.up.setStyleSheet("border: 2px solid #2E2E2E;background-color: #C70606;")
          self.ui.yaw.setPixmap(QPixmap(u":/Icons/icons/YAW red.png"))
        else :
          self.ui.LeftStick.setPixmap(QPixmap(u":/Icons/icons/Left Stick.png"))
          self.ui.yaw.setPixmap(QPixmap(u":/Icons/icons/YAW (1).png"))
          self.ui.down.setStyleSheet("border: 2px solid #2E2E2E;background-color: rgb(28, 28, 28);")
          self.ui.up.setStyleSheet("border: 2px solid #2E2E2E;background-color: rgb(28, 28, 28);")
          self.ui.gripper2.setPixmap(QPixmap(u":/Icons/icons/gripper1 white.png"))
          self.ui.gripper1.setPixmap(QPixmap(u":/Icons/icons/gripper1.png"))
    # def receive_data(self, data):
    #     self.ui.triaaaaal.setText(data)
    def update_movements(self,data):
      # print(f"Updating connection status to: {self.connection}")
      # print(f"Updating connection status to: {data}")
      thruster_1 = int(data[0:4])
      thruster_2 = int(data[4:8])
      bilge_1_pwm = int(data[8:11])
      bilge_1_control = int(data[11])
      bilge_2_pwm = int(data[12:15])
      bilge_2_control = int(data[15])
      bilge_3_pwm = int(data[16:19])
      bilge_3_control = int(data[19])
      bilge_4_pwm = int(data[20:23])
      bilge_4_control = int(data[23])
      gripper_1 = bool(int(data[24]))
      gripper_2 = bool(int(data[25]))
      servo=int(data[26:29])
      sample=bool(int(data[29]))
      highest_pwm = max(bilge_1_pwm, bilge_2_pwm, bilge_3_pwm, bilge_4_pwm)
      percentage = int((highest_pwm / 255) * 100)
      self.ui.gainlabel.setText(f"GAIN : {percentage}%")
      if bilge_1_control==1 and bilge_2_control==1 and bilge_3_control==1 and bilge_4_control==1 and bilge_1_pwm > 0 and bilge_2_pwm > 0 and bilge_3_pwm > 0 and bilge_4_pwm > 0 :
        self.ui.LeftStick.setPixmap(QPixmap(u":/Icons/icons/Left Stick Up.png"))
      elif bilge_1_control==0 and bilge_2_control==0 and bilge_3_control==0 and bilge_4_control==0 :
        self.ui.LeftStick.setPixmap(QPixmap(u":/Icons/icons/Left Stick Down.png"))
      elif bilge_1_control==0 and bilge_2_control==1 and bilge_3_control==1 and bilge_4_control==0 :
        self.ui.LeftStick.setPixmap(QPixmap(u":/Icons/icons/Left Stick Right.png"))
      elif bilge_1_control==1 and bilge_2_control==0 and bilge_3_control==0 and bilge_4_control==1 :
        self.ui.LeftStick.setPixmap(QPixmap(u":/Icons/icons/Left Stick Left.png"))
      else :
        self.ui.LeftStick.setPixmap(QPixmap(u":/Icons/icons/Left Stick.png"))
      if bilge_3_control==1 and bilge_4_control==1 and bilge_1_control==0 and bilge_2_control==0 :
        self.ui.yaw.setPixmap(QPixmap(u":/Icons/icons/YAWleft.png"))
      elif bilge_1_control==1 and bilge_2_control==1 and bilge_3_control==0 and bilge_4_control==0  :
        self.ui.yaw.setPixmap(QPixmap(u":/Icons/icons/YAWright.png"))
      else :
        self.ui.yaw.setPixmap(QPixmap(u":/Icons/icons/YAW (1).png"))
      if thruster_1<1500 and thruster_2<1500 :
        self.ui.up.setStyleSheet("border: 2px solid #2E2E2E;background-color: #059212;")
        self.ui.down.setStyleSheet("border: 2px solid #2E2E2E;background-color: rgb(28, 28, 28);")
      elif thruster_1>1500 and thruster_2>1500  :
        self.ui.down.setStyleSheet("border: 2px solid #2E2E2E;background-color: #059212;")
        self.ui.up.setStyleSheet("border: 2px solid #2E2E2E;background-color: rgb(28, 28, 28);")
      else :
        self.ui.down.setStyleSheet("border: 2px solid #2E2E2E;background-color: rgb(28, 28, 28);")
        self.ui.up.setStyleSheet("border: 2px solid #2E2E2E;background-color: rgb(28, 28, 28);")
      if gripper_1==1 :
        self.ui.gripper1.setPixmap(QPixmap(u":/Icons/icons/green gripper 2.png"))
      else :
        self.ui.gripper1.setPixmap(QPixmap(u":/Icons/icons/gripper1.png"))
      if gripper_2==1 :
        self.ui.gripper2.setPixmap(QPixmap(u":/Icons/icons/Firstt gripper.png"))
      else :
        self.ui.gripper2.setPixmap(QPixmap(u":/Icons/icons/gripper1 white.png"))
      self.ui.labelPercentage.setText(str(servo)+"°")
      if servo == 0:
        style = """
        QFrame {
            border-radius: 59px;
            background-color: qconicalgradient(
                cx:0.5, cy:0.5,
                angle:90,
                stop:0 rgba(255, 0, 127, 0)
            );
        }
        """
      else:
        proportion = servo / 170.0
        proportion = 1.0 - (servo / 170.0)
        stop_value = round(proportion * 0.999, 3)
        style = f"""
        QFrame {{
            border-radius: 59px;
            background-color: qconicalgradient(
                cx:0.5, cy:0.5,
                angle:90,
                stop:{stop_value} rgba(255, 0, 127, 0),
                stop:{min(stop_value + 0.001, 0.999)} rgba(85, 170, 255, 255)
            );
        }}
        """
      self.ui.circularProgress.setStyleSheet(style)
      if sample==True :
        self.ui.sampletool.setStyleSheet("border: 2px solid #2E2E2E;background-color: #059212;")
      else :
        self.ui.sampletool.setStyleSheet("border: 2px solid #2E2E2E;background-color: #C70606")