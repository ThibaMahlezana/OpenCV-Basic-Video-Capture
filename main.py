from imutils.video import VideoStream
import cv2

print("[INFO] Loading video stream")
cap = VideoStream(src=0).start()

while True:
    frame = cap.read()

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.stop()
cv2.destroyAllWindows()
