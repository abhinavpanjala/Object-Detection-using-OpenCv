import cv2

pic = cv2.imread('C:/Users/Krishna/PycharmProjects/FaceDetection-using-OpenCv/resources/kristy.jpg')

dimpixel = 7
color = 100
space = 100

filter = cv2.bilateralFilter(pic, dimpixel, color, space)
cv2.imshow('filter', filter)

cv2.waitKey(0)
cv2.destroyAllWindows()
