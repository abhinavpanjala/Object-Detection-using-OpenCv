import cv2

pic = cv2.imread('C:/Users/Krishna/PycharmProjects/FaceDetection-using-OpenCv/resources/kristy.jpg', 0)

matrix = (7, 7)

blur = cv2.GaussianBlur(pic, matrix, 0)

cv2.imshow('blur', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
