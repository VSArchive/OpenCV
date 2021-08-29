import cv2
import numpy


def on_change(value):
    pass


img = cv2.imread("../assets/krishna.tif")
img = cv2.resize(img, (512, 512))
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow('Trackbars')

cv2.createTrackbar('HMin', "Trackbars", 0, 255, on_change)
cv2.createTrackbar('HMax', "Trackbars", 0, 255, on_change)
cv2.createTrackbar('SMin', "Trackbars", 0, 255, on_change)
cv2.createTrackbar('SMax', "Trackbars", 0, 255, on_change)
cv2.createTrackbar('VMin', "Trackbars", 0, 255, on_change)
cv2.createTrackbar('VMax', "Trackbars", 0, 255, on_change)

while True:
    HMin = cv2.getTrackbarPos("HMin", "Trackbars")
    HMax = cv2.getTrackbarPos("HMax", "Trackbars")
    SMin = cv2.getTrackbarPos("SMin", "Trackbars")
    SMax = cv2.getTrackbarPos("SMax", "Trackbars")
    VMin = cv2.getTrackbarPos("VMin", "Trackbars")
    VMax = cv2.getTrackbarPos("VMax", "Trackbars")

    minimum = numpy.array([HMin, SMin, VMin])
    maximum = numpy.array([HMax, SMax, VMax])

    mask = cv2.inRange(imgHSV, minimum, maximum)

    whitePixels = numpy.where(
        (mask[:, :] == 255) &
        (mask[:, :] == 255) &
        (mask[:, :] == 255)
    )

    img[whitePixels] = [0, 0, 0]

    cv2.imshow("Result", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
