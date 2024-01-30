import cv2
import streamlit as st
from datetime import datetime

# Set the title of the Streamlit app
st.title('Motion Detector Webcam')

# Create a button to start the camera
start = st.button('Start Camera')

# Check if the "Start Camera" button is pressed
if start:
    # Create a Streamlit image placeholder
    streamlit_image = st.image([])

    # Open the webcam (camera index 0)
    camera = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        check, frame = camera.read()

        # Convert the BGR frame to RGB color space for displaying in Streamlit
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get the current date and time
        now = datetime.now()

        # Add a text overlay with the day of the week on the frame
        cv2.putText(img=frame, text=now.strftime("%A"), org=(30, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)

        # Add a text overlay with the time on the frame
        cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(30, 140),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)

        # Display the frame with the text overlays in Streamlit
        streamlit_image.image(frame)
