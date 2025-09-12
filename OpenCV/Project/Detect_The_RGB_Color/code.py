
import cv2
import numpy as np
url = "http://192.168.0.101:4747/video"

cap = cv2.VideoCapture(url)

while(True):

    ret, frame = cap.read()

    if not ret:
        print("Khong tim thay camera")
     # theo tiêu chuẩn BGR
    b_frame = frame[:,:,0]
    g_frame = frame[:,:,1]
    r_frame = frame[:,:,2]

    b = np.mean(b_frame)
    g = np.mean(g_frame)
    r = np.mean(r_frame)


    if b > g and b > r:
        print("That is blue")
    elif g > b and g > r:
        print("That is green")
    else:
        print("That is red")

    cv2.imshow("Detect Color", frame)

    if cv2.waitKey(1) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()