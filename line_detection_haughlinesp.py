
# coding: utf-8

import cv2
import numpy as np

cap=cv2.VideoCapture("road_car_view.mp4")

while(True):
    res,frame=cap.read()
    
    
    frame1=cv2.GaussianBlur(frame,(5,5),0)
    hsv=cv2.cvtColor(frame1,cv2.COLOR_BGR2HSV)
    
    low_yellow=np.array([18,94,140])
    up_yellow=np.array([48,255,255])
    
    mask=cv2.inRange(hsv,low_yellow,up_yellow)
    edges=cv2.Canny(mask,75,150)
    
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
    #print(lines)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)   
    
    
    cv2.imshow("mask",mask)
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)
    if(key==27):
        break
cap.release()
cv2.destroyAllWindows()

