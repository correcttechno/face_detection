import cv2
import emotion
import age
import faceid
import database

cap = cv2.VideoCapture(0)
faceid.startFaceIdScanner()
print("PROQRAM BASLADI:")

while True:
    ret, frame = cap.read()
    if(ret):
        #
        detectName=faceid.faceIdCallback(frame)
        print("OXUNAN DATA:")
        print(detectName)
        if(detectName==False):
            detectAge=age.detectAges(frame)
            print("YAS:")
            print(detectAge)
            database.insert(detectName,"",detectAge)
        else:
           detectEmotion=emotion.detectEmotion(frame)
           print(detectEmotion)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

