import cv2

path = r"D:\Project Python AI\OpenCV\Img\he-mau-rgb.png"

img = cv2.imread(path)

# Tách kênh màu BGR
b = img[:, :, 0]  # Blue channel
g = img[:, :, 1]  # Green channel
r = img[:, :, 2]  # Red channel

# # Hiển thị ảnh kênh blue
# cv2.imshow("anh blue", b)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print("Kiểu dữ liệu:", type(img))         # <class 'numpy.ndarray'>
print("Kích thước:", img.shape)           # (chiều cao, chiều rộng, số kênh)
print("Số chiều:", img.ndim)              # 3 nếu ảnh màu, 2 nếu ảnh grayscale
print("Kiểu dữ liệu pixel:", img.dtype)   # thường là uint8 (0-255)
print("Số phần tử:", img.size)            # tổng số pixel * số kênh
print("Chiều cao (rows):", img.shape[0])  # số hàng
print("Chiều rộng (cols):", img.shape[1]) # số cột
print("Số kênh:", img.shape[2])
print(img.dtype)


# truy cập vùng ảnh
# roi = img[y1:y2, x1:x2] hàng y1 đến y2 và x cũng vậy

a = img[200:300, 100:200]


cv2.imshow("meo", a)
cv2.waitKey()
