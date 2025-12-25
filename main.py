import cv2
import time
from video_capture import get_video_stream
from motion_detector_ml import detect_motion_ml
from event_sender import send_event
from data_store import save_event

cap = get_video_stream()

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    motion_value, mask = detect_motion_ml(frame)

    if motion_value > 3000:   
        event = {
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "event_type": "ml_motion_detected",
            "value": motion_value
        }

        send_event(event)
        save_event(event)

    cv2.imshow("Video Stream", frame)
    cv2.imshow("Motion Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
