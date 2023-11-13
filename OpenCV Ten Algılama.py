# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 10:17:46 2022

@author: casper
"""

import cv2
import numpy as np 
import sys

if sys.platform=='win32': 
    deltax=0
    deltay=0
else:
    deltax=50
    deltay=105
    
kamera=cv2.VideoCapture(0)
kamera.set(3, 640) #genişlik
kamera.set(4,480) #yükseklik
kamera.set(10, 0.8) #parlaklık

while True:
    _,kare=kamera.read()
    ycrcb=cv2.cvtColor(kare,cv2.COLOR_BGR2YCrCb)
    ycrcb=cv2.inRange(ycrcb,(0,137,85),(255,180,135))
    ycrcb=cv2.morphologyEx(ycrcb,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    ycrcb=cv2.dilate(ycrcb,(11,11),iterations=1)
    ycrcb=cv2.erode(ycrcb,(11,11),iterations=1)
    ycrcb=cv2.medianBlur(ycrcb,5)
    sonuc=cv2.bitwise_and(kare,kare,mask=ycrcb)
    cv2.imshow("kare",kare)
    cv2.imshow("maske",ycrcb)
    cv2.imshow("sonuc",sonuc)
    cv2.moveWindow('kare',10,10)
    cv2.moveWindow('maske',10,kare.shape[0]+deltay)
    cv2.moveWindow('sonuc',kare.shape[1]+deltax,kare.shape[0]+deltay)
    k=cv2.waitKey(10)
    if k==27 or k==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()