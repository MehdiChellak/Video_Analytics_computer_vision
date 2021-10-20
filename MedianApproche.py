# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:24:10 2021

@author: ASUS
"""


import cv2
import numpy as np

def simpleApproche(frame,bg):
    difference = cv2.subtract(frame, bg, dtype=cv2.CV_64F)
    absul = np.abs(difference)
    thresh = cv2.threshold(absul, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    return thresh



# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('../my_video1.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

n=21
images = np.zeros(shape=(480,480) + (3,))
# Read until video is completed
while(cap.isOpened() and n > 0):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
      
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    height, width = 480, 480
    gray = cv2.resize(gray, (round(width), round(height)), interpolation=cv2.INTER_AREA)
    
    if (n==11):
        images = gray
    else:
        images = np.dstack((images,gray))
    
    n-=1
  # Break the loop
  else: 
    break


medianImage = np.median(images,axis=2)
medianImage = medianImage.astype(int)

# When everything done, release the video capture object
cap.release()


cap = cv2.VideoCapture('../my_video1.mp4')
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

while (cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        height, width = 480, 480
        gray = cv2.resize(gray, (round(width), round(height)), interpolation=cv2.INTER_AREA)
        
        thresh = simpleApproche(gray,medianImage)
        
        cv2.imshow('Frame 1',gray)
        cv2.imshow('Frame 2',thresh)
                
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

  # Break the loop
    else:
        break
    
# When everything done, release the video capture object
cap.release()


# Closes all the frames
cv2.destroyAllWindows()
