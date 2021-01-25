import cv2 as cv
import matplotlib.pyplot as plt
plt.style.use('seaborn-paper')
plt.rc('font', family='serif')

#load image
road = cv.imread('data/road.jpg')

#conversion to greyscale
road_gray = cv.cvtColor( src = road, code = cv.COLOR_BGR2GRAY )

#gaussian filter
road_gaussianBlur = cv.GaussianBlur( src = road_gray, ksize = (33,33), sigmaX = 1, sigmaY = 1)

#threshold
thr, road_thr = cv.threshold( road_gaussianBlur, 200, 255, cv.THRESH_BINARY)

#resize
ratio = 0.033
height, width = road_thr.shape
road_r = cv.resize( road_thr, ( int(width*ratio), int(height*ratio) ), interpolation = cv.INTER_NEAREST)

#plot the results
plt.figure( figsize = (15,13), facecolor = '#FFFFFF' )
plt.axes().set_facecolor('#FFFFFF')

plt.subplot( 2, 3, 1 )
plt.title('Original image', size = 15, pad = 10)
plt.imshow( road )

plt.subplot( 2, 3, 2 )
plt.title('B/W road', size = 15, pad = 10)
plt.imshow( road_gray, cmap = 'gray' )

plt.subplot( 2, 3, 3 )
plt.title('B/W road + Gaussian filter', size = 15, pad = 10)
plt.imshow( road_gaussianBlur, cmap = 'gray' )

plt.subplot( 2, 3, 4 )
plt.title('B/W road + Gaussian filter + \n thresholding', size = 15, pad = 10)
plt.imshow( road_thr, cmap = 'gray' )

plt.subplot( 2, 3, 5 )
plt.title('Smaller road', size = 15, pad = 10)
plt.imshow( road_r, cmap = 'gray' )

plt.show()
