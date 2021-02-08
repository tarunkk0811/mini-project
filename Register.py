import cv2
import os
import sys
import time
import Training

def registerFace(face_id):
    cam = cv2.VideoCapture(0)#0 is the index of our camera device
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    print("[INFO] Initializing face capture. Look at the camera (Look straight, Left and Right for better Results)...")

    vidStream = cv2.VideoCapture(0)
    count = 0

    while(True):
        ret, img = vidStream.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/user."+str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('Collecting Dataset Please wait....', img)

        if cv2.waitKey(10) == ord('q'):
            break

        elif count >= 100: # Take 100 face sample and stop video
             break
        time.sleep(0.051)
    # Do a bit of cleanup
    print("---NEW DATASET RECORDED---")
    cam.release()
    cv2.destroyAllWindows()


