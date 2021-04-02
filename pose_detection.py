import cv2
import time
import mediapipe as mp
import numpy as np

#Defining Webcam as video input
cap = cv2.VideoCapture(1)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

mp_draw = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

ptime = 0
ctime = 0

while True:
    #reading from webcam
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    image_height, image_width, _ = img.shape
    screen = np.zeros(img.shape)
    x1,y1 = 0 ,0

    #getting the pose from the image using media
    results = pose.process(imgRGB)

    #using mediapipe module to draw the landmarks into image
    if results.pose_landmarks:
        #for poselms in results.pose_landmarks:   
        #x1 = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].x * image_width
        #y1 = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].y * image_height
        #if x1 > 0 and y1 > 0:
            #cv2.circle(screen,(int(x1),int(y1)),10,(0,0,255),-1)
        mp_draw.draw_landmarks(screen,results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        #print (x1,y1)

    #to calculate fps
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(screen,"FPS: "+str(round(fps)),(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)
    cv2.imshow("CAM001",screen)
    cv2.waitKey(1)

    
