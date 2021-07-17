import numpy
import cv2

# Read Image
img = cv2.imread("../assets/chessboard.png", -1)

# Convert to Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Track Corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

# Convert float values to int
corners = numpy.int0(corners)

# For all corners draw a circle
for corner in corners:
    x, y = corner[0]
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

# Display Image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
