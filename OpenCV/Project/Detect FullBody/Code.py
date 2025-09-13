
import cv2


# load the video file

cap = cv2.VideoCapture(r"D:\Project Python AI\OpenCV\Project\Detect FullBody\6387-191695740_small.mp4")

#load  the pre trainedd


body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

min_size = (30, 60)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Không tìm thấy")
        break

    # resize frame
    frame_resized = cv2.resize(frame, (640, 480))

    # convert to gray
    gray_frame = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    # reduce noise giảm nhiễu
    gray_blurred = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    # detect human in the frame
    bodies = body_cascade.detectMultiScale(gray_blurred, scaleFactor=1.05, minNeighbors=4, minSize=min_size)

    for x, y, w, h in bodies:
        cv2.rectangle(frame, (x,y) , (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Detect Body", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
