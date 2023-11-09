from IPython.display import display, Image, Audio
import cv2
import base64
import time
import openai
import os
import requests

# # Ensure your OPENAI_API_KEY is set in your .env and loaded with python-dotenv
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("API_KEY")  # Set OpenAI API key globally


def main():
    # Extract frames from a video with OpenCV
    video = cv2.VideoCapture("Input\testvid.mp4")
    base64Frames = []
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
    video.release()
    print(len(base64Frames), "frames read.")

    # Assuming you have a way of generating the script from GPT
    script = "Your generated script goes here."

    # Use TTS API to generate the voiceover audio
    response = requests.post(
        "https://api.openai.com/v1/audio/speech",
        headers={
            "Authorization": f"Bearer {os.getenv('API_KEY')}"
        },
        json={
            "model": "tts-1",  # Assuming 'tts-1' is the correct TTS model
            "input": script,
            "voice": "onyx",
        }
    )

    if response.status_code == 200:
        # If the request was successful, save the audio file
        audio_filename = 'voiceover.mp3'
        with open(audio_filename, 'wb') as audio_file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                audio_file.write(chunk)
        print(f"Voiceover saved to {audio_filename}")
    else:
        # If the request failed, display the error message
        print("Failed to generate voiceover:", response.text)


if __name__ == '__main__':
    main()