
import cv2
import mediapipe as mp
import pygame
import numpy as np

print("OpenCV version:", cv2.__version__)
print("MediaPipe version:", mp.__version__)
print("Pygame version:", pygame.version.ver)
print("NumPy version:", np.__version__)

if not hasattr(mp, "solutions"):
    print("MediaPipe hand tracking is not available.")
    raise SystemExit

print("MediaPipe hand tracking is available!")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Could not open the webcam.")
    raise SystemExit

print("Webcam opened successfully!")
print("Press Q to close the webcam window.")

while True:
    success, frame = camera.read()

    if not success:
        print("Could not read webcam frame.")
        break

    frame = cv2.flip(frame, 1)

    cv2.putText(
        frame,
        "Webcam Test - Press Q to Exit",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow("Hand Gesture Project - Webcam Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

print("Webcam test completed!")
