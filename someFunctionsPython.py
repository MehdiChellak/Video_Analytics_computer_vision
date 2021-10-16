# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:54:24 2021

@author: ASUS
"""


import numpy as np 
import cv2
from random import randrange


a = np.array([[1,2,3],[4,5,6]])

b = np.array([[7,8,9],[10,11,12]])

c =  np.array([[5,4,2],[10,11,6]])

d =  np.zeros((2,3))

t=np.dstack((a,b,c))

n=3
i = 3
images = np.zeros(shape = (2,3))
while (i>0):
       array =  np.random.randint(randrange(20), size=(2, 3))
       print(array)
       if(i==3):
           images = array
       else:     
           images = np.dstack((images,array))
       i-=1

print("images", images)
rr = np.median(t,axis=2)
rr = rr.astype(int)

