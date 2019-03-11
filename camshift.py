
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

#load the image
img=cv2.imread('wallet.jpg',-1)
print(img.shape)
print(img.size)

#find the roi of image
roi=img[200:3000,200:4000]

x,y=200,200
w=300-x
h=400-y


#convert the roi into hsv and histogram
hsv_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
roi_hist=cv2.calcHist([hsv_roi],[0],None,[180],[0,180])

#print(hsv_roi)
#print(roi_hist)

#create the term_criteria
term_criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)

#web camera on
cap=cv2.VideoCapture(0)
      
while(True):
    res,frame=cap.read()
    
    #create hsv and mask to web camera
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
    
    
    #track the object
    ret,track_window=cv2.CamShift(mask,(x,y,w,h),term_criteria)
    
    #create rectangle
    pts=cv2.boxPoints(ret)
    pts=np.int0(pts)
    cv2.polylines(frame,[pts],True,(255,0,0),2)
    
    cv2.imshow('mask',mask)
    cv2.imshow('frame',frame)
    key=cv2.waitKey(1)
    if(key==27):
        break


cap.release()
cv2.destroyAllWindows()


# In[ ]:


import cv2
import numpy as np
image=cv2.imread('wallet.jpg',0)
gray=np.float32(image)
dst=cv2.cornerHarris(gray,2,23,0.04)
print(dst)
while True:
    cv2.imshow('corners',gray)
cv2.destroyAllWindows()


# In[ ]:


import cv2
vidcap = cv2.VideoCapture('road_car_view.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

