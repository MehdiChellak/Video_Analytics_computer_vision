# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mySecond App.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtCore import QCoreApplication
import os
from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np
width, height = 480, 480
import sys

NBF=50

class Ui_Form(object):
    def setupUi(self, Form):
        self.videoPath=''
        self.bgPath=''
        Form.setObjectName("Form")
        Form.resize(657, 471)
        
        self.bg = QtWidgets.QPushButton(Form)
        self.bg.setGeometry(QtCore.QRect(210, 70, 141, 28))
        self.bg.setObjectName("bg")
        
        self.simple = QtWidgets.QPushButton(Form)
        self.simple.setGeometry(QtCore.QRect(70, 70, 141, 28))
        self.simple.setObjectName("simple")
        
        self.average = QtWidgets.QPushButton(Form)
        self.average.setGeometry(QtCore.QRect(70, 120, 141, 28))
        self.average.setObjectName("average")
        self.median = QtWidgets.QPushButton(Form)
        self.median.setGeometry(QtCore.QRect(70, 170, 141, 28))
        self.median.setObjectName("median")
        self.moving_average = QtWidgets.QPushButton(Form)
        self.moving_average.setGeometry(QtCore.QRect(70, 220, 141, 28))
        self.moving_average.setObjectName("moving_average")
        self.filter = QtWidgets.QPushButton(Form)
        self.filter.setGeometry(QtCore.QRect(70, 270, 141, 28))
        self.filter.setObjectName("filter")
        self.select_video = QtWidgets.QPushButton(Form)
        self.select_video.setGeometry(QtCore.QRect(200, 330, 93, 28))
        self.select_video.setObjectName("select_video")
        self.saveVideo = QtWidgets.QPushButton(Form)
        self.saveVideo.setGeometry(QtCore.QRect(330, 330, 93, 28))
        self.saveVideo.setObjectName("saveVideo")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 330, 101, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, -20, 401, 111))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.select_video.clicked.connect(lambda: self.select_video_handler())
        self.simple.clicked.connect(lambda: self.simple_app())
        self.median.clicked.connect(lambda: self.median_app())
        self.moving_average.clicked.connect(lambda: self.moving_average_app())
        self.average.clicked.connect(lambda: self.average_app())
        self.bg.clicked.connect(lambda: self.select_bg_handler())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.simple.setText(_translate("Form", "Simple "))
        self.bg.setText(_translate("Form", "choose background "))
        self.average.setText(_translate("Form", "Average "))
        self.median.setText(_translate("Form", "Median "))
        self.moving_average.setText(_translate("Form", "Moving Average"))
        self.filter.setText(_translate("Form", "Filter Pass Haute"))
        self.select_video.setText(_translate("Form", "Select Video"))
        self.saveVideo.setText(_translate("Form", "Save Video"))
        self.pushButton_3.setText(_translate("Form", "Open Camera"))
        self.label.setText(_translate("Form", "5 Approches video analysis"))

    
    def select_video_handler(self):
        file_filter = 'Data File (*.mp4 *.avi)'
        response = QFileDialog.getOpenFileName(
            caption='Select a Video',
            directory=os.getcwd(),# get the current path of this file
            filter=file_filter # set your filter
        )
        self.videoPath = response[0]
        print(self.videoPath)
    
    def select_bg_handler(self):
        file_filter = 'Data File (*.jpeg *.jpg)'
        response = QFileDialog.getOpenFileName(
            caption='Select a back ground',
            directory=os.getcwd(),# get the current path of this file
            filter=file_filter # set your filter
        )
        self.bgPath = response[0]
        print(self.bgPath)
    
    def substraction(self, frame, bg, th=25):
        difference = cv2.subtract(frame, bg, dtype=cv2.CV_64F)
        absul = np.abs(difference)
        thresh = cv2.threshold(absul, th, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        return thresh
    
    def convertToGray(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        height, width = 480, 480
        gray = cv2.resize(gray, (round(width), round(height)), interpolation=cv2.INTER_AREA)
        return gray
    
    def readVideo(self):
        cap = cv2.VideoCapture(self.videoPath)
        if (cap.isOpened()== False): 
          print("Error opening video stream or file")
        return cap
    
    def showMeSome(self,bg, msg):
        cap = cv2.VideoCapture(self.videoPath)
    
        # Check if camera opened successfully
        if (cap.isOpened()== False): 
          print("Error opening video stream or file")
        while (cap.isOpened()):
            ret,frame = cap.read()
            if ret == True:
                
                gray = self.convertToGray(frame)
                thresh = self.substraction(gray,bg)
                cv2.imshow('original',gray)
                cv2.imshow(msg,thresh)
                
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
                    cap.release()
                    cv2.destroyAllWindows()
            else:
                break
        cap.release()
        # Closes all the frames
        cv2.destroyAllWindows()
    
    def simple_app(self):
        if (self.bgPath==''):
            bg = cv2.imread(self.bgPath, 1)
            grayBg = self.convertToGray(bg)
            self.showMeSome(grayBg, "Simple")
        else:
            print("empty path of background")

    def moving_average_app(self):
        cap = cv2.VideoCapture(self.videoPath)

        # Check if camera opened successfully
        if (cap.isOpened()== False): 
          print("Error opening video stream or file")
        
        width, height = 480, 480
        
        MOVAVG = np.zeros(shape=(width, height))
        alpha = 0.1
        # Read until video is completed
        while(cap.isOpened()):
          # Capture frame-by-frame
          ret, frame = cap.read()
          if ret == True:
            gray = self.convertToGray(frame)
            MOVAVG = ((1-alpha)*MOVAVG) + (alpha*gray)
          else: 
            break
        cap.release()
        MOVAVG = MOVAVG.astype(int)
        
        self.showMeSome(MOVAVG, "mouving average")
    
    def median_app(self):
        cap = cv2.VideoCapture(self.videoPath)
        if (cap.isOpened()== False): 
          print("Error opening video stream or file")
        
        n=NBF
        images = np.zeros(shape=(480,480) + (3,))
        # Read until video is completed
        while(cap.isOpened() and n > 0):
          # Capture frame-by-frame
          ret, frame = cap.read()
          if ret == True:
              
            gray = self.convertToGray(frame)
            
            if (n==NBF):
                images = gray
            else:
                images = np.dstack((images,gray))
            
            n-=1
          # Break the loop
          else: 
            break
        medianImage = np.median(images,axis=2)
        medianImage = medianImage.astype(int)
        self.showMeSome(medianImage, "median")

    def average_app(self):
        cap = self.readVideo()
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
            if numberFrame == NBF:
                break
          else: 
            break
        
        bigFrame = 1/numberFrame * bigFrame
        moyenFrame = bigFrame.astype(int)
        cap.release()
        self.showMeSome(moyenFrame,"average")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
