# tổng quan  template Matching
# là phương pháp nhận dạng đối tượng cơ bản và dễ sử dụng
# phương pháp sẽ sử dụng bức ảnh nhận dạng (ảnh đích)
# quét trong vùng của ảnh anguoonf
# tuy nhiên phương ơhaps có nhược điểm khi ảnh bị xoay, scale

# một số hàm phương pháp ảnh nguồn(I), ảnh template(T), ma trận kết quả(R)

# eval(expression, [globals, locals)

# matchTemplate(image, templ, method)
# method là phương pháp so khớp
# Tên phương pháp	Ý nghĩa
# cv2.TM_CCOEFF	Hệ số tương quan
# cv2.TM_CCOEFF_NORMED	Hệ số tương quan chuẩn hóa (thường dùng)
# cv2.TM_CCORR	Tương quan trực tiếp
# cv2.TM_CCORR_NORMED	Tương quan chuẩn hóa
# cv2.TM_SQDIFF	Tổng bình phương sai khác
# cv2.TM_SQDIFF_NORMED	Tổng bình phương sai khác chuẩn hóa
# Với TM_SQDIFF và TM_SQDIFF_NORMED, giá trị nhỏ hơn = khớp tốt hơn.
# Các phương pháp còn lại: giá trị lớn hơn = khớp tốt hơn.

# minMaxLoc() cv2.minMaxLoc() ->minVal,maxVal, minLoc, maxLoc
#syntax
#
# minVal	Giá trị pixel nhỏ nhất
# maxVal	Giá trị pixel lớn nhất
# minLoc	(x, y) của pixel min
# maxLoc	(x, y) của pixel max
import cv2

# doc 2 buc anh
path1 = r"D:\Project Python AI\OpenCV\Img\meo.jpg"
path2 = r"D:\Project Python AI\OpenCV\Img\z6991144215860_f7ea3d6ddb9701fd685b155c72157b7b.jpg"

s_img = cv2.imread(path1)
# convert BGR -> RGB
s_img = cv2.cvtColor(s_img, cv2.COLOR_BGR2RGB)
t_img = cv2.imread(path2)
# convert BGR -> RGB
t_img = cv2.cvtColor(t_img, cv2.COLOR_BGR2RGB)

method = eval("cv2.TM_CCOEFF")
s_img_copy = s_img.copy()

res =cv2.matchTemplate(s_img_copy, t_img, method)
# hiển thị 2 bức ảnh


# xác định vị trí pixel  max, min

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:
    top_left =  min_loc
else:
    top_left = max_loc

# nghĩa là ta tìm được vị trí top_left x y của ảnh t_img
# chỉ cần xác định chiều dài rộng là ra các điểm còn lại

heigh, width , channel = t_img.shape
bottom_right = (top_left[0] + width, top_left[1] + heigh)

cv2.rectangle(s_img, top_left, bottom_right, (188, 0, 0), 100)
print(f"pixel min")
#cv2.imshow("Anh Gốc",res)
cv2.imshow("ket qua", s_img)
k = cv2.waitKey(0) & 0xff
if(k == 27):
    cv2.destroyAllWindows()