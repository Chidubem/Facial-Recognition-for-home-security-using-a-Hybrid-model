import cv2
import time
from send_email_alert import send_email_alert

# Simulate known face check (in practice, use a real face recognition model)
def is_unknown_face(frame):
    # For demo purposes, always returns True
    return True

# Set recipient email address
recipient_email = "recipient@example.com"

# Open webcam
cap = cv2.VideoCapture(0)

# Track when the last alert was sent
last_alert_time = 0
alert_interval = 30  # seconds between alerts

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # If unknown face detected and enough time has passed, send alert
    if is_unknown_face(frame):
        current_time = time.time()
        if current_time - last_alert_time > alert_interval:
            send_email_alert(recipient_email=recipient_email)
            last_alert_time = current_time

    # Show the camera feed
    cv2.imshow("Camera", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
