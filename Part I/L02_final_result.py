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
#....................................................................................
def poly_interest(image, pt = [ (135,150), (350, 150), (380, 238), (115, 238) ], color = (100,100,100), closed = True):
    polygon_vert = np.array(pt)
    polygon_vert = polygon_vert.reshape((-1,1,2))
    return cv.polylines(image, [polygon_vert], closed, color)
#....................................................................................
def region_interest(image, pt = [ (135,150), (350, 150), (115, 238), (380, 238) ], pref_size = (480, 240) ):
    pts1 = np.float32( pt )
    pts2 = np.float32( [ [0,0], [pref_size[0], 0], [0, pref_size[1]], pref_size ] )
    matrix = cv.getPerspectiveTransform( pts1, pts2 )
    img_wrap = cv.warpPerspective( image, matrix, pref_size )
    return (img_wrap)
#....................................................................................
def mid_point( image ):
    close_up = image[ 220:, : ]
    sum_columns = close_up.sum(axis=0)
    indexes = np.arange( len(sum_columns) )
    midPoint = int( np.dot(indexes, sum_columns)/np.sum(sum_columns) )
    return midPoint
#....................................................................................
def left_sum( image, midpoint ):
    return np.round(np.sum( image[:, :midpoint].sum(axis = 0) )/(255*image.shape[0]*image.shape[1]),2)
#....................................................................................
def right_sum( image, midpoint ):
    return np.round(np.sum( image[:, midpoint:].sum(axis = 0) )/(255*image.shape[0]*image.shape[1]),2)
#==================================== PARAMETERS =====================================
font = cv.FONT_HERSHEY_TRIPLEX

org1 = (60, 185)
org2 = (370, 185)
org3 = (200, 100)

fontScale = 0.7

colour = (150, 150, 150)

thickness = 1
#==================================== CODE =====================================
video = cv.VideoCapture('data/video_road_v2.mp4')
while(video.isOpened()):
    ret, frame = video.read()
    if ret:
        cv.imshow("Original video", frame)
        img_bin = binarization(frame)
        img_bin = poly_interest(image=img_bin)
        cv.imshow("Binarized video", img_bin)
        img_interest = region_interest(image=img_bin)
        midPoint = mid_point(img_interest)
        left = left_sum(img_interest, midPoint)
        right = right_sum(img_interest, midPoint)
        cv.putText(img_interest, str(left), org1, font, fontScale,
                 colour, thickness, cv.LINE_AA, False)
        cv.putText(img_interest, str(right), org2, font, fontScale,
                 colour, thickness, cv.LINE_AA, False)
        delta = left - right
        if delta > 0.05:
            heading = "Left"
        elif delta < 0.05:
            heading = "Right"
        else:
            heading = "Straight"
        cv.putText(img_interest, heading, org3, font, fontScale,
                 colour, thickness, cv.LINE_AA, False)
        cv.circle(img_interest, (midPoint,235),5,(100,100,100),-1)
        cv.imshow("Aerial view", img_interest)
        time.sleep(0.00000001)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
video.release()
cv.destroyAllWindows()
