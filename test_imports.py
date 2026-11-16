
import cv2
import mediapipe as mp
import pygame
import numpy as np

print("Python libraries imported successfully!")

print("OpenCV version:", cv2.__version__)
print("MediaPipe version:", mp.__version__)
print("Pygame version:", pygame.version.ver)
print("NumPy version:", np.__version__)

# Check the MediaPipe hand tracking API
print("MediaPipe Hands available:", hasattr(mp, "solutions"))

print("\nInstallation verification completed!")
