import cv2

# Read Image Color
img = cv2.imread("../assets/avengers.jpg", -1)

# Rotate Image
img = cv2.rotate(img, cv2.ROTATE_180)

# Read Image Black & White
img_black_white = cv2.imread("../assets/avengers.jpg", 0)

# Resize Image
img_black_white = cv2.resize(img_black_white, (400, 400))

# Display Image
cv2.imshow("Image", img)
cv2.imshow("Image Black & White", img_black_white)
cv2.waitKey(0)
cv2.destroyAllWindows()
