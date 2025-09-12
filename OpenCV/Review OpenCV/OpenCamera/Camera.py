

# cú pháp kết nối camera
# cv2.VideoCapture(index)
# ý nghĩa là kết nối camera. Để mở camera thì idx = 0

# cú pháp đọc lệnh Frame
# # cv2.VideoCapture.read([, image])-> retval, image
#
# ret (retval) → giá trị Boolean:
#
# True nếu đọc thành công (có khung hình).
#
# False nếu không có khung hình (camera không kết nối hoặc hết video).
#
# frame (image) → khung hình được chụp (kiểu numpy.ndarray).
# giá trị trả về false nếu không có khung hình nào được chụp
import cv2

cap = cv2.VideoCapture(0)  # Kết nối webcam

while True:
    ret, frame = cap.read()  # Đọc một khung hình
    # ret là trạng thái có khung hình k
    # trả về true nếu có và ngược lại


    if not ret:  # Nếu không có khung hình
        print("Không thể đọc khung hình từ camera")
        break

    cv2.imshow("CameranThanhTan", frame)  # Hiển thị khung hình

    if cv2.waitKey(1) == ord('q') : # ESC để thoát
        break

    if cv2.waitKey(1) & 0 : # ESC để thoát
        break


