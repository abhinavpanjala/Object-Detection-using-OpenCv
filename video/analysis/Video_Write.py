import cv2

cap = cv2.VideoCapture('C:/Users/Krishna/PycharmProjects/FaceDetection-using-OpenCv/resources/thor.mp4')
fourcc = cv2.VideoWriter_fourcc(*'VIDE')
fps = 30
framesize = (720, 400)
out = cv2.VideoWriter('sample.avi', fourcc, fps, framesize)
while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
