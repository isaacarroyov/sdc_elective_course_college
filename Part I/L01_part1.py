import cv2 as cv
import matplotlib.pyplot as plt
plt.style.use('seaborn-paper')
plt.rc('font', family='serif')

#read/load image
img = cv.imread('data/uxmal.jpg')

#change BGR -> RGB
img_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)

#conversion to greyscale
img_gray = cv.cvtColor(img, code = cv.COLOR_BGR2GRAY)

#median filter
img_medianBlur = cv.medianBlur(img_gray, ksize = 23)

#applying threshold
thr, img_thr = cv.threshold(img_medianBlur, 150, 255,cv.THRESH_BINARY)

#resize image
ratio = 0.02
height, width, canales = img.shape

img_r = cv.resize(img_thr, ( int(width*ratio), int(height*ratio) ), interpolation = cv.INTER_NEAREST)

#plot the results
plt.figure( figsize = (15, 8), facecolor = '#FFFFFF' )
plt.axes().set_facecolor('#FFFFFF')

#original image
plt.subplot( 2, 3 , 1 )
plt.title( 'Original image (BGR channel)')
plt.imshow(img)

#RGB image
plt.subplot( 2, 3 , 2 )
plt.title( 'Uxmal in RGB channel')
plt.imshow(img_rgb)

#greyscale image
plt.subplot( 2, 3 , 3 )
plt.title( 'B/W Uxmal')
plt.imshow(img_gray, cmap = 'gray')

#image with medina filter
plt.subplot( 2, 3 , 4 )
plt.title( 'B/W + median filter')
plt.imshow(img_medianBlur, cmap = 'gray')

#threshold
plt.subplot( 2, 3 , 5 )
plt.title( 'B/W + median filter + threshold(=150)')
plt.imshow(img_thr, cmap = 'gray')

#resized image
plt.subplot( 2, 3 , 6 )
plt.title( 'Smaller image')
plt.imshow(img_r, cmap = 'gray')

plt.show()
