import cv2
import numpy as np
import pyautogui
import time

# Set the interval between captures (in seconds).
capture_interval = 10  # Capture every 10 seconds

# The main loop
while True:
    # Capture the screen
    screenshot = pyautogui.screenshot()
    
    # Convert the screenshot to a format that OpenCV can read
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert the image color to BGR
    
    # Save the captured image to disk
    timestamp = time.strftime("%Y%m%d-%H%M%S")  # Get a timestamp for the filename
    filename = f"screenshot_{timestamp}.png"  # Create a filename with the timestamp
    cv2.imwrite(filename, frame)  # Save the image
    
    print(f"Captured {filename}")

    # Wait for the specified interval before capturing the next screenshot
    time.sleep(capture_interval)
