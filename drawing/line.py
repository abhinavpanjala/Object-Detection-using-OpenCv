import numpy as np
import cv2

# 500 x 500 pixels image with 3 colors RBG and 8 bit unsigned Integers
pic = np.zeros((500, 500, 3), dtype='uint8')

cv2.line(pic, (350, 350), (500, 350), (0, 0, 255))
cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
