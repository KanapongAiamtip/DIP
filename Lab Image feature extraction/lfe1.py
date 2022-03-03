import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt
 
img = cv.imread('Lab Image feature extraction/sign4.jpg')
img = cv.resize(img,None,fx=0.3,fy=0.3)

blurimage = cv.medianBlur(img, 5)

HSV = cv.cvtColor(blurimage, cv.COLOR_BGR2HSV)

lower_color = np.array([[20,100,100],[30,50,50]])  
upper_color = np.array([[27,255,255],[120,255,255]])

for ppromxx in range(len(lower_color)):
    mask = cv.inRange(HSV,lower_color[ppromxx],upper_color[ppromxx])
    circles = cv.HoughCircles(mask, cv.HOUGH_GRADIENT, 1, 40, param1=255, param2=13,minRadius=13, maxRadius=50)
if circles is None:
    print('red traffic signal')
else:
    print('green traffic signal')

imgRGB =  cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.subplot(1,1,1),plt.imshow(imgRGB)
plt.show()