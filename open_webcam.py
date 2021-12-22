import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    cv2.imshow('JKwebcam',img)
    k=cv2.waitKey(10)
    if k==27:
        break;
cap.release()
cv2.destroyAllWindows()
