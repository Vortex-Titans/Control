import serial
import time
from PySide6.QtCore import QThread, Signal

class SerialReader(QThread):
    sensors_signal = Signal(str)
    connection_signal = Signal(bool)

    def __init__(self, port="COM3", baudrate=9600):
        super().__init__()
        self.message = "None"
        self.connected = False
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.init_serial()
        self.start()

    def init_serial(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=0.1)
            self.connected = True
            self.connection_signal.emit(True)
            print(f"Connected to {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            print(f"Serial connection error: {e}")
            self.connection_signal.emit(False)
            self.connected = False

    def run(self):
        while True:
            if self.connected:
                try:
                    self.send_message()
                    self.receive_message()
                    time.sleep(0.1)
                except serial.SerialException as e:
                    print(f"Serial error: {e}")
                    self.connected = False
                    self.reconnect()
            else:
                self.reconnect()

    def set_message(self, data):
        self.message = data

    def send_message(self):
        if self.connected and self.ser and self.ser.is_open:
            self.ser.write(self.message.encode('utf-8'))
            print(f"Sent: {self.message}")

    def receive_message(self):
        if self.connected and self.ser and self.ser.in_waiting > 0:
            recvmsg = self.ser.readline().decode('utf-8').strip()
            if recvmsg:
                print(f"Received: {recvmsg}")
                self.sensors_signal.emit(recvmsg)

    def reconnect(self):
        if self.ser:
            self.ser.close()
        while not self.connected:
            try:
                print("Attempting to reconnect...")
                self.init_serial()
                time.sleep(1)
            except Exception as e:
                print(f"Reconnect failed: {e}")
                time.sleep(1)
