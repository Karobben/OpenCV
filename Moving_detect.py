#!/usr/bin/env python3
import numpy as np
import cv2
import itertools
import time
from mss import mss

Threshold = 60
def Mv_detect(pic1,pic2):
    pic1 = cv2.cvtColor(pic1, cv2.COLOR_BGR2GRAY)
    pic2 = cv2.cvtColor(pic2, cv2.COLOR_BGR2GRAY)
    Df = abs(np.array(pic1,dtype='int16') - np.array(pic2,dtype='int16'))
    Df_sum = sum(Df[np.where(Df>Threshold)])
    #print(Df_sum)
    return Df

def Screen_snap():
    cords = {'top':0 , 'left': 0 , 'width': 1920, 'height': 1080 }
    with mss() as sct :
        img = np.array(sct.grab(cords)) #sct.grab(cords/monitor)
    return img

fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter("outfilename.mp4", fourcc, 15,(1920,1080),0)

frame0 = Screen_snap()

while(True):
    frame = Screen_snap()
    Df = Mv_detect(frame,frame0)
    frame0 = frame
    Df_frame = np.array(Df,dtype='uint8')
    out.write(Df_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
