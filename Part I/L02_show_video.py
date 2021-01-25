import numpy as np
import cv2 as cv
import time

video = cv.VideoCapture("data/video_road.mp4")
while(video.isOpened()):
    ret, frame = video.read()
    if ret:
        cv.imshow("Original video", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
video.release()
cv.destroyAllWindows()
