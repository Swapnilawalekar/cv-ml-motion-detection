import cv2


bg_model = cv2.createBackgroundSubtractorMOG2(
    history=100,
    varThreshold=40,
    detectShadows=False
)

def detect_motion_ml(frame):
    fg_mask = bg_model.apply(frame)

    
    _, thresh = cv2.threshold(fg_mask, 200, 255, cv2.THRESH_BINARY)

    motion_pixels = cv2.countNonZero(thresh)
    return motion_pixels, thresh
