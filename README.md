# Image Description and Speech Synthesis Program

This Python program captures screenshots of your computer screen at regular intervals and uses artificial intelligence to generate descriptions of these images. It also converts the generated descriptions into speech. This program can be useful for providing real-time descriptions of what is happening on your screen, making it accessible for visually impaired individuals or for various automation tasks.

## Prerequisites
Before running this program, make sure you have the following prerequisites installed and set up:

1. Python: Ensure you have Python installed on your system.

2. Required Python packages: Install the necessary Python packages using the following commands:

   ```
   pip install os-dotenv
   pip install opencv-python
   pip install numpy
   pip install pyautogui
   pip install openai
   pip install requests
   ```

3. OpenAI API Key: You'll need an API key from OpenAI to access their services. You can obtain this key from [OpenAI's website](https://beta.openai.com/signup/).

4. `.env` file: Create a `.env` file in the same directory as this program and add your OpenAI API key like this:

   ```
   API_KEY=your-api-key-here
   ```

## How the Program Works
This program performs the following steps:

1. Captures a screenshot of your screen at regular intervals (specified by `capture_interval`).

2. Converts the screenshot into a format that OpenAI can process.

3. Sends the image to the OpenAI API to generate a textual description.

4. Converts the generated text description into speech using the OpenAI TTS (Text-to-Speech) API.

5. Saves the generated speech as an MP3 file.

6. Repeats this process indefinitely in a loop.

## Usage
1. Configure the program with your OpenAI API key by adding it to the `.env` file.

2. Set the `capture_interval` variable to control how often you want to capture screenshots (in seconds).

3. Run the program using the following command:

   ```
   python your_program_name.py
   ```

4. The program will continuously capture screenshots and provide spoken descriptions based on the content of the screen.

## Note
- The program uses the OpenAI API for both image description and speech synthesis. Be mindful of API usage limits and costs associated with API calls.

- You can customize the description prompt within the `get_image_description` function to suit your specific needs.

- The program saves the generated speech as "speech.mp3" in the same directory as the program.

- Ensure that you have a working internet connection and that the OpenAI API key is correctly configured in the `.env` file for the program to function properly.

- You can modify the program to handle exceptions and errors gracefully based on your requirements.

Feel free to adjust the program to fit your needs or use it as a starting point for more advanced automation tasks.


# Test cases and Implementations:

## League of Legends Gameplay

I did a test with a bit of league gameplay from 2020 and ran the program while screen recording.

Inside the [leagueTest folder](https://github.com/ThePalad1n/announcerGPT/tree/main/leagueTest) youll find the screenshots the program made along with the audio file that was generated from the api.

I then combined them without trimming using an online tool and it generated this [screen recording combined with audio](https://drive.google.com/file/d/1n4PswS76Umk4U10BV1bAZiiqcm7ozZsm/view?usp=sharing)

## Future Implementations

Some applications making it accessible for visually impaired individuals or for various automation tasks.
