import cv2

# Define the GStreamer pipeline
gst_pipeline = (
    "rtspsrc latency=0 location=rtsp://admin:vortex2025@192.168.33.54:554/Streaming/Channels/101 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! video/x-raw,width=1920,height=1080 ! appsink"
    # "rtspsrc latency=0 location=rtsp://admin:VortexROV2025@192.168.33.63:554/Streaming/Channels/102 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! video/x-raw,width=640,height=480 ! appsink max-buffers=1 drop=true"
    #   "rtspsrc latency=0 location=rtsp://admin:VortexROV2025@192.168.33.65:554/Streaming/Channels/102 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! video/x-raw,width=640,height=480 ! appsink max-buffers=1 drop=true"
    # "rtspsrc latency=0 buffer-mode=0 location=rtsp://admin:VortexROV2025@192.168.33.67:554/Streaming/Channels/101 ! "
    # "queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! "
    # "videoconvert ! "
    # "video/x-raw,width=1920,height=1080,framerate=30/1 ! appsink max-buffers=1 drop=true"
    # "rtspsrc latency=0 location=rtsp://admin:VortexROV2025@192.168.33.64:554/Streaming/Channels/101 ! "
    # "queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! "
    # "videoflip video-direction=4 ! video/x-raw,width=576,height=1024 ! appsink max-buffers=1 drop=true"
)

# Open the GStreamer pipeline
cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Error: Unable to open GStreamer pipeline.")
    exit()

# Main loop to read and display frames
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to retrieve frame from GStreamer pipeline.")
        break
    frame = cv2.resize(frame, (576, 1024))
    cv2.imshow("720p RTSP Camera Feed", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()


# rtspsrc latency=0 location=rtsp://admin:VortexROV2025@192.168.33.63:554/Streaming/Channels/101 ! queue max-size-buffers=0 max-size-bytes=0 max-size-time=0 ! decodebin ! videoconvert ! video/x-raw,width=1920,height=1080 ! appsink max-buffers=1 drop=true