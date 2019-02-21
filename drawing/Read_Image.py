import cv2

img = cv2.imread('resources/image.jpg', 1)
img = cv2.imwrite('resources/image.png', img)
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()