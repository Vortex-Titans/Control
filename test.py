# # import cv2
# # # Define the GStreamer pipeline
# # gst_pipeline = (
# #     "rtspsrc latency=0 location=rtsp://admin:vortex2025@192.168.33.52:554/Streaming/Channels/101 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! video/x-raw,width=1920,height=1080 ! appsink"
# # )
# # # Open the GStreamer pipeline
# # cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)
# # if not cap.isOpened():
# #     print("Error: Unable to open GStreamer pipeline.")
# #     exit()
# # # Main loop to read and display frames
# # while True:
# #     ret, frame = cap.read()
# #     if not ret:
# #         print("Error: Unable to retrieve frame from GStreamer pipeline.")
# #         break
# #     frame = cv2.resize(frame, (576, 1024))
# #     cv2.imshow("720p RTSP Camera Feed", frame)
# #     # Exit on pressing 'q'
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
# # # Cleanup
# # cap.release()
# # cv2.destroyAllWindows()
# # # rtspsrc latency=0 location=rtsp://admin:VortexROV2025@192.168.33.52:554/Streaming/Channels/101 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! video/x-raw,width=1920,height=1080 ! appsink max-buffers=1 drop=true
# #  #"rtspsrc latency=0 location=rtsp://admin:VortexROV2025@192.168.33.52:554/Streaming/Channels/101 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! videoflip video-direction=3 ! video/x-raw,width=1080,height=1920 ! appsink max-buffers=1 drop=true"
# #     # "rtspsrc latency=0 location=rtsp://admin:VortexROV2025@192.168.33.63:554/Streaming/Channels/102 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! video/x-raw,width=640,height=480 ! appsink max-buffers=1 drop=true"
# #     #   "rtspsrc latency=0 location=rtsp://admin:VortexROV2025@192.168.33.65:554/Streaming/Channels/102 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! video/x-raw,width=640,height=480 ! appsink max-buffers=1 drop=true"
# #     # "rtspsrc latency=0 buffer-mode=0 location=rtsp://admin:VortexROV2025@192.168.33.67:554/Streaming/Channels/101 ! "
# #     # "queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! "
# #     # "videoconvert ! "
# #     # "video/x-raw,width=1920,height=1080,framerate=30/1 ! appsink max-buffers=1 drop=true"
# #     # "rtspsrc latency=0 location=rtsp://admin:VortexROV2025@192.168.33.64:554/Streaming/Channels/101 ! "
# #     # "queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! "
# #     # "videoflip video-direction=4 ! video/x-raw,width=576,height=1024 ! appsink max-buffers=1 drop=true"
# import cv2
# from PySide6.QtCore import QObject, Signal ,QThread
# from PySide6.QtGui import QImage

# class CameraStream(QThread):
#     frame_ready = Signal(QImage)  # Signal to emit QImage frames

#     def __init__(self, rtsp_url):
#         """Initialize the camera stream with the RTSP URL"""
#         super().__init__()  # Initialize QObject
#         self.rtsp_url = rtsp_url
#         self.cap = cv2.VideoCapture(self.rtsp_url, cv2.CAP_GSTREAMER)
#         self.running = True  # Control loop executions

#         if not self.cap.isOpened():
#             print("Error: Failed to open RTSP stream.")
    
#     def convert_frame_to_qimage(self, frame):
#         """Convert an OpenCV BGR frame to a QImage"""
#         if frame is None:
#             return None

#         height, width, channel = frame.shape
#         bytes_per_line = 3 * width  # 3 channels (RGB)

#         # Convert BGR to RGB (since OpenCV uses BGR by default)
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         # Create QImage from frame data
#         qimg = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
#         return qimg

#     def run(self):  # Use `run` instead of `start` when using QThread
#         """Start streaming from the RTSP source without displaying OpenCV window"""
#         if not self.cap.isOpened():
#             print("Error: Cannot start streaming. RTSP stream is not opened.")
#             return

#         while self.running:
#             ret, frame = self.cap.read()
#             if not ret:
#                 print("Error: Failed to grab frame.")
#                 break  # Exit if no frames received
            
#             # Convert frame to QImage
#             qimg = self.convert_frame_to_qimage(frame)

#             # if qimg is not None:
#             #     self.frame_ready.emit(qimg)  # Emit the QImage as a signal
            
            
#             cv2.imshow("Camera Stream", frame)

#             # Press 'q' to exit (optional if controlled via GUI)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#     # Release resources when exiting
#         self.stop()


#     def stop(self):
#         """Stop streaming and release resources"""
#         self.running = False  # Stop the loop
#         self.quit()  # Quit the QThread safely
#         self.wait()


# # RTSP Stream URL
# RTSP_URL = ("rtspsrc latency=0 location=rtsp://admin:vortex2025@192.168.33.51:554/Streaming/Channels/101 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! video/x-raw,width=1920,height=1080 ! appsink")

# # Start the stream
# camera = CameraStream(RTSP_URL)
# camera.start()
import sys
import cv2
from PySide6.QtCore import Qt, Signal, QThread
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class CameraStream(QThread):
    frame_ready = Signal(QImage)  # Signal to emit QImage frames

    def __init__(self, rtsp_url):
        """Initialize the camera stream with the RTSP URL"""
        super().__init__()
        self.rtsp_url = rtsp_url
        self.cap = cv2.VideoCapture(self.rtsp_url, cv2.CAP_GSTREAMER)
        self.running = True  # Control loop executions

        if not self.cap.isOpened():
            print("Error: Failed to open RTSP stream.")

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
        """Start streaming from the RTSP source"""
        if not self.cap.isOpened():
            print("Error: Cannot start streaming. RTSP stream is not opened.")
            return

        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Failed to grab frame.")
                break  # Exit if no frames received

            # Convert frame to QImage
            qimg = self.convert_frame_to_qimage(frame)

            # Emit the QImage as a signal
            if qimg is not None:
                self.frame_ready.emit(qimg)

            # Exit on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Ensure that cleanup is done properly
        self.cleanup()

    def stop(self):
        """Stop streaming and release resources"""
        self.running = False  # Stop the loop
        self.quit()  # Quit the QThread safely
        self.wait()  # Wait for the thread to finish

    def cleanup(self):
        """Cleanup resources"""
        if self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()


class CameraWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RTSP Camera Stream")
        self.setGeometry(100, 100, 800, 600)

        # QLabel to display camera frames
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        # Layout to organize widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        # Central widget
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # RTSP URL of the camera
        self.rtsp_url = "rtspsrc latency=0 location=rtsp://admin:vortex2025@192.168.33.50:554/Streaming/Channels/101 ! decodebin ! videoconvert ! appsink"

        # Create CameraStream instance
        self.camera_stream = CameraStream(self.rtsp_url)
        self.camera_stream.frame_ready.connect(self.update_frame)  # Connect signal to update_frame method
        self.camera_stream.start()

    def update_frame(self, qimg):
        """Update the QLabel with the new frame"""
        self.label.setPixmap(QPixmap.fromImage(qimg))

    def closeEvent(self, event):
        """Handle closing of the window"""
        self.camera_stream.stop()  # Stop the camera stream thread
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraWindow()
    window.show()
    sys.exit(app.exec())
