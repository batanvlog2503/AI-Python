
# setMouseCallback()

# syntax cvsetMouseCallback(winname, Mousecallback(function), )

# def func(event, x, y, flag, param)
#.......... event là các sự kiện
# x. y là tọa độ chuột trong aảnh
# flag là trạng thái phím hoặc chuột

# 🔹 Các loại sự kiện chuột (event):
# Sự kiện	Ý nghĩa
# cv2.EVENT_MOUSEMOVE	Di chuyển chuột
# cv2.EVENT_LBUTTONDOWN	Nhấn chuột trái
# cv2.EVENT_LBUTTONUP	Nhả chuột trái
# cv2.EVENT_LBUTTONDBLCLK	Nhấp đúp chuột trái
# cv2.EVENT_RBUTTONDOWN	Nhấn chuột phải
# cv2.EVENT_RBUTTONUP	Nhả chuột phải
# cv2.EVENT_RBUTTONDBLCLK	Nhấp đúp chuột phải
# cv2.EVENT_MBUTTONDOWN	Nhấn nút chuột giữa
# cv2.EVENT_MBUTTONUP	Nhả nút chuột giữa
# cv2.EVENT_MBUTTONDBLCLK	Nhấp đúp nút chuột giữa
# cv2.EVENT_MOUSEWHEEL	Cuộn chuột (lên/xuống)
# cv2.EVENT_MOUSEHWHEEL	Cuộn ngang chuột



import cv2

def drawCircle(event, x, y, flag, param):
    if(event == cv2.EVENT_MOUSEMOVE):
        cv2.circle(img,(x, y), 10, (0, 0, 255), -1)



path = r"D:\Project Python AI\OpenCV\Img\meo1.jpg"

img = cv2.imread(path)

cv2.namedWindow("ImageCat")
cv2.setMouseCallback("ImageCat", drawCircle)



while(1):
    cv2.imshow("ImageCat", img)
    # nghĩa là sẽ đợi 20ms thì người dùng ms được nhấn
    if cv2.waitKey(20) & 0xff == 27: # Esc
        break