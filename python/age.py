import cv2
import numpy as np

age_model_path = "agefiles/age_net.caffemodel"
age_proto_path = "agefiles/age_deploy.prototxt"
face_model_path = "agefiles/opencv_face_detector_uint8.pb"
face_proto_path = "agefiles/opencv_face_detector.pbtxt"
AGE_GROUPS = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(21-24)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
age_net = cv2.dnn.readNetFromCaffe(age_proto_path, age_model_path)
face_net = cv2.dnn.readNetFromTensorflow(face_model_path, face_proto_path)

def detectAges(frame):
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104, 117, 123], True, False)
    face_net.setInput(blob)
    detections = face_net.forward()
    

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.7: 
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            face = frame[startY:endY, startX:endX]
            if face.size > 0:
                blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
                age_net.setInput(blob)
                age_preds = age_net.forward()
                age = AGE_GROUPS[age_preds[0].argmax()]
                label =age
                #cv2.rectangle(frame, (startX, startY), (endX, endY), (255, 0, 0), 2)
                #cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                #cv2.imshow("Age Estimation", frame)
                return label
           

    return False

    

