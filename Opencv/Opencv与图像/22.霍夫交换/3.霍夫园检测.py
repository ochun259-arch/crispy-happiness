# 导入OpenCV库
import cv2
import numpy as np

# 1. 读取图像
image_np = cv2.imread('./picture.png')
image_shape = image_np.shape

# 2. 灰度化
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# # 3. Canny边缘检测  得到边缘点
# image_canny = cv2.Canny(image_gray, 30, 70)

# 4. 霍夫圆检测
# circles = cv2.HoughCircles(image_gray, cv2.HOUGH_GRADIENT, 1, 20, param1=70, param2=50)
circles = cv2.HoughCircles(image_gray, cv2.HOUGH_GRADIENT_ALT, 1.5, 20, param1=300, param2=0.9)
circles = np.int0(np.around(circles))

# 创建一个模板图，方便绘制检测结果
image_Circle = np.zeros(image_shape, dtype=np.uint8)

for circle in circles:
    x, y, radius = circle[0]
    cv2.circle(image_Circle, (x, y), radius, (0, 0, 255), 2)

# 结果显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_Circle', image_Circle)
cv2.waitKey(0)