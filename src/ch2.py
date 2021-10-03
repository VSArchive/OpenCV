import cv2
import numpy as np

img = cv2.imread("resources/imgsat11.jpeg")
print(img.shape)

imgResize = cv2.resize(img,(300,200))

imgCropped = img[40:390,550:900]

cv2.imshow("Image",img)
cv2.imshow("resize",imgResize)
cv2.imshow("cropped",imgCropped)
cv2.waitKey(0)