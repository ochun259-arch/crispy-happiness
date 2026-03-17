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

# 6. 寻找最小外接矩形
# 注意：cv2.minAreaRect 只能一个一个轮廓的去返回结果
for cnt in contours:
    # cv2.minAreaRect 返回的是 角度、矩形中心、矩形的宽和高
    rect = cv2.minAreaRect(cnt)
    # 由于rect所包含的信息不能够帮我们直接去绘制旋转矩形
    # 所以需要使用cv2.boxPoints来帮我们获取旋转矩形的四个顶点坐标
    box = np.int0(cv2.boxPoints(rect))
    # 根据四个顶点坐标将最小外接矩形绘制出来
    # cv2.drawContours 的contours参数必须是contours级别的
    # 此时的box是cnt级别的
    cv2.drawContours(image_contour, [box], -1, (255, 0, 0), 2)

# 7. 结果显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_contour', image_contour)
cv2.waitKey(0)