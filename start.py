import cv2 as cv


cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot recieve gram (stream end?) Exiting")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("frame", gray)

    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destoryAllWindows()
