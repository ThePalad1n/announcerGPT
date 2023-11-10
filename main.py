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


import base64
import requests

import openai

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Retrieve the API_KEY
api_key = os.getenv("API_KEY")


#Function to encode the image to base64
def encode_image(filename):
    with open(filename, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to send the image to the OpenAI API and get the description
def get_image_description(base64_image):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Format the base64 string as a data URI
    data_uri = f"data:image/jpeg;base64,{base64_image}"

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe the image like an announcer for a broadcast."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": data_uri
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    description_text(response.json())

def description_text(x):    # Extracting the 'content' from the first 'choice' in the 'choices' list,
    # no matter what the 'id' is
    if 'choices' in x and x['choices']:
        # This checks if 'choices' exists and is not empty
        first_choice = x['choices'][0]
        
        if 'message' in first_choice and 'content' in first_choice['message']:
            # Assuming each 'choice' has a 'message' with 'content'
            content_text = first_choice['message']['content']
            print(content_text)
            return content_text
        else:
            print("The 'message' or 'content' key is missing in the first choice.")
    else:
        print("The 'choices' key is missing in the response or is empty.")

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

    timestamp = time.strftime("%Y%m%d-%H%M%S")  # Get a timestamp for the filename
    filename = f"image_{timestamp}.png"  # Create a filename with the timestamp

    cv2.imwrite(filename, frame)  # Save the image

    print(f"Captured {filename}")
    base64_image = encode_image(filename)
    # Get the description of the image
    get_image_description(base64_image)
   

    time.sleep(capture_interval)

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

    time.sleep(capture_interval)

