import cv2 as cv
import numpy as np

img = cv.imread('Mini Test/E2.jpg')

src2 = cv.resize(img , None , fx=0.5 , fy=0.5)
src = cv.resize(img , None , fx=0.5 , fy=0.5)
imgBlur = cv.medianBlur(src, 25)

hsv = cv.cvtColor(imgBlur, cv.COLOR_BGR2HSV) 

lower_red = np.array([0,0,220])
upper_red = np.array([180,255,255])

ppromxx = cv.inRange(hsv, lower_red , upper_red)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(11,11))
phuwin = cv.morphologyEx(ppromxx, cv.MORPH_OPEN, kernel, iterations = 1)
dilate = cv.morphologyEx(phuwin, cv.MORPH_CLOSE, kernel, iterations = 1)
contours,h = cv.findContours(dilate, cv.RETR_EXTERNAL , cv.CHAIN_APPROX_NONE)

for bestboom in contours:
        cv.drawContours(src2, bestboom, -1, (0, 255, 0), 3)

cv.imshow("Tomato detection", src2)
# 3.1
print("Tomato = " + str(len(contours)))

cv.waitKey(0)
cv.destroyAllWindows()

