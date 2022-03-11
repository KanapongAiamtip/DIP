import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('Mini Test/E1.jpg')
imgcolorRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#1.1
print(image.shape)

#1.2
scale_up_x = 0.3
scale_up_y = 0.3

ppromxx = cv2.resize(imgcolorRGB,None,fx=scale_up_x,fy=scale_up_y)
print(ppromxx.shape)
cv2.imshow('1.2',ppromxx)

#1.3
bbver = np.array(255*(image/255)**0.67,dtype='uint8')
chageimage = cv2.hconcat([image,bbver])
cv2.imshow('1.3',chageimage)

#1.4
plt.hist(image.ravel(),(0,256),[0,32])
plt.show()

#1.5
grayimage = cv2.imread('Mini Test/E1.png',0)
cv2.imshow('1.5', grayimage)
cv2.waitKey(0)


