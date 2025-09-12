
# vẽ hình chữ nhật
# syntax cv2.rectangle(img, start, end, color, thichness)
import cv2

path = r"D:\Project Python AI\OpenCV\Img\meo1.jpg"

img = cv2.imread(path)

start_point = (0, 0)
end_point = (100, 100)
color = (0, 0, 255)
thickness = 7 # độ dày

img = cv2.rectangle(img, start_point, end_point, color, thickness)
cv2.imshow("anh con meo", img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()