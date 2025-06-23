# Face-Recognition-System

This project performs **real-time face recognition** using the webcam feed. It uses Python, OpenCV, and the `face_recognition` library to detect and identify a known face in the live video stream.

---

## 🔧 Technologies Used

- Python
- OpenCV (`opencv-python`)
- face_recognition

---

## 🚀 Features

- Real-time face detection from webcam
- Recognizes and matches faces with a preloaded image
- Displays bounding boxes and name labels
- Highlights recognized face in **green**, unknown faces in **red**

---

## 🧠 How It Works

1. A reference image (`sona.jpg`) is loaded and encoded.
2. Webcam captures real-time frames.
3. Detected faces in each frame are compared with the reference encoding.
4. If a match is found, the face is labeled with the person's name (`Sona`).
5. Non-matching faces are labeled as `Unknown`.

##Install Required Libraries
pip install opencv-python face_recognition
