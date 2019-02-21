import numpy as np
import cv2

# 500 x 500 pixels image with 3 colors RBG and 8 bit unsigned Integers
pic = np.zeros((500, 500, 3), dtype='uint8')

color = (255, 0, 255)

cv2.circle(pic, (250, 250), 100, color)

cv2.imshow('white', pic)

cv2.waitKey(0)

cv2.destroyAllWindows()
