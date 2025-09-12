
# vẽ text

#syntax cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[,
#bottomLeftOrigin]]])
# text: Text String to be drawn
# org : Tọa độ (x, y) của góc dưới bên trái của chữ trên ảnh.
# fontScale Hệ số phóng to chữ (giống cỡ chữ).
# lineType Kiểu đường vẽ: cv2.LINE_AA (mượt), cv2.LINE_4, cv2.LINE_8.
# bottomLeftOrigin:Nếu True, gốc ảnh ở dưới trái; mặc định là False.

import cv2

path = r"D:\Project Python AI\OpenCV\Img\meo1.jpg"

img = cv2.imread(path)

font = cv2.FONT_HERSHEY_SIMPLEX
org = (100, 100)
fontScale = 1
color = (0, 255, 0)
thickness = 4

img = cv2.putText(img, "Thanh Tan PTIT", org, font, fontScale, color, thickness)


cv2.imshow("anh con meo", img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()