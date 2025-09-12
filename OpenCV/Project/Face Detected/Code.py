

import cv2
import numpy as np
def main():
    url = "http://192.168.0.101:4747/video"

    cap = cv2.VideoCapture(url)
    # sử dụng mô hình CascadeClassifer đã huấn luyện khuôn mặt
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+ "haarcascade_frontalface_default.xml")

    while(True):
        ret, frame = cap.read()

        if not ret:
            print("Khong tim thay camera")
            break


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        cv2.imshow("Face Detected", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


