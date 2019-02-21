import numpy as np
import cv2

# 500 x 500 pixels image with 3 colors RBG and 8 bit unsigned Integers
pic = np.zeros((500, 500, 3), dtype='uint8')

cv2.rectangle(pic, (0, 0), (500, 150), (123, 200, 98), 3, lineType=8, shift=0)

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic, 'Krishna', (100, 100), font, 3, (255, 255, 255), 4, cv2.LINE_8)

color = (255, 0, 255)
cv2.circle(pic, (250, 250), 100, color)

cv2.line(pic, (133, 138), (388, 133), (0, 0, 255))

cv2.imshow('dark', pic)

cv2.waitKey(0)
cv2.destroyAllWindows()
