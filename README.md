# Real-Time Motion Detection using ML and OpenCV

## Objective
To build a real-time computer vision pipeline that detects motion from a video stream,
generates events, and sends them to a backend service.

## Approach
- Captured live video using OpenCV
- Applied ML-based background subtraction (MOG2)
- Detected motion using foreground pixel intensity
- Generated structured events with timestamp, event type, and value
- Sent events to a Flask backend using REST API
- Stored events locally in CSV format

## Image Processing Technique
Background Subtraction (MOG2) followed by binary thresholding.

## Project Structure

cv_event_detection/
├── main.py
├── video_capture.py
├── motion_detector_ml.py
├── event_sender.py
├── data_store.py
├── backend.py
├── events.csv


## How to Run
1. Install dependencies:
    pip install -r requirements.txt
2. Run backend:
    python backend.py
3. Run application:
    python main.py



## Output
- Detects motion in real time
- Generates JSON events
- Displays video and motion mask
- Logs events in backend console and CSV file

## Assumptions
- Default webcam is available
- Backend runs on localhost

## Improvements
- WebSocket communication
- Object detection
- Dashboard visualization
- Database storage

## Author
Swapnil Awalekar
