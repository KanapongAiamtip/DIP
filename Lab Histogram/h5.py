import cv2
img1 = cv2.imread('Lab Histogram/prom.jpg',0)
img2 = cv2.imread('Lab Histogram/dunk.jpg',0)
hist_img1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
hist_img2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
ppromxx = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)
if ppromxx == 1:
    print("ภาพเหมือนกัน , มีผลต่างเท่ากับ = ", ppromxx)
else:
    print("ภาพต่างกัน , มีผลต่างเท่ากับ = ", ppromxx)