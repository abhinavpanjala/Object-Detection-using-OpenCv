'''
Thresholding means converting image into binary format. It is important for image processing. Because,
some time people need separation of dark and light region. Thresholding image can separate dark and light side of the colorful image.
Another reason is, you can convert binary image in any format using that. To make the image binary, you have to go to adjustment tool and select “Threshold”.
That’s an easy way to do this.
'''

import cv2

pic = cv2.imread('C:/Users/Krishna/PycharmProjects/FaceDetection-using-OpenCv/resources/kristy.jpg', 0)

threshold_value = 100

# Black on white
#(T_value, binary_threshold) = cv2.threshold(pic, threshold_value, 255, cv2.THRESH_BINARY_INV)

# white on black
(T_value, binary_threshold) = cv2.threshold(pic, threshold_value, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', binary_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
