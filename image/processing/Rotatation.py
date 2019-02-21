import cv2

pic = cv2.imread('C:/Users/Krishna/PycharmProjects/FaceDetection-using-OpenCv/resources/kristy.jpg')
cols = pic.shape[1]
rows = pic.shape[0]

center = (cols / 2, rows / 2)
angle = 45

M = cv2.getRotationMatrix2D(center, angle, 1)
rotate = cv2.warpAffine(pic, M, (cols, rows))

cv2.imshow('shifted', rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
