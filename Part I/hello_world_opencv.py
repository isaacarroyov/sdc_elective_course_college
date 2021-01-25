import cv2 as cv

img = cv.imread('data/hello_world.png')
cv.imshow("Hello world!", img)
cv.waitKey(0)
cv.destroyAllWindows()
print('Hello a to2')
