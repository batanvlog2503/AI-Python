
import cv2

# and
# cv2.bitwise_and(source1, source2, destination, mask)

path1 = r"D:\Project Python AI\OpenCV\Img\opencv_bitwise_not.webp"
path2 = r"D:\Project Python AI\OpenCV\Img\opencv_bitwise_not.webp"

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

# mau den la 0 mau trang la 1
dest_and = cv2.bitwise_and(img2, img1, mask = None)
dest_or = cv2.bitwise_or(img2, img1, mask = None)
dest_xor = cv2.bitwise_xor(img2, img1, mask = None)
dest_not = cv2.bitwise_not(img2, img1, mask = None)

cv2.imshow("anh 1", img1)
cv2.imshow("anh 2", img2)
cv2.imshow("anh dest_and", dest_xor)

#0xff == 27 la nut esc
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

