import cv2
import numpy


img = cv2.imread("../assets/lake.png")
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

minimum = numpy.array([0, 0, 0])
maximum = numpy.array([179, 150, 255])

mask = cv2.inRange(imgHSV, minimum, maximum)
# imgColor = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Mask", mask)
cv2.waitKey(0)
