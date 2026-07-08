# Real-Time Face Detection with OpenCV

## 📌 Overview
This project demonstrates **real-time face detection and tracking** using Python and OpenCV’s built-in Haar Cascade Classifier.  
It connects to your webcam, detects multiple faces simultaneously, and highlights them with bounding boxes and labels.

## 🚀 Features
- Live face detection via webcam  
- Tracks multiple faces at once  
- Uses OpenCV’s Haar Cascade (no external libraries like dlib/mediapipe)  
- Lightweight and easy to run  

## 🛠️ Installation & Setup
1. Install [Python 3.x](https://www.python.org/downloads/)  
2. Install OpenCV:
   ```bash
   pip install opencv-python

##Clone this repository:

bash
git clone https://github.com/your-username/real-time-face-detection.git

cd real-time-face-detection

##Run the script:

bash
python face_detection.py

##🎯 Usage
The webcam feed opens automatically.

Detected faces are marked with green rectangles and labeled (Face #1, Face #2, etc.).

Press q to quit safely.

##📷 Demo
When you run the program, you’ll see something like this:

Code
[ Webcam window with faces highlighted ]

##📖 Tech Stack
Language: Python

Library: OpenCV (cv2)

Model: Haar Cascade Classifier


##✨ Future Improvements
Add drowsiness/sleep detection

Integrate sound alerts for fatigue monitoring

Extend to emotion recognition
