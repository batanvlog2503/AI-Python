import cv2
import os
# cv2.imread(path, flag)
# cv2.IMREAD_COLOR : value 1 ảnh màu
# cv2.IMREAD_GRAYSCALE value0 ảnh đen trắg
# cv2.IMREAD_UNCHANGED value -1 ảnh có thêm kênh alpha

# cv2.imshow(window_name, image)


path = r"/OpenCV/Img/meo.jpg"
path1 = r"D:\Project Python AI\OpenCV\Img"
img = cv2.imread(path)
os.chdir(path1)
cv2.imshow("tai anh con meo", img)

cv2.waitKey(10000) # ms

# save ảnh
# cv2.imwrite(filename, image);

filename = "anh moi.png"
cv2.imwrite(filename, img)