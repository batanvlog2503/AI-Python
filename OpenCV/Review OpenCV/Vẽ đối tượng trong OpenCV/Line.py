
# Vẽ đường thẳng
# Syntax = cv2.line(image, start, end, color ,thickness)
# X values - y value
# color is BGR we pass a tuple
# thickness it is the thickness of the line in px

import cv2

path = r"D:\Project Python AI\OpenCV\Img\meo1.jpg"

img = cv2.imread(path)

start_point = (0, 0)
end_point = (100, 100)
color = (0, 0, 255)
thickness = 7 # độ dày

img = cv2.line(img, start_point, end_point, color, thickness)
cv2.imshow("anh con meo", img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()



