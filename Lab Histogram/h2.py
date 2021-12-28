import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('Lab Histogram/prom.jpg', 0)

dimensions = image.size

plt.hist(image.ravel()/dimensions)
plt.show()