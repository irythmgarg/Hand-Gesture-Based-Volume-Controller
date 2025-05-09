# Hand-Gesture-Based-Volume-Controller

# 🖐️ Hand Gesture Volume Control

Control your **macOS system volume** using simple hand gestures via webcam. This project uses **OpenCV**, **MediaPipe**, and **AppleScript** for real-time fingertip tracking and volume control.

---

## 📸 Demo

> Add a GIF or screenshot here showing the thumb and index fingers adjusting volume.

---

## ✨ Features

- Real-time hand tracking using webcam
- Tracks **thumb tip** and **index fingertip** distance
- Adjusts **system volume** (macOS) using gestures:
  - 🟢 Fingers **apart** → Volume increases
  - 🔴 Fingers **close** → Volume decreases

---

## 🧰 Tech Stack

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://google.github.io/mediapipe/)
- [AppleScript (via `os.system`)] for controlling macOS volume
- Python 3.7+

---

🖥️ Platform Support
✅ macOS (volume control uses AppleScript)

⚠️ Windows/Linux users can adapt this by replacing AppleScript with OS-specific volume control commands.

---

🚀 Future Improvements
Smooth volume mapping from finger distance (0–100%)

Add sound feedback or on-screen volume level

Cross-platform volume control

Use time-based delay to avoid rapid volume changes

---

🙌 Credits
MediaPipe for hand detection

OpenCV for image processing

---

📜 License
This project is open-source and available under the MIT License.
