import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
im = cv.imread('Lab Histogram/prom.jpg', 0)
hist = cv.calcHist([im], [0], None, [256], [0, 256])
row, col = im.shape
ppromxx = [0, 0, 0]
for i in range(len(hist)):
    if i <= 85:
        ppromxx[0] += hist[i]
    elif i <= 170:
        ppromxx[1] += hist[i]
    else:
        ppromxx[2] += hist[i]
result = "Dark image" if ppromxx[0] > ppromxx[1] and ppromxx[0] > ppromxx[
    2] else "Low contrast" if ppromxx[1] > ppromxx[0] and ppromxx[1] > ppromxx[2] else "Bright image"
cv.imshow(f"this Image is : {result}", im)
cv.waitKey(0)
