


import cv2
import numpy as np


cap = cv2.VideoCapture('video/1.mp4')
frame_last = np.zeros((720,1074))
i = 0
count = 0
while (1):
    ret, frame_now = cap.read()
    frame_now=cv2.cvtColor(frame_now,cv2.COLOR_RGB2GRAY)
    frame_now = cv2.threshold(frame_now, 200, 255, cv2.THRESH_BINARY)[1]

    diff = abs(frame_now - frame_last)
    diff = np.where(diff==0,0,1)
    ##over 300，000 pixels have changed over abs(100) value in 255
    if diff.sum()>8000:
        cv2.imwrite(str(i)+'.jpg',frame_now)
        print(str(i)+'.jpg')
        i += 1
    frame_last = frame_now


    if ret == False:
        break

    print('count:', count)
    count += 1