# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 17:05:23 2021

@author: ASUS
"""



import cv2
import numpy as np


def diff(frame, bg):
    s = (frame.shape[0],frame.shape[1])    
    finaleFrame = np.zeros(s)
    #print("type de finale frame ",type(finaleFrame))
    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            finaleFrame[i,j] =  abs(frame[i,j]-bg[i,j])
    return finaleFrame

def simpleApproche(frame,bg):
    difference = cv2.absdiff(frame, bg)
    thresh = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    return thresh

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('../my_video.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# get the background -------------------------
path = "../bg.jpg"
bg = cv2.imread(path, 1)
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
bg = cv2.GaussianBlur(bg, (21, 21), 0)
height, width = 480, 480
bg = cv2.resize(bg, (round(width), round(height)), interpolation=cv2.INTER_AREA)


# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       
    frame = cv2.GaussianBlur(frame, (21, 21), 0)
    frame = cv2.resize(frame, (round(width), round(height)), interpolation=cv2.INTER_AREA)
    
    thresh = simpleApproche(frame,bg)
    
    #cv2.imshow("thresh", cv2.subtract(frame,bg))
    # Display the resulting frame
    cv2.imshow('Frame1',frame)
    cv2.imshow('Frame2',thresh)
    
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()