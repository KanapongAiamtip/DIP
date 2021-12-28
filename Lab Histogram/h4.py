import cv2
originalImage = cv2.imread('Lab Histogram/prom.jpg')
grayimage = cv2.imread('Lab Histogram/prom.jpg',0)
thresholder = int(input("Input the threshold: "))
(thresh, blackAndWhiteImage) = cv2.threshold(grayimage, thresholder, 255, cv2.THRESH_BINARY)
cv2.imshow('Original image', originalImage)
cv2.imshow('Black White image', blackAndWhiteImage)
cv2.waitKey(0)
cv2.destroyAllWindows()