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
        
        self.prev_gain_btn = 0
        self.prev_gripper_1_value = self.prev_gripper_2_value = self.prev_suction_tool_value = 0
        self.back_left_dir = self.front_left_dir = self.back_right_dir = self.front_right_dir = 0
        self.back_left_pwm = self.front_left_pwm = self.back_right_pwm = self.front_right_pwm = 0
        self.thruster_1 = self.thruster_2  = self.thruster_3 = self.thruster_4 = 1500
        self.gripper_1, self.gripper_2 = False, False


        # variables to save activation status of pelges and thrusters
        self.back_left_belge_activation = True
        self.front_left_belge_activation = True
        self.back_right_belge_activation = True
        self.front_right_belge_activation = True
        self.thruster_1_activation = True
        self.thruster_2_activation = True
        self.thruster_3_activation = True
        self.thruster_4_activation = True

        self.messege = "11111111"  #activation values for pelges and thrysters , 1 -> activated 0-> not
        
        self.kp = 2   #increase to increase pid correction values
        self.ki = 0.001
        self.kd = 0.0001

        self.setpoint_yaw = None
        self.current_value_yaw = None
        self.previous_error_yaw = 0
        self.integral_yaw = 0
        self.past_derivative_yaw = 0
        self.alpha = 0.9
        
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
    
    def pid_control(self):        #pid algoritm and return correction value to be added to motors

        error = self.setpoint_yaw - self.current_value_yaw

        p = error * self.kp

        integral += (error * self.ki)

        d = (error - self.previous_error_yaw) * self.kd
        d = self.alpha * self.past_derivative_yaw + (1 - self.alpha) * d

        output = p + integral + d

        self.previous_error_yaw = error
        self.past_derivative_yaw = d

        return output
    def reset_pid_variables(self):  #resets pid values when new setpoint is set to avoid using old values
        self.integral_yaw = 0
        self.previous_error_yaw = 0
        self.past_derivative_yaw = 0
        self.setpoint_yaw = None
    def check_button_pushed(self , prev , joystick_readings , button): #checks if a button is clicked
        
        if getattr(self,prev) == 0 and joystick_readings == 1:
            setattr(self,button,not getattr(self, button))
        setattr(self,prev,joystick_readings) 
        
    def set_activation_messege(self):   #sets the messege value from GUI for pelges_thrusters activation
        # getting the messege from GUI to sets the messege logic

        #save the messege to self.messege variable
        return  # was put to avoid errors before function inialization
    def set_IMU_current_value(self):  #add angleZ IMU readings to self.current_yaw_value
            #remove return after finishing 
        return # was put to avoid errors before function inialization
    def set_motors_thrusters_activation_status(self):    #checks which motors and algorithms are working and which arent 
        
        if self.messege is None or len(self.messege) != 8:
            self.messege = None
        else:
            self.back_left_belge_activation = True if self.messege[0] == "1" else 0
            self.front_left_belge_activation = True if self.messege[1] == "1" else 0
            self.back_right_belge_activation = True if self.messege[2] == "1" else 0
            self.front_right_belge_activation = True if self.messege[3] == "1" else 0
            self.thruster_1_activation = True if self.messege[4] == "1" else 0
            self.thruster_2_activation = True if self.messege[5] == "1" else 0
            self.thruster_3_activation = True if self.messege[6] == "1" else 0
            self.thruster_4_activation = True if self.messege[7] == "1" else 0

    def resets_belges_thrusters_activation_messege(self):   
        self.messege = None
    def set_direction(self , back_left_direction , front_left_direction , back_right_direction , front_right_direction):  #sets the direction for pelges based on arguments
        self.back_left_dir = back_left_direction
        self.front_left_dir = front_left_direction
        self.back_right_dir = back_right_direction
        self.front_right_dir = front_right_direction

    def set_pwm_for_pelges(self , pwm):

        
        self.back_left_pwm = pwm
        self.front_left_pwm = pwm
        self.back_right_pwm = pwm
        self.front_right_pwm = pwm
        
    def set_thrusters_value(self , value):   #sets the thrusters value
        self.thruster_1 = self.thruster_2 = value
    def setting_belges_thrusters_pwm_based_on_activation(self):    # sets the the pwm or thruster value to 0 if not activated 
        self.back_left_pwm = self.back_left_pwm if self.back_left_belge_activation else 0
        self.front_left_pwm = self.front_left_pwm if self.front_left_belge_activation else 0
        self.back_right_pwm = self.back_right_pwm if self.back_right_belge_activation else 0
        self.front_right_pwm = self.front_right_pwm if self.front_right_belge_activation else 0

        self.thruster_1 = self.thruster_1 if self.thruster_1_activation else 1500
        self.thruster_2 = self.thruster_2 if self.thruster_2_activation else 1500
        self.thruster_3 = self.thruster_3 if self.thruster_3_activation else 1500
        self.thruster_4 = self.thruster_4 if self.thruster_4_activation else 1500
    
    def up_down_movments(self , up_down):
        delta = int(300 * abs(up_down) * self.gain)
        if up_down < -0.1:
            self.set_thrusters_value(1500 - delta)

        elif up_down > 0.1:
            self.set_thrusters_value(1500 + delta)
        else:
            self.set_thrusters_value(1500)
    def horizontal_movments(self , x_axis, y_axis):
        if abs(y_axis) > abs(x_axis):
            pwm = int(abs(y_axis) * self.gain * 255)
            self.set_pwm_for_pelges(pwm)
            if y_axis < 0 :
                self.set_direction(1,1,1,0)
                self.thruster_3 = self.thruster_4 = 1500 - int(abs(y_axis) * self.gain * 300) 
                
            else:
                self.set_direction(0,0,0,1)
                self.thruster_3 = self.thruster_4 = int(abs(y_axis) * self.gain * 300) + 1500
        elif abs(x_axis) > abs(y_axis):
            if x_axis > 0:
                pwm = int(abs(x_axis) * self.gain * 255)
                self.set_pwm_for_pelges(pwm)
                # self.pwm_4 = self.spee
                self.set_direction(0,1,1,1)
            else:
                pwm = int(abs(x_axis) * self.gain * 255)
                self.set_pwm_for_pelges(pwm)
                # self.pwm_6 = self.speed
                self.set_direction(1,0,0,0)
    def rotation_movments(self , rotate_left , rotate_right):
        if rotate_right != -1:
            pwm = int(self.gain * JoystickController.map_value(rotate_right, -1, 1, 0, 1) * 255)
            self.set_pwm_for_pelges(pwm)
            self.thruster_3 = self.thruster_4 = int(JoystickController.map_value(rotate_right, -1, 1, 0, 1) * self.gain * 300) + 1500
            self.set_direction(1,1,0,1)
        
        if rotate_left != -1:
            pwm = int(self.gain * JoystickController.map_value(rotate_left, -1, 1, 0, 1) * 255)
            self.thruster_3 = self.thruster_4 = 1500 - int(JoystickController.map_value(rotate_left, -1, 1, 0, 1) * self.gain * 300)
            self.set_pwm_for_pelges(pwm)
            self.set_direction(1,0,0,0)

    def gain_function(self, joystick_value):

        if self.prev_gain_btn == 0 and joystick_value == 1:
            if self.gain == 1.0:
                self.gain = 0.25
            elif self.gain == 0.75:
                self.gain = 1.0
            elif self.gain == 0.5:
                self.gain = 0.75
            elif self.gain == 0.25:
                self.gain = 0.5
        
        self.gain_signal.emit(self.gain)
        self.prev_gain_btn = joystick_value

    def update_controls(self):
        pygame.event.pump()
        os.system("cls" if os.name == "nt" else "clear")

        self.set_activation_messege()
        self.set_motors_thrusters_activation_status()

        x_axis = self.joystick.get_axis(0)
        y_axis = self.joystick.get_axis(1)
        up_down = self.joystick.get_axis(3)
        rotate_left = self.joystick.get_axis(4)
        rotate_right = self.joystick.get_axis(5)

        self.horizontal_movments(x_axis , y_axis)
        
        self.up_down_movments(up_down)

        
        self.rotation_movments(rotate_left , rotate_right)
        #gain
        self.gain_function(self.joystick.get_button(6))


        
        # grippers , R1 & L1
        self.check_button_pushed("prev_gripper_1_value" , self.joystick.get_button(4) , "gripper_1")
        self.check_button_pushed("prev_gripper_2_value" , self.joystick.get_button(5), "gripper_2")
        
        
        
        # suction tool , button X
        self.check_button_pushed("prev_suction_tool_value" , self.joystick.get_button(0) , "suction_tool")

        self.setting_belges_thrusters_pwm_based_on_activation()  #sets not activated pelge_thrusters to 0 or 1500
        self.resets_belges_thrusters_activation_messege()  # resets the messege to None
        
        
    def get_message(self):
        return (
            f"{int(self.thruster_1):04d}{int(self.thruster_2):04d}"
            f"{int(self.thruster_4):04d}{int(self.thruster_3):04d}"
            f"{int(self.back_left_pwm):03d}{int(self.back_left_dir)}"
            f"{int(self.front_left_pwm):03d}{int(self.front_left_dir)}"
            f"{int(self.back_right_pwm):03d}{int(self.back_right_dir)}"
            f"{int(self.front_right_pwm):03d}{int(self.front_right_dir)}"
            f"{int(self.gripper_1)}{int(self.gripper_2)}"
            f"{int(self.suction_tool)}\n"
        )

    def run(self):
     while True:
        if self.joystick is None or not self.is_joystick_connected():
            self.connect_joystick()
        if self.joystick:
            self.update_controls()
            msg = self.get_message()
            
            print(msg)
            print(len(msg))
            self.message_signal.emit(msg)
        else:
             msg = "00000000000000000000000000"  # Default message when no joystick
             self.connection_signal.emit("no")
        # pygame.time.wait(100)  # Prevent excessive CPU usage
        time.sleep(0.05)
if __name__ == "__main__":
    joystick_controller = JoystickController()
    joystick_controller.run()
