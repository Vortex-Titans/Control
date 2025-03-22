import pygame
import os


class JoystickController:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.connect_joystick()
        print(f"Initialized Joystick: {self.joystick.get_name()}")
        self.prev_1 = self.prev_2 = 0
        self.pump_1 = self.pump_3 = self.pump_4 = self.pump_6 = 0
        self.pwm_1 = self.pwm_3 = self.pwm_4 = self.pwm_6 = 0
        self.thruster_1 = self.thruster_2 = 1500
        self.gripper_1, self.gripper_2 = False, False


    def connect_joystick(self):

        while pygame.joystick.get_count() == 0:
            #WAITS FOR THE CONNECTION 
            pygame.time.wait(100)
            pygame.joystick.quit()
            pygame.joystick.init()
            print("waiting for connection")
            pygame.time.wait(1000)
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()    

    def is_joystick_connected(self):
        #checks for connection
        return pygame.joystick.get_count() and self.joystick.get_init()

    def map_value(x, in_min, in_max, out_min, out_max):
        return (x - in_min) / (in_max - in_min) * (out_max - out_min) + out_min

    def update_controls(self):
        pygame.event.pump()
        os.system("cls" if os.name == "nt" else "clear")

        x_axis = self.joystick.get_axis(0)
        y_axis = self.joystick.get_axis(1)

        
        if abs(x_axis) > abs(y_axis):

            pwm = int(abs(x_axis) * 255)
            self.pwm_1 = self.pwm_3 = self.pwm_4 = self.pwm_6 = pwm
            if x_axis > 0 :
                
                self.pump_1, self.pump_3, self.pump_4, self.pump_6 = 0, 1, 0, 1
            else:
                self.pump_1, self.pump_3, self.pump_4, self.pump_6 = 1,0,1,0
            
        elif abs(y_axis) > abs(x_axis):

            pwm = int(abs(y_axis) * 255)
            self.pwm_1 = self.pwm_3 = self.pwm_4 = self.pwm_6 = pwm
            self.pump_1 = self.pump_3 = self.pump_4 = self.pump_6 = 1 if y_axis > 0 else 0
    

        up_down = self.joystick.get_axis(3)
        if up_down < -0.1:
            self.thruster_1 = self.thruster_2 = int(JoystickController.map_value(abs(up_down),0,1,1500,1200))
        elif up_down > 0.1:
            self.thruster_1 =  self.thruster_2 = int(JoystickController.map_value(up_down,0,1,1500,1800))
        else:
            self.thruster_1 = self.thruster_2 = 1500
        rotate_right = self.joystick.get_axis(4)
        if rotate_right != -1:
            pwm = int(255 * JoystickController.map_value(rotate_right, -1, 1, 0, 1))
            self.pwm_1 = self.pwm_3 = self.pwm_4 = self.pwm_6 = pwm
            self.pump_1, self.pump_3, self.pump_4, self.pump_6 = 0, 0, 1, 1

        rotate_left = self.joystick.get_axis(5)
        if rotate_left != -1:
            pwm = int(255 * JoystickController.map_value(rotate_left, -1, 1, 0, 1))
            self.pwm_1 = self.pwm_3 = self.pwm_4 = self.pwm_6 = pwm
            self.pump_1, self.pump_3, self.pump_4, self.pump_6 = 1, 1, 0, 0

        if self.prev_1 == 0 and self.joystick.get_button(0) == 1:
            self.gripper_1 = not self.gripper_1
        self.prev_1 = self.joystick.get_button(0)
                                                
                                                
        if self.prev_2 == 0 and  self.joystick.get_button(1):
            self.gripper_2 = not self.gripper_2
        self.prev_2 = self.joystick.get_button(1)

        
    def get_message(self):
        return (
            f"{self.thruster_1:04d}{self.thruster_2:04d}"
            f"{self.pump_1}{self.pwm_1:03d}"
            
            f"{self.pump_3}{self.pwm_3:03d}"
            f"{self.pump_4}{self.pwm_4:03d}"
          
            f"{self.pump_6}{self.pwm_6:03d}"
            f"{int(self.gripper_1)}{int(self.gripper_2)}"
        )


    def run(self):
        while True:
            if not self.is_joystick_connected():
                self.connect_joystick()
            else:    
                self.update_controls()
                msg = self.get_message()
                print(msg)  # Print the message to the console
                print("Message Length:", len(msg))
            

if __name__ == "__main__":
    joystick_controller = JoystickController()
    joystick_controller.run()

