import cv2

def get_video_stream():
    cap = cv2.VideoCapture(0)
    return cap
