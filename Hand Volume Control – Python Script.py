# ===============================
# Hand Gesture Volume Control
# Author: [Ridham Garg]
# Description: Control system volume on macOS using hand gestures.
# ===============================

import cv2                      # OpenCV for image processing and webcam
import mediapipe as mp          # MediaPipe for hand tracking
import os                       # For running AppleScript commands on macOS

# Initialize variables to hold fingertip coordinates
x1 = y1 = x2 = y2 = 0

# Open the default webcam (0)
webcam = cv2.VideoCapture(0)

# Initialize the MediaPipe Hands model
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils  # Utility for drawing hand landmarks

# Start an infinite loop to capture frames from the webcam
while True:
    _, image = webcam.read()  # Read a frame
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
    output = my_hands.process(rgb_image)  # Process the frame to detect hands
    hands = output.multi_hand_landmarks   # Extract landmark information

    # If hand(s) detected
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)  # Draw hand landmarks
            x1 = y1 = x2 = y2 = None  # Reset landmark coordinates each frame

            for id, lm in enumerate(hand.landmark):  # Iterate through landmarks
                x = int(lm.x * image.shape[1])  # Scale normalized x to image width
                y = int(lm.y * image.shape[0])  # Scale normalized y to image height

                if id == 8:  # Index fingertip
                    cv2.circle(image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    x1, y1 = x, y

                if id == 4:  # Thumb tip
                    cv2.circle(image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                    x2, y2 = x, y

            # If both thumb and index are detected
            if x1 is not None and x2 is not None:
                cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 3)  # Draw line between them
                distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 / 4  # Calculate distance

                # Control macOS volume using AppleScript
                if distance > 50:
                    os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'")
                else:
                    os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'")

    # Show the result frame
    cv2.imshow('Hand Volume control', image)

    # Break the loop on pressing ESC (key code 27)
    key = cv2.waitKey(10)
    if key == 27:
        break

# Release resources
webcam.release()
cv2.destroyAllWindows()
