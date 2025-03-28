import socket
import time
import os
import pygame
from joystickControl_py import JoystickController

# Server configuration
HOST = '192.168.33.1'
PORT = 1222

# Initialize server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server started at {HOST}:{PORT}, waiting for connection...")

# Wait for Arduino to connect
client, addr = server.accept()
server.setblocking(False)
print(f"Arduino connected from {addr}")

# Initialize Joystick Controller
joystick = JoystickController()

def parse_and_print_sensor_data(data):
    """Directly parse and print the sensor data"""
    try:
        # Split the data into parts
        ph = data[:5].strip()
        depth = data[5:10].strip()
        roll = data[10:16].strip()
        pitch = data[16:22].strip()
        yaw = data[22:28].strip()
        
        # Clear console and print values
        # os.system("cls" if os.name == "nt" else "clear")
        print("=== Sensor Readings ===")
        print(f"pH:       {ph}")
        print(f"Depth:    {depth}")
        print(f"Roll:     {roll}")
        print(f"Pitch:    {pitch}")
        print(f"Yaw:      {yaw}")
        print("=======================")
        # time.sleep(0.5)
    except Exception as e:
        print(f"Error parsing data: {e}")

while True:
    # Update joystick values
    joystick.update_controls()

    try:
        # Send joystick data to Arduino
        msg = joystick.get_message() + "\n"
        # print(f"Sending: {msg.strip()}")
        client.send(msg.encode())

         # Receive and process data from Arduino
        data = client.recv(28).decode()
        print(f"{data} (length: {len(data)})")
        if data and len(data) == 28:
             parse_and_print_sensor_data(data)
        elif data:
             print(f"Received incomplete data: {data} (length: {len(data)})")

        time.sleep(0.05)
        
    except Exception as e:
        print(f"Error: {e}. Reconnecting...")
        server.close()
        while True:
            try:
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.bind((HOST, PORT))
                server.listen(1)
                client, addr = server.accept()
                print(f"Reconnected to Arduino at {addr}")
                break
            except Exception as e:
                print(f"Reconnect failed: {e}, retrying...")
                time.sleep(1)
                continue