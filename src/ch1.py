import cv2
import numpy as np

img = cv2.imread("resources/imgsat12.jpeg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #gray scale
imgBlur =cv2.GaussianBlur(img,(9,9),0) #blur images
imgCanny = cv2.Canny(img,250,200) #edge detecction
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgCanny,kernel,iterations=3)

cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("dialation",imgDialation)
cv2.imshow("Erosion",imgEroded)


cv2.waitKey(0)






