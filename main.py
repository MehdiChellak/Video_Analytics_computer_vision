# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 17:48:32 2021

@author: ASUS
"""
from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np

width, height = 480, 480
class MainWindow :
    
    def __init__(self,main):
        self.fileName = "my_video1.mp4"
        main.config(background="#F3C007")
        main.geometry('700x600')
        
        frame_left = Frame(width=100, height=300, relief=SOLID,bd=3)
        button = Button(frame_left, text="Choose ...", height=2, width=40, command=self.printt)
        button = Button(frame_left, text="Choose ...", height=2, width=40, command=self.printt)
        button = Button(frame_left, text="Choose ...", height=2, width=40, command=self.printt)
        button = Button(frame_left, text="Choose ...", height=2, width=40, command=self.printt)
        button.pack()
        frame_left.pack(side=LEFT, padx=100, pady=5)
        
        
    def printt(self):
        print("toto")
    def substraction(self, frame, bg, th=25):
        difference = cv2.subtract(frame, bg, dtype=cv2.CV_64F)
        absul = np.abs(difference)
        thresh = cv2.threshold(absul, th, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        return thresh
    
    def getBackGround(self, choice, number = 0):
        if(choice == "simple"):
            bg = averageApproch(number)
        elif choice == "median":
            bg = medianApproch(number)
        elif choice == "movingAvg":
            bg = movingAvgApproch()
        elif choice =="difference":
            bg = movingAvgApproch()
        else :

            bg = 0
            
    def movingAvgApproch(self):
        cap = self.readVideo()
        MOVAVG = np.zeros(shape=(width, height))
        alpha = 0.1
        while(cap.isOpened()):
          # Capture frame-by-frame
          ret, frame = cap.read()
          if ret == True:
        
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       
            frame = cv2.GaussianBlur(frame, (21, 21), 0)
            frame = cv2.resize(frame, (round(width), round(height)), interpolation=cv2.INTER_AREA)
            
            MOVAVG = ((1-alpha)*MOVAVG) + (alpha*frame)
        
          else: 
            break
        cap.release()
        return MOVAVG.astype(int)
    
    def medianApproch(self,number):
        cap = readVideo()
        i=number
        
        images = np.zeros(shape=(width,height) + (3,))

        while(cap.isOpened() and i > 0):
          ret, frame = cap.read()
          if ret == True:
              
            outgray = self.convertToGray(frame)
            
            if (i==number):
                images = outgray
            else:
                images = np.dstack((images, outgray))
            i-=1
          else: 
            break
        
        cap.release()
        
        medianImage = np.median(images,axis=2)
        return medianImage.astype(int)
    
    
    def averageApproch(self,number):
        cap = readVideo()
        numberFrame = 0
        s = (height,width)
        bigFrame = np.zeros(s)
        while(cap.isOpened()):
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
        
    def convertToGray(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        height, width = 480, 480
        gray = cv2.resize(gray, (round(width), round(height)), interpolation=cv2.INTER_AREA)
        return gray
    
    def affichage(self, oldframe, newframe):
        cv2.imshow('Frame 1',oldframe)
        cv2.imshow('Frame 2',newframe)
        
    def readVideo(self):
        cap = cv2.VideoCapture('../'+self.fileName)
        if (cap.isOpened()== False): 
          print("Error opening video stream or file")
        
        return cap
    
    
root = Tk()
MainWindow(root)
root.mainloop()
        