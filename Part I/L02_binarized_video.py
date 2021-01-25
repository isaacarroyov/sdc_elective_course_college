import numpy as np
import cv2 as cv
import time

#==================================== FUNCTIONS =====================================
#....................................................................................
def binarization(image, size = (480,240)):
    img_gray = cv.cvtColor(src = image, code = cv.COLOR_BGR2GRAY)
    img_gauss = cv.GaussianBlur(src = img_gray, ksize =  (5,5), sigmaX = 0)
    thr, img_thr = cv.threshold( img_gauss, 160, 255, cv.THRESH_BINARY)
    img_r = cv.resize( src = img_thr, dsize = size, interpolation = cv.INTER_NEAREST)
    return (img_r)

#==================================== PARAMETERS =====================================

#==================================== CODE =====================================
video = cv.VideoCapture("data/video_road.mp4")
while(video.isOpened()):
    ret, frame = video.read()
    if ret:
        cv.imshow("Original video", frame)
        img_bin = binarization(frame)
        cv.imshow("Binarized video", img_bin)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
video.release()
cv.destroyAllWindows()
