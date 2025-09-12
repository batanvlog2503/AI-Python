import cv2

# Dùng URL chính xác từ app
url = "http://10.20.15.43:4747/video"

cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không lấy được video, kiểm tra URL và mạng!")
        break

    cv2.imshow("IP Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC để thoát
        break

cap.release()
cv2.destroyAllWindows()