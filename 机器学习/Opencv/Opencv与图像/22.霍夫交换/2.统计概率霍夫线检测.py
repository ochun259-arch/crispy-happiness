# 导入OpenCV库
import cv2
import numpy as np

# 1. 读取图像
image_np = cv2.imread('./picture.png')
image_shape = image_np.shape

# 2. 灰度化
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 3. Canny边缘检测  得到边缘点
image_canny = cv2.Canny(image_gray, 30, 70)
# 创建一个模板图，方便绘制检测结果
image_HoughLinesP = np.zeros(image_shape, dtype=np.uint8)

# 4. 统计概率霍夫直线检测
lines = cv2.HoughLinesP(image_canny, 0.8, np.pi / 180, 90, minLineLength=50, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image_HoughLinesP, (x1, y1), (x2, y2), (0, 0, 255))

# 结果显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_HoughLines', image_HoughLinesP)
cv2.waitKey(0)