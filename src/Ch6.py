import cv2
import numpy


img = cv2.imread("resources/L1C_T44PMC_A020594_20210214T051145.tif")
img = cv2.resize(img,(512,512))
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

minimum = numpy.array([0, 0, 0])
maximum = numpy.array([179, 150, 255])

mask = cv2.inRange(imgHSV, minimum, maximum)
# imgColor = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Mask", mask)
cv2.waitKey(0)