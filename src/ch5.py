import cv2
import numpy as np

img = cv2.imread("resources/imgsat12.jpeg")

imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("Original",img)
cv2.imshow("HSV",imgHSV)
cv2.waitKey(0)