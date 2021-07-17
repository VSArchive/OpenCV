import cv2

# Read From Web Cam
cam = cv2.VideoCapture(0)

# Display Video
while True:
    ret, frame = cam.read()
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
