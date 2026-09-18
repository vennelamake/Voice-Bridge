from flask import Flask, render_template, Response
import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model

app = Flask(__name__)

# -----------------------------
# Load Gesture Recognition Model
# -----------------------------
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)

mpDraw = mp.solutions.drawing_utils

model = load_model("mp_hand_gesture")

with open("gesture.names", "r") as f:
    classNames = f.read().splitlines()


# -----------------------------
# Webcam
# -----------------------------
camera = cv2.VideoCapture(0)


def generate_frames():
    while True:
        success, frame = camera.read()

        if not success:
            break

        # Flip camera
        frame = cv2.flip(frame, 1)

        # Convert BGR → RGB
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hand
        result = hands.process(framergb)

        className = ""

        if result.multi_hand_landmarks:

            landmarks = []

            for handslms in result.multi_hand_landmarks:

                for lm in handslms.landmark:
                    lmx = int(lm.x * frame.shape[1])
                    lmy = int(lm.y * frame.shape[0])

                    landmarks.append([lmx, lmy])

                # Draw hand landmarks
                mpDraw.draw_landmarks(
                    frame,
                    handslms,
                    mpHands.HAND_CONNECTIONS
                )

                # Predict gesture
                prediction = model.predict(
                    [landmarks],
                    verbose=0
                )

                classID = np.argmax(prediction)

                className = classNames[classID]

        # Display gesture name
        cv2.putText(
            frame,
            className,
            (10, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
            cv2.LINE_AA
        )

        # Convert frame to JPEG
        ret, buffer = cv2.imencode(".jpg", frame)

        frame = buffer.tobytes()

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + frame
            + b"\r\n"
        )


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("modhome.html")


# -----------------------------
# Text to Speech
# -----------------------------
@app.route("/ttos")
def ttos():
    return render_template("modttos.html")


# -----------------------------
# Speech to Text
# -----------------------------
@app.route("/stot")
def stot():
    return render_template("modstotwithlang.html")


# -----------------------------
# Sign Language Page
# -----------------------------
@app.route("/run_gesture")
def run_gesture():
    return render_template("gesture.html")


# -----------------------------
# Webcam Video
# -----------------------------
@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


# -----------------------------
# Start Flask
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)