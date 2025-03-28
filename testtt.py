import socket
import time
import os
import pygame
from joystickControl_py import JoystickController

# Server configuration
HOST = '192.168.33.1'  # IP address for the server
PORT = 1222  # Port number

# Initialize server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"Server started at {HOST}:{PORT}, waiting for connection...")

# Wait for Arduino to connect
client, addr = server.accept()
server.setblocking(False)  # Make the server non-blocking to avoid waiting for responses
print(f"Arduino connected from {addr}")

# Initialize Joystick Controller
joystick = JoystickController()

def parse_and_print_sensor_data(data):
    """Directly parse and print the sensor data"""
    try:
        # Extract sensor values based on their fixed positions
        ph = data[:5].strip()
        depth = data[5:10].strip()
        roll = data[10:16].strip()
        pitch = data[16:22].strip()
        yaw = data[22:28].strip()
        
        # Print values
        print("=== Sensor Readings ===")
        print(f"pH:       {ph}")
        print(f"Depth:    {depth}")
        print(f"Roll:     {roll}")
        print(f"Pitch:    {pitch}")
        print(f"Yaw:      {yaw}")
        print("=======================")
    except Exception as e:
        print(f"Error parsing data: {e}")

while True:
    joystick.update_controls()  # Update joystick values without delay
    
    try:
        # Send joystick data to Arduino
        msg = joystick.get_message() + "\n"
        print(f"Sending: {msg.strip()}")
        client.send(msg.encode())

        # Receive and process data from Arduino (non-blocking attempt)
        try:
            data = client.recv(28).decode()
            if len(data) == 28:
                parse_and_print_sensor_data(data)
            elif data:
                print(f"Received incomplete data: {data} (length: {len(data)})")
        except BlockingIOError:
            pass  # No data received yet, continue loop

    except Exception as e:
        print(f"Error: {e}. Reconnecting...")
        server.close()
        
        # Reconnect loop
        while True:
            try:
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.bind((HOST, PORT))
                server.listen(1)
                client, addr = server.accept()
                print(f"Reconnected to Arduino at {addr}")
                break  # Exit reconnect loop when successful
            except Exception as e:
                print(f"Reconnect failed: {e}, retrying...")
                time.sleep(1)
