import cv2
import numpy as np

# 1. 读取图片
image_np = cv2.imread('./picture.png')

# 复制出一张图片，专门用来绘制轮廓
image_contour = image_np.copy()

# 2. 灰度化图片
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 3. 二值化图像
ret, image_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)

# 4. 寻找轮廓
contours, hierarchy = cv2.findContours(image_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 5. 绘制轮廓
cv2.drawContours(image_contour, contours, -1, (0, 0, 255), 2)

# 6. 绘制最小外接圆
# 6.1 通过cv2.minEnclosingCircle()函数获取最小外接圆的圆心和半径
# 注意：cv2.minEnclosingCircle()也是只能一个一个去获取最小外接圆
for cnt in contours:
    # cv2.minEnclosingCircle()返回的是圆心坐标和半径大小
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    # 返回的圆心坐标和半径都不是整数，都需要进行一次取整
    (x, y, radius) = np.int0((x, y, radius))
    # 使用cv2.circle()去进行画圆
    cv2.circle(image_contour, (x, y), radius, (255, 0, 0), 2)

# 7. 显示结果
cv2.imshow('image_np', image_np)
cv2.imshow('image_contour', image_contour)
cv2.waitKey(0)