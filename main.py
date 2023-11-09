# from IPython.display import display, Image, Audio
# import cv2
# import base64
# import time
# import openai
# import os
# import requests

# # # Ensure your OPENAI_API_KEY is set in your .env and loaded with python-dotenv
# from dotenv import load_dotenv
# load_dotenv()

# openai.api_key = os.getenv("API_KEY")  # Set OpenAI API key globally


# def main():
#     # Extract frames from a video with OpenCV
#     video = cv2.VideoCapture("Input\testvid.mp4")
#     base64Frames = []
#     while video.isOpened():
#         success, frame = video.read()
#         if not success:
#             break
#         _, buffer = cv2.imencode(".jpg", frame)
#         base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
#     video.release()
#     print(len(base64Frames), "frames read.")

#     # Assuming you have a way of generating the script from GPT
#     script = "Your generated script goes here."

#     # Use TTS API to generate the voiceover audio
#     response = requests.post(
#         "https://api.openai.com/v1/audio/speech",
#         headers={
#             "Authorization": f"Bearer {os.getenv('API_KEY')}"
#         },
#         json={
#             "model": "tts-1",  # Assuming 'tts-1' is the correct TTS model
#             "input": script,
#             "voice": "onyx",
#         }
#     )

#     if response.status_code == 200:
#         # If the request was successful, save the audio file
#         audio_filename = 'voiceover.mp3'
#         with open(audio_filename, 'wb') as audio_file:
#             for chunk in response.iter_content(chunk_size=1024 * 1024):
#                 audio_file.write(chunk)
#         print(f"Voiceover saved to {audio_filename}")
#     else:
#         # If the request failed, display the error message
#         print("Failed to generate voiceover:", response.text)


# if __name__ == '__main__':
#     main()from moviepy.editor import VideoFileClip
import os
import requests
import openai
from moviepy.editor import VideoFileClip

api_key = os.getenv('API_KEY')
openai.api_key = api_key


def take_screenshots_and_analyze(video_path, interval=10, output_folder='screenshots'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the video file into a video clip object
    video_clip = VideoFileClip(video_path)
    duration = video_clip.duration

    for i in range(0, int(duration), interval):
        output_image_path = os.path.join(output_folder, f'screenshot_{i}.png')

        # Save the frame of the video at time 'i'
        video_clip.save_frame(output_image_path, t=i)

        # Analyze the image (assuming analyze_image_with_openai takes a file path)
        analysis_result = analyze_image_with_openai(output_image_path)
        print(f'Analysis for screenshot_{i}.png:', analysis_result)

    # Don't forget to close the video clip to free resources
    video_clip.close()


def analyze_image_with_openai(image_url):
    response = openai.Completion.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        },
                    },
                ],
            }
        ],
        max_tokens=3000,
    )

    return response.choices[0].message['content']


def text_to_speech(text):
    response = requests.post(
        "https://api.openai.com/v1/audio/speech",
        headers={
            "Authorization": f"Bearer {openai.api_key}"
        },
        json={
            "model": "tts-1",
            "input": text,
            "voice": "echo",
        }
    )

    if response.status_code == 200:
        audio_filename = 'voiceover.mp3'
        with open(audio_filename, 'wb') as audio_file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                audio_file.write(chunk)
        print(f"Voiceover saved to {audio_filename}")
    else:
        print("Failed to generate voiceover:", response.text)


def main():
    # Replace with the path to your video file
    video_path = "testvid.mp4"
    take_screenshots_and_analyze(video_path)

    # Combine the entire script into a single string
    script = ""  # Include the actual code as a string
    text_to_speech(script)


if __name__ == '__main__':
    main()
