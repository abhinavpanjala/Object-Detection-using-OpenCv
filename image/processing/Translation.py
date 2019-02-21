import numpy as np

import cv2

pic = cv2.imread('C:/Users/Krishna/PycharmProjects/FaceDetection-using-OpenCv/resources/kristy.jpg')
cols = pic.shape[1]
rows = pic.shape[0]

# 150 pixels right X-axis & 70 pixels Y-axis for negative numbers opposite of positive image
M = np.float32([[1, 0, 150], [0, 1, 70]])

shifted = cv2.warpAffine(pic, M, (cols, rows))
cv2.imshow('shifted', shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()
