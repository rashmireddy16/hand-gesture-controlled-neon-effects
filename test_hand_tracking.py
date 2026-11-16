
import cv2
from hand_tracking import HandTracker

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open webcam.")
    raise SystemExit

tracker = HandTracker()

print("Show your hand in front of the webcam.")
print("Press Q to exit.")

while True:

    success, frame = camera.read()

    if not success:
        print("Could not read camera.")
        break

    frame = cv2.flip(frame, 1)

    frame, landmarks = tracker.find_hands(frame)

    if landmarks:
        cv2.putText(
            frame,
            "HAND DETECTED!",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("Hand Tracking Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
tracker.close()
cv2.destroyAllWindows()
