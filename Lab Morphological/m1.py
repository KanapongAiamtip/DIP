import cv2 as cv
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Lab Morphological/water_coins.jpg')
grayimage = cv2.imread('Lab Morphological/water_coins.jpg',0)

bitimg = cv.cvtColor(grayimage,cv.COLOR_BGR2HSV)
cv2.imshow(bitimg)

kernel = np.ones((3,3),dtype='uint8')
img_erode = cv.erode(bitimg,kernel,iterations=5)
cv2.imshow(img_erode)