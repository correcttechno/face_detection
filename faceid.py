import threading
import time
import cv2
import face_recognition
import os
import random

video = None
known_faces = []
known_names = []
known_faces_dir = './known_faces'
file_extension = '.jpg'

def startFaceIdScanner():
    global known_faces
    global known_names

    for filename in os.listdir(known_faces_dir):
        name = os.path.splitext(filename)[0]
        known_names.append(name)

        file_path = os.path.join(known_faces_dir, filename)
        image = face_recognition.load_image_file(file_path)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(face_encoding)


def faceIdCallback(frame):
    global video
    global known_faces
    global known_names

    while True:
        frame = cv2.resize(frame, (640, 480))
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_faces, face_encoding)

            best_match_index = -1
            best_match_distance = 0.5

            for i in range(len(matches)):
                if matches[i]:
                    face_distance = face_recognition.face_distance([known_faces[i]], face_encoding)[0]
                    if face_distance < best_match_distance:
                        best_match_index = i
                        best_match_distance = face_distance

            top, right, bottom, left = face_location
            cropped_face = frame[top:bottom, left:right]  # Yüzü kırp

            if best_match_index == -1:
                #cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 1)
                #print("Tanımadı")
                name =str(random.randrange(111,999999))
                known_faces.append(face_encoding)
                known_names.append(name)
                file_path = os.path.join(known_faces_dir, name + file_extension)
                cv2.imwrite(file_path, cropped_face)
                return name

            else:
                name = known_names[best_match_index]
                #cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 1)
                return name
                #cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (0, 255, 0), cv2.FILLED)
                #font = cv2.FONT_HERSHEY_DUPLEX
                #cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

            # Kırpılan yüzü göster
            #if cropped_face.size > 0:
               # cv2.imshow(f"Cropped Face {name if best_match_index != -1 else 'Unknown'}", cropped_face)

        #cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



