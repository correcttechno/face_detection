import cv2
import emotion
import age
import faceid
import database
from datetime import datetime


cap = cv2.VideoCapture(0)
faceid.startFaceIdScanner()
print("PROQRAM BASLADI:")

while True:
    ret, frame = cap.read()
    if(ret):
        #
        now = datetime.now()
        detectName=faceid.faceIdCallback(frame)
        print("OXUNAN DATA:")
        print(detectName)
        if(detectName!=None and detectName[1]==False):
            detectAge=age.detectAges(frame)
            print("YAS:")
            print(detectAge)
            database.insertFaceid(detectName[0],now.strftime("%d/%m/%Y %H:%M:%S"),detectAge)
        elif(detectName!=None and detectName[1]==True):
           detectEmotion=emotion.detectEmotion(frame)
           if(detectEmotion!=None):
            database.saveEmotion(detectName[0],detectEmotion,now.strftime("%d/%m/%Y %H:%M:%S"))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

