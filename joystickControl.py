import pygame
import os
import time
from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtGui import QPixmap
class JoystickController(QThread):
    message_signal = Signal(str)
    connection_signal = Signal(str)
    gain_signal = Signal(float)
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.joystick.init()
        self.joystick = None
        self.gain = 1.0
        self.speed = 255 * self.gain
        self.prev_gain_btn = 0
        self.prev_1 = self.prev_2 = self.prev_3 = self.prev_4 = self.prev_5= 0
        self.pump_1 = self.pump_3 = self.pump_4 = self.pump_6 = 0
        self.pwm_1 = self.pwm_3 = self.pwm_4 = self.pwm_6 = 0
        self.thruster_1 = self.thruster_2 = 1500
        self.gripper_1, self.gripper_2 = False, False
        self.servo_motor = 0
        self.suction_tool = False
        self.start()
    def connect_joystick(self):
      if pygame.joystick.get_count() > 0:
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        print(f"Initialized Joystick: {self.joystick.get_name()}")
        self.connection_signal.emit("yes")
      else:
        print("No joystick detected. Running in GUI mode without joystick.")
        self.connection_signal.emit("no")
        time.sleep(0.05)
        self.joystick = None
    def is_joystick_connected(self):
        #checks for connection
        return pygame.joystick.get_count() and self.joystick.get_init()
    def map_value(x, in_min, in_max, out_min, out_max):
        return (x - in_min) / (in_max - in_min) * (out_max - out_min) + out_min
    def update_controls(self):
        pygame.event.pump()
        os.system("cls" if os.name == "nt" else "clear")
        y_axis = self.joystick.get_axis(1)
        x_axis = self.joystick.get_axis(0)
        if abs(y_axis) > abs(x_axis):
            pwm = int(abs(y_axis) * self.speed)
            self.pwm_1 = self.pwm_3 = self.pwm_4 = self.pwm_6 = pwm
            if y_axis < 0 :
                self.pump_1, self.pump_3, self.pump_4, self.pump_6 = 1,1,1,0
            else:
                self.pump_1, self.pump_3, self.pump_4, self.pump_6 = 0,0,0,1
        elif abs(x_axis) > abs(y_axis):
            if x_axis > 0:
                pwm = int(abs(x_axis) * self.speed)
                self.pwm_1 = self.pwm_3 = self.pwm_4 = self.pwm_6 = self.speed
                # self.pwm_4 = self.speed
                self.pump_1 = 0# Back left
                self.pump_3 = 1 # Front left
                self.pump_4 = 1# Back right
                self.pump_6 = 1 # Front right
            else:
                pwm = int(abs(x_axis) * self.speed)
                self.pwm_1 = self.pwm_3 = self.pwm_4 = self.pwm_6 = self.speed
                # self.pwm_6 = self.speed
                self.pump_1 = 1
                self.pump_3 = 0
                self.pump_4 = 0
                self.pump_6 = 0
        up_down = self.joystick.get_axis(3)
        if up_down < -0.1:
            delta = int(300 * abs(up_down) * self.gain)  # backward
            self.thruster_1 = self.thruster_2 = 1500 - delta
        elif up_down > 0.1:
            delta = int(300 * up_down * self.gain)  # forward
            self.thruster_1 = self.thruster_2 = 1500 + delta
        else:
            self.thruster_1 = self.thruster_2 = 1500

        rotate_right = self.joystick.get_axis(5)
        if rotate_right != -1:
            pwm = int(self.speed * JoystickController.map_value(rotate_right, -1, 1, 0, 1))
            self.pwm_1 = self.pwm_3 = self.pwm_4 = self.pwm_6 = pwm
            self.pump_1, self.pump_3, self.pump_4, self.pump_6 = 1,1,0,1
        rotate_left = self.joystick.get_axis(4)
        if rotate_left != -1:
            pwm = int(self.speed * JoystickController.map_value(rotate_left, -1, 1, 0, 1))
            self.pwm_1 = self.pwm_3 = self.pwm_4 = self.pwm_6 = pwm
            self.pump_1, self.pump_3, self.pump_4, self.pump_6 = 0,0,1,0
            
        #gain
        if self.prev_gain_btn == 0 and self.joystick.get_button(6) == 1:
            if self.gain == 1.0:
                self.gain = 0.25
            elif self.gain == 0.25:
                self.gain = 0.5
            else:
                self.gain = 1.0
            self.speed = int(255 * self.gain)  # <--- Add this line
        self.gain_signal.emit(self.gain)
        self.prev_gain_btn =  self.joystick.get_button(6)



        # grippers , R1 & L1
        if self.prev_1 == 0 and self.joystick.get_button(4) == 1:
            self.gripper_1 = not self.gripper_1
        self.prev_1 = self.joystick.get_button(4)
        if self.prev_2 == 0 and  self.joystick.get_button(5):
            self.gripper_2 = not self.gripper_2
        self.prev_2 = self.joystick.get_button(5)
        # servo ,
        if self.prev_3 == 0 and self.joystick.get_button(2) == 1:
            self.servo_motor = (self.servo_motor + 10) % 180
        self.prev3 = self.joystick.get_button(2)
        if self.prev_4 == 0 and self.joystick.get_button(3) == 1:
            self.servo_motor = (self.servo_motor - 10) % 180
        self.prev_4 = self.joystick.get_button(3)
        # suction tool , button X
        if self.prev_5 == 0 and self.joystick.get_button(0) == 1:
            self.suction_tool = not self.suction_tool
        self.prev_5 = self.joystick.get_button(0)
    def get_message(self):
        return (
            f"{self.thruster_1:04d}{self.thruster_2:04d}"
            f"{self.pwm_1:03d}{self.pump_1}"
            f"{self.pwm_3:03d}{self.pump_3}"
            f"{self.pwm_4:03d}{self.pump_4}"
            f"{self.pwm_6:03d}{self.pump_6}"
            f"{int(self.gripper_1)}{int(self.gripper_2)}"
            f"{self.servo_motor:03d}{int(self.suction_tool)}""\n"
        )
    def run(self):
     while True:
        if self.joystick is None or not self.is_joystick_connected():
            self.connect_joystick()
        if self.joystick:
            self.update_controls()
            msg = self.get_message()
            # print(msg)
            self.message_signal.emit(msg)
        else:
             msg = "00000000000000000000000000"  # Default message when no joystick
             self.connection_signal.emit("no")
        # pygame.time.wait(100)  # Prevent excessive CPU usage
        time.sleep(0.05)
if __name__ == "__main__":
    joystick_controller = JoystickController()
    joystick_controller.run()
