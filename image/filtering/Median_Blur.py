import cv2

pic = cv2.imread('C:/Users/Krishna/PycharmProjects/FaceDetection-using-OpenCv/resources/kristy.jpg')

kernal = 3

median = cv2.medianBlur(pic, kernal)

cv2.imshow('median', median)

cv2.waitKey(0)
cv2.destroyAllWindows()
