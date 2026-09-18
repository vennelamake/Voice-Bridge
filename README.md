
````markdown
# Voice Bridge

Voice Bridge is an assistive communication web application designed to bridge communication gaps through **Text-to-Speech, Speech-to-Text, and Sign Language Recognition**.

The application combines web technologies, speech APIs, computer vision, and machine learning to provide multiple communication modes through a single platform.

## Overview

Voice Bridge provides three main communication modules:

- **Text-to-Speech** – Converts written text into spoken audio.
- **Speech-to-Text** – Converts spoken language into written text.
- **Sign Language Recognition** – Recognizes predefined hand gestures in real time using a webcam and a trained machine learning model.

The application is developed using **Python and Flask** for the backend, with **HTML, CSS, and JavaScript** for the user interface.

## Features

### 🗣️ Text-to-Speech

Converts user-entered text into spoken audio using the browser's **Web Speech API – SpeechSynthesis**.

- Text input through a web interface
- Browser-based speech synthesis
- Language and voice selection
- No additional audio-processing hardware required

### 🎙️ Speech-to-Text

Converts spoken language into text using the browser's **Web Speech API – SpeechRecognition**.

- Microphone-based speech input
- Real-time speech recognition
- Language selection
- Recognized speech displayed as text
- Speech history within the interface

### 🤟 Sign Language Recognition

Recognizes predefined hand gestures in real time using a webcam.

The recognition process uses **MediaPipe Hands** to detect hand landmarks and a trained **TensorFlow/Keras** model to classify the detected gesture.

### Supported Gestures

| No. | Gesture |
|-----|---------|
| 1 | Okay |
| 2 | Peace |
| 3 | Thumbs Up |
| 4 | Thumbs Down |
| 5 | Call Me |
| 6 | Stop |
| 7 | Rock |
| 8 | Live Long |
| 9 | Fist |
| 10 | Smile |

## System Architecture

```text
                         Voice Bridge
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
       Text-to-Speech   Speech-to-Text   Sign Language
                                             Recognition
             │                │                │
             ▼                ▼                ▼
       Speech Synthesis  Speech Recognition  Webcam
                                              │
                                              ▼
                                         MediaPipe
                                              │
                                              ▼
                                      Hand Landmarks
                                              │
                                              ▼
                                      TensorFlow/Keras
                                              │
                                              ▼
                                      Gesture Prediction
````

## Technology Stack

| Category         | Technologies            |
| ---------------- | ----------------------- |
| Frontend         | HTML5, CSS3, JavaScript |
| Backend          | Python, Flask           |
| Computer Vision  | OpenCV, MediaPipe       |
| Machine Learning | TensorFlow, Keras       |
| Browser APIs     | Web Speech API          |

## Project Structure

```text
voicebridge/
│
├── mp_hand_gesture/
│   ├── variables/
│   ├── keras_metadata.pb
│   └── saved_model.pb
│
├── templates/
│   ├── gesture.html
│   ├── modhome.html
│   ├── modstotwithlang.html
│   └── modttos.html
│
├── app.py
├── gesture.names
├── TechVidvan-hand_gesture_detection.py
├── .gitignore
└── README.md
```

### Key Files

* **`app.py`** – Main Flask application that handles routing, webcam streaming, hand detection, and gesture prediction.
* **`mp_hand_gesture/`** – Contains the trained TensorFlow/Keras model used for gesture classification.
* **`gesture.names`** – Contains the gesture class names used by the model.
* **`templates/`** – Contains the HTML pages for the application modules.
* **`TechVidvan-hand_gesture_detection.py`** – Standalone implementation for testing the gesture recognition system.
* **`.gitignore`** – Prevents environment-specific and generated files from being committed.

## Application Workflow

### Text-to-Speech

```text
User enters text
       ↓
Web Interface
       ↓
Speech Synthesis API
       ↓
Spoken Audio
```

### Speech-to-Text

```text
User speaks
       ↓
Microphone
       ↓
Speech Recognition API
       ↓
Recognized Text
```

### Sign Language Recognition

```text
Webcam
   ↓
OpenCV Video Capture
   ↓
MediaPipe Hand Detection
   ↓
21 Hand Landmarks
   ↓
TensorFlow/Keras Model
   ↓
Gesture Classification
   ↓
Predicted Gesture
```

## Installation

### Prerequisites

* Python 3.11
* Git
* Webcam
* Microphone
* Modern web browser

Python 3.11 is recommended for compatibility with the machine learning dependencies.

### 1. Clone the Repository

```bash
git clone <repository-url>
cd voicebridge
```

### 2. Create a Virtual Environment

```bash
py -3.11 -m venv venv
```

### 3. Activate the Environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install numpy==1.26.4 opencv-python==4.10.0.84 mediapipe==0.10.21 tensorflow==2.15.1 flask
```

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000/
```

Allow **camera and microphone permissions** when requested by the browser.

## Browser Requirements

The Text-to-Speech and Speech-to-Text modules depend on browser-supported Web Speech APIs.

For proper functionality:

* Use a modern web browser.
* Allow microphone access for Speech-to-Text.
* Allow camera access for Sign Language Recognition.
* Ensure the microphone and webcam are working correctly.

Browser support for individual Web Speech API features may vary.

## Future Enhancements

* Expand the number of supported sign language gestures
* Support continuous sign language sentence recognition
* Improve gesture recognition accuracy
* Add support for more languages
* Improve accessibility and user interface design
* Deploy the application as a cloud-based service

## License

This project is developed for educational and project demonstration purposes.

```
```
