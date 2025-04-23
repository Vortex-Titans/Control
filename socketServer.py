import socket
import time
from PySide6.QtCore import QThread, Signal

class socketServer(QThread):
    sensors_signal = Signal(str)
    connection_signal = Signal(str)
    def __init__(self):
        super().__init__()
        self.message = "None"  # Default message
        self.connected = False
        self.HOST = '192.168.33.11'  # PC's static IP (same subnet as Arduino)
        self.PORT = 1222  # Port to listen on
        self.initSocket()
        self.start()

    def run(self):
        while True:
            if not self.connected:
                print(f"Server started at {self.HOST}:{self.PORT}, waiting for connection...")
                try:
                    self.connection, address = self.socket.accept()
                    # self.connection.setblocking(False)  # Set non-blocking after accepting connection
                    # self.socket.settimeout(0.05)
                    print(f"Arduino connected from {address}")
                    self.connected = True
                except Exception as e:
                    print(f"Error accepting connection: {e}")
                    # time.sleep(1)  # Retry after a delay
            else:
                try:
                    self.send_message()
                    self.receive_message()
                    time.sleep(0.1)  # Delay to prevent overloading
                except socket.timeout:
                    # print("Socket timeout occurred. Retrying...")
                    pass
                except BlockingIOError:
                    pass  # No data received, continue loop
                except ConnectionResetError:
                    print("Connection reset by peer. Reconnecting...")
                    self.connected = False
                    self.reconnect()
                except Exception as e:
                    print(f"Unexpected error: {e}. Reconnecting...")
                    self.connected = False
                    self.reconnect()

    def initSocket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.HOST, self.PORT))
        self.socket.listen(1)

    def set_message(self, data):
        self.message = data

    def send_message(self):
        if self.connected:
            self.connection.send(bytes(self.message, "utf-8"))
            # print(f"Sent: {self.message}")

    def receive_message(self):
        # recvmsg = self.connection.recv(28).decode()
        # self.sensors_signal.emit(recvmsg)
        # if recvmsg:
        #     print(f"Received: {recvmsg} (length: {len(recvmsg)})")
        #     self.sensors_signal.emit(recvmsg)
            try:
                recvmsg = self.connection.recv(28).decode()
                self.sensors_signal.emit(recvmsg)
            except BlockingIOError:
                return None  # No data received, continue loop
            except ConnectionResetError:
                self.connected = False  # Handle disconnection
                return None

    def reconnect(self):
        self.socket.close()
        while True:
            try:
                self.initSocket()
                self.connection, address = self.socket.accept()
                self.connection.setblocking(False)
                print(f"Reconnected to Arduino at {address}")
                self.connected = True
                break
            except Exception as e:
                print(f"Reconnect failed: {e}, retrying...")
                time.sleep(1)
