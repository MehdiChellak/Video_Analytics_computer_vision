# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 22:24:26 2021

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
    

cap = cv2.VideoCapture('../my_video1.mp4')

# Check if camera opened successfully

if (cap.isOpened()== False): 
  print("Error opening video stream or file")

numberFrame = 0
s = (480,480)
# Read until video is completed
bigFrame = np.zeros(s)
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    height, width = 480, 480
    gray = cv2.resize(gray, (round(width), round(height)), interpolation=cv2.INTER_AREA)    
    bigFrame = gray + bigFrame 
    numberFrame +=1
    if numberFrame == 50:
        break
  else: 
    break

bigFrame = 1/numberFrame * bigFrame
moyenFrame = bigFrame.astype(int)
cap.release()
print(numberFrame)


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
        
        thresh = simpleApproche(gray,moyenFrame)
        
        # Stack all three frames and show the image
        stacked = np.hstack((gray,gray))
        #cv2.imshow('All three',cv2.resize(stacked,None,fx=0.65,fy=0.65))
        cv2.imshow("frame 1", gray)
        cv2.imshow("frame 2", thresh)
                
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

  # Break the loop
    else:
        break
    
# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()