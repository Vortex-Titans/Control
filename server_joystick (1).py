import socket
import time
import os
import pygame
from joystickControl_py import JoystickController  # Import the class

# Server configuration (PC's static IP)
HOST = '192.168.33.1'   # PC's static IP (same subnet as Arduino)
PORT = 1222         # Port to listen on

# Initialize server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server started at {HOST}:{PORT}, waiting for connection...")

# Wait for Arduino to connect
client, addr = server.accept()

# server.settimeout(0.1)
server.setblocking(False)
print(f"Arduino connected from {addr}")

# Initialize Joystick Controller
joystick = JoystickController()


while True:
    # pygame.event.pump()
    # os.system("cls" if os.name == "nt" else "clear")  # Clear console output

    # Update joystick values
    joystick.update_controls()

    # Get the current time
    # current_time = time.strftime("%H:%M:%S", time.localtime())

    # current_time += "\n"
    # Define the messages to send
    # msg = '1500150025502550255025502550255011'
    # msg2 = '1500150025502550255025502550255010'

    # Print the formatted message

    # print(f"Sending: {current_time}")
    try:
        # Send current_time to Arduino
        # client.send(current_time.encode())
        # client.settimeout(0.1)  # Set a 5-second timeout

        msg=joystick.get_message()
        print(msg,"\n")
        client.send(msg.encode())

        data = client.recv(4).decode()
        if data:
            print(f"Received from Arduino: {data}")
        
        
        # time.sleep(0.5)  # Small delay to ensure Arduino processes the data

        # Send msg to Arduino
       #time.sleep(0.1)  # Small delay to ensure Arduino processes the data

        # Send msg2 to Arduino (if needed)
        # client.send(msg2.encode())
        # time.sleep(0.1)

        # Receive response from Arduino (optional)
        # client.settimeout(1)  # Set a 5-second timeout

        time.sleep(0.05)  # Delay to prevent spamming
        
    except :
            print(f"Error: . Connection lost. Waiting for Arduino to reconnect...")
            server.close()
            while True:
                try:
                    # # Server configuration (PC's static IP)
                    # HOST = '192.168.33.1'   # PC's static IP (same subnet as Arduino)
                    # PORT = 1222         # Port to listen on

                    # # Initialize server socket
                    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    server.bind((HOST, PORT))
                    server.listen(1)

                    print(f"Server started at {HOST}:{PORT}, waiting for connection...")

                    # Wait for Arduino to connect
                    client, addr = server.accept()

                    # # server.settimeout(0.1)
                    # server.setblocking(False)
                    print(f"Arduino connected from {addr}")
                    break
                except Exception as e:
                    print(e)
                    continue

    # server.settimeout(0.5)    