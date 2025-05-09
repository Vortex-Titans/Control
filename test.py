import cv2
from PySide6.QtCore import QThread, Signal, QTimer, Qt
from PySide6.QtGui import QImage
import numpy as np

class CameraStream(QThread):
    frame_ready = Signal(QImage)  # Signal to emit QImage frames
    reconnecting = Signal(str)    # Signal to indicate reconnection status
    reconnect_requested = Signal() # Signal to request reconnection from main thread

    def __init__(self, rtsp_url):
        """Initialize the camera stream with the RTSP URL"""
        super().__init__()
        self.rtsp_url = rtsp_url
        self.identifier = rtsp_url[62:64] if len(rtsp_url) > 64 else "main"  # Extract camera ID from URL or use default
        self.cap = None
        self.frame = None
        
        # Connection and reconnection settings
        self.running = True
        self.connected = False
        self.reconnect_attempts = 0
        self.max_reconnect_attempts = 10  # Maximum consecutive reconnection attempts
        self.reconnect_delay = 0.5  # Delay between reconnection attempts in seconds
        
        # Connect the reconnect signal to try_reconnect method
        self.reconnect_requested.connect(self.try_reconnect, Qt.QueuedConnection)
        
        # Start periodic reconnection attempts
        self.reconnect_timer = QTimer(self)
        self.reconnect_timer.timeout.connect(self.check_connection)
        self.reconnect_timer.start(500)  # Check every 500ms
    
    def init_camera(self):
        """Initialize the camera connection"""
        if self.cap is not None:
            self.cap.release()
            self.cap = None
            
        try:
            self.cap = cv2.VideoCapture(self.rtsp_url, cv2.CAP_GSTREAMER)
            if self.cap.isOpened():
                print(f"✅ Camera {self.identifier} connected")
                self.reconnecting.emit(f"Camera {self.identifier} connected successfully")
                self.connected = True
                self.reconnect_attempts = 0  # Reset counter on successful connection
                return True
            else:
                self.connected = False
                self.cap = None
                self.reconnecting.emit(f"Unable to connect to camera {self.identifier}")
                return False
        except Exception as e:
            print(f"❌ Error connecting to camera {self.identifier}: {str(e)}")
            self.reconnecting.emit(f"Error: {str(e)}")
            self.connected = False
            if self.cap:
                self.cap.release()
                self.cap = None
            return False
    
    def try_reconnect(self):
        """Attempt to reconnect to the camera"""
        if self.connected:
            return
            
        self.reconnect_attempts += 1
        if self.reconnect_attempts % 5 == 0:
            print(f"🔄 Attempting to reconnect camera {self.identifier} (attempt {self.reconnect_attempts})")
            self.reconnecting.emit(f"Reconnection attempt {self.reconnect_attempts}...")
            
        if self.reconnect_attempts > self.max_reconnect_attempts:
            print(f"⚠️ Giving up reconnection for camera {self.identifier} after {self.max_reconnect_attempts} attempts")
            self.reconnecting.emit(f"Giving up after {self.max_reconnect_attempts} attempts. Will retry later.")
            self.reconnect_attempts = 0  # Reset for future attempts
            return
            
        self.init_camera()
    
    def check_connection(self):
        """Periodically check connection status and trigger reconnection if necessary"""
        if not self.connected:
            print(f"🔄 Camera {self.identifier} is disconnected, attempting reconnection...")
            self.try_reconnect()

    def convert_frame_to_qimage(self, frame):
        """Convert an OpenCV BGR frame to a QImage"""
        if frame is None:
            return None

        height, width, channel = frame.shape
        bytes_per_line = 3 * width  # 3 channels (RGB)

        # Convert BGR to RGB (since OpenCV uses BGR by default)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create QImage from frame data
        qimg = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return qimg

    def run(self):
        """Main loop for streaming from RTSP source"""
        connected = self.init_camera()
        if not connected:
            print(f"🔄 Camera {self.identifier} will attempt reconnection in background...")
            QTimer.singleShot(int(self.reconnect_delay * 1000), lambda: self.reconnect_requested.emit())
        
        consecutive_failures = 0
        max_consecutive_failures = 5
        
        while self.running:
            if not self.connected or self.cap is None:
                # Sleep briefly before next check to prevent CPU hogging
                self.msleep(100)
                continue
                
            try:
                ret, frame = self.cap.read()
                if not ret:
                    consecutive_failures += 1
                    if consecutive_failures == 1:
                        print(f"❌ Camera {self.identifier} failed to read frame")
                    
                    if consecutive_failures >= max_consecutive_failures:
                        print(f"⚠️ Camera {self.identifier} connection lost")
                        self.reconnecting.emit(f"Stream lost, attempting to reconnect...")
                        self.connected = False
                        if self.cap:
                            self.cap.release()
                            self.cap = None
                        self.reconnect_requested.emit()
                    
                    self.msleep(100)
                    continue
            except Exception as e:
                print(f"❌ Error reading from camera {self.identifier}: {str(e)}")
                self.reconnecting.emit(f"Error reading from stream: {str(e)}")
                self.connected = False
                if self.cap:
                    self.cap.release()
                    self.cap = None
                self.reconnect_requested.emit()
                self.msleep(100)
                continue

            # Successfully read a frame
            consecutive_failures = 0
            self.frame = frame
            
            # Convert frame to QImage and emit it
            qimg = self.convert_frame_to_qimage(frame)
            if qimg is not None:
                self.frame_ready.emit(qimg)
                
            # Process at a reasonable frame rate
            self.msleep(10)  # Sleep for 10ms (~100 fps max)

    def stop(self):
        """Stop streaming and release resources"""
        self.running = False
        self.quit()
        self.wait()
        self.cleanup()

    def cleanup(self):
        """Cleanup resources"""
        if self.cap and self.cap.isOpened():
            self.cap.release()
            self.cap = None
        # No need to call destroyAllWindows since we're using Qt

# Example usage:
# RTSP_URL = "rtspsrc latency=0 location=rtsp://admin:vortex2025@192.168.33.51:554/Streaming/Channels/101 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! video/x-raw,width=1920,height=1080 ! appsink"
# camera = CameraStream(RTSP_URL)
# camera.start()