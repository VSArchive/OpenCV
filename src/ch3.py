import cv2
import numpy as np

img=np.ones((512,512,3),np.uint8)


cv2.line(img,(250,250),(400,400),(205,135,150),6)
cv2.rectangle(img,(0,0),(250,250),(25,120,180),cv2.FILLED)
cv2.circle(img,(180,350),100,(12,120,63),6)
cv2.putText(img,"OPENCV",(100,200),cv2.FONT_HERSHEY_SIMPLEX,1,(25,63,89),3)
cv2.imshow("image",img)



cv2.waitKey(0)