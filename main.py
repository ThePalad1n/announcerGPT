import os
from dotenv import load_dotenv
import cv2
import numpy as np
import pyautogui
import time
from pathlib import Path
from openai import OpenAI
client = OpenAI(
        # Get the API key from the environment variable
    api_key = os.getenv('API_KEY')
)


# Set the interval between captures (in seconds).
capture_interval = 10  # Capture every 10 seconds

# The main loop
while True:
    # Capture the screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to a format that OpenCV can read
    frame = np.array(screenshot)
    # Convert the image color to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Save the captured image to disk
    # Get a timestamp for the filename
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    # Create a filename with the timestamp
    filename = f"screenshot_{timestamp}.png"
    cv2.imwrite(filename, frame)  # Save the image

    print(f"Captured {filename}")

    # Wait for the specified interval before capturing the next screenshot
    time.sleep(capture_interval)


    # Load the environment variables from the .env file
    load_dotenv()



    # Output file path for the MP3
    speech_file_path = "speech.mp3"

    # Call the OpenAI API to generate speech
    response = client.audio.speech.create(
        model="tts-1",
        voice="echo",
        input="Today is a wonderful day to build something people love!"
    )

    # Save the generated speech to an MP3 file
    with open(speech_file_path, 'wb') as f:
        f.write(response.content)
