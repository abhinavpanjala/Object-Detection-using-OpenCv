import numpy as np
import cv2

# 500 x 500 pixels image with 3 colors RBG and 8 bit unsigned Integers
pic = np.zeros((500, 500, 3), dtype='uint8')

cv2.rectangle(pic, (0, 0), (500, 150), (123, 200, 98), 3, lineType=8, shift=0)
cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
