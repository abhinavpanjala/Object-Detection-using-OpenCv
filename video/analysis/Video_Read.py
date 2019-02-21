import cv2

cap = cv2.VideoCapture('C:/Users/Krishna/PycharmProjects/FaceDetection-using-OpenCv/resources/thor.mp4')

while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('vid', frame)
    #print(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
