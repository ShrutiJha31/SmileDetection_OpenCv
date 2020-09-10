# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 17:12:21 2020

@author: Shruti Jha
"""

#Importing the libraries

import cv2

# loading the cascade - for this we will create two objects
#one for face
#one for eyes
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
  #we call this class from opencv to create an object
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('Mouth.xml')
smile_cascade = cv2.CascadeClassifier('Smile.xml') 
  
  #now we need to define the function which will used for the detection
  #1. We need to define the detection rectangle(coordiantes)
  #2. We need to define the for loop whi9ch iterates through the face
  #the argument of the function will be the different images taken by the rectangle from the video
  #gray-image in black and white(taken by the rect)
  #frame-original image
def detect(gray, frame):
      faces = face_cascade.detectMultiScale(gray, 1.3, 5)
      #1.3 specifies the scale by which the image size is reduced 5- inorder to accept the image the five neighbour zones must also be accepted
       #faces tuples(sort of array) will store the coordinate of the upper right corner of the rectangle as well as the height and width of the rectangle
      for (x, y, w , h) in faces:
          cv2.rectangle(frame, (x , y),(x+w,y+h), (255,0,0),2)#x+w&y+h give the bottom right coordinte of the rectangle
          #rgb argument of the colour, 2- thickness of the rectangle
          roi_gray = gray[x:x+w, y:y+h]
          roi_color= frame[x:x+w, y:y+h]
          eyes =eye_cascade.detectMultiScale(roi_gray, 1.1,22)
          for(ex, ey,ew, eh) in eyes:
              cv2.rectangle(roi_color, (ex , ey),(ex+ew,ey+eh), (0,255,0),2)
                   #frame is the image onwhich we are drawing i.e the coloured image and gray is the image from which are extracting
                   #we search for eyes in the boxes they found the face in therefore refrence to the face
         
              
          smile=smile_cascade.detectMultiScale(roi_gray,1.7,22)
          for(sx,sy,sw,sh) in smile:
                 cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2) 
                 cv2.putText(
                 roi_color, #numpy array on which text is written
                "smile", #text
                (sx,sy), #position at which writing has to start
                 cv2.FONT_HERSHEY_SIMPLEX, #font family
                1, #font size
                (209, 80, 0, 255), #font color
                 3) #font stroke
      return frame  #return the original image with the rectangles drawn on it

  #Doing face detection using webcam
video_capture = cv2.VideoCapture(0) 
  #to connect the webcam we created a video_capture object using the video_capture class of openCV
  #the video_capture class of opencv takes only one argument i.e 0 if its the computer's webcam
  # 1 if there is an external web camera`
while True:
      #we create an infinte loop till the break
      _, frame = video_capture.read()  
      #convert this image to black n white
      gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      canvas = detect(gray, frame)
      cv2.imshow('Video', canvas)
      #if we press q thr webcam stops
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break;
video_capture.release()
  #has the power to turn of the webcam
cv2.destroyAllWindows()
          
          
      
  
             