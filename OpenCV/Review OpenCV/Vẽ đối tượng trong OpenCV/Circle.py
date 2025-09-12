

# vẽ đường tròn
# syntax cv2.circle(image, center_, radius, color, thickness)
# center(Xvalue, Yvalue)
import cv2

path = r"D:\Project Python AI\OpenCV\Img\meo1.jpg"

img = cv2.imread(path)

center = (100, 100)
r =  30
color = (0, 0, 255)
thickness = 8 # độ dày

img = cv2.circle(img, center, r, color, thickness)
cv2.imshow("OK", img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
