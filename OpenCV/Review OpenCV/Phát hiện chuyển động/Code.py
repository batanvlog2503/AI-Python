
import cv2

# cv2.CAP_PROP_FRAME_WIDTH (3)	Độ rộng khung hình (pixel).
# cv2.CAP_PROP_FRAME_HEIGHT (4)	Chiều cao khung hình (pixel).
# cv2.CAP_PROP_FPS (5)	Số khung hình/giây (fps).
# cv2.CAP_PROP_BRIGHTNESS (10)	Độ sáng video (0.0 – 1.0 hoặc driver).
# cv2.CAP_PROP_CONTRAST (11)	Độ tương phản.
# cv2.CAP_PROP_SATURATION (12)	Độ bão hòa màu.
# cv2.CAP_PROP_GAIN (14)	Độ khuếch đại tín hiệu.
# cv2.CAP_PROP_EXPOSURE (15)	Độ phơi sáng.
# cv2.CAP_PROP_POS_FRAMES (1)	Đặt vị trí khung hình (frame index).
cap = cv2.VideoCapture(0) # camera của máy
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # pixel # set cho khung hình
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)


for i in range(10):
    _, frame = cap.read()
frame = cv2.resize(frame, (640, 480))

# chuyển thành ảnh grayscale 0 1
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
last_frame = gray # background ban đầu rồi lấy từng hình ảnh trừ đi
# là ra chuyển động
#
# cv2.imshow("BACKGROUND", background)
# lấy background
while True:
    ret, frame = cap.read()

    # xử lý frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (25, 25), 0)
    abs_img = cv2.absdiff(last_frame, gray)
    # abs(0-255) =255 là 1 nói chung đỡ bị tràn số

    last_frame = gray # caapj nhat anh

    # hiển thị màn hình ã

    _, img_mask = cv2.threshold(abs_img, 30, 255, cv2.THRESH_BINARY)
    # dùng threshold để biến màu pức tạp thành 2 màu trắng đen
    # thresh 30 nghia là pixel nào lớn hơn 30 thì coi là tranwgs 255 nguocj lại là đen

    contours, _ = cv2.findContours(img_mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # contours là danh sách các đường biên tìm được
    # mode cv2.RETR_EXTERNAL → chỉ lấy contour ngoài cùng.
    # cv2.RETR_LIST → lấy tất cả contour, không quan tâm quan hệ cha – con.
    # cv2.RETR_TREE → lấy tất cả và xây dựng cây phân cấp (hierarchy).
    # cv2.RETR_CCOMP → chia contour thành 2 cấp độ (contour ngoài và lỗ bên trong).

    # cv2.CHAIN_APPROX_NONE lưu tất cả các điểm trên đường biên (nhiều điểm dư thừa).
    #cv2.CHAIN_APPROX_SIMPLE chỉ lưu các điểm góc (bỏ điểm thẳng hàng, tiết kiệm bộ nhớ).
    # cv2.CHAIN_APPROX_TC89_L1 và cv2.CHAIN_APPROX_TC89_KCOS các thuật toán nén tiên tiến (ít dùng).


    # contours trả về 1 lisst danh sách các điểm gồm [[x1, y1], [x2. y2],...
    for contour in contours:
        if cv2.contourArea(contour) < 900: # diện tích nhỏ quá thì bỏ ra
            continue
        x, y, w, h = cv2.boundingRect(contour)
        # vẽ hình chuwx nhat nho nhat bao quanh contour
        cv2.rectangle(frame, (x, y), (x + w, y+h), (0, 255, 0), 3)
    cv2.imshow("Window", frame)
    if(cv2.waitKey(1) == ord('q')):
        break