import cv2
import emotion
import age
import faceid
cap = cv2.VideoCapture(0)
faceid.startFaceIdScanner()


while True:
    ret, frame = cap.read()
    if(ret):
        #emotion.detectEmotion(frame)
        #age.detectAges(frame)
        faceid.detectFaceId(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

