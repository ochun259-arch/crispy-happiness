# 在这个文件中，使用平均值的方法去灰度化一张彩色图
import numpy as np
import cv2

# 1. 使用opencv的imread函数去读取要灰度化的图片
image_np = cv2.imread('./tp.jpg')

# 2. 获取彩色图的形状，方便后续建立灰度图的模板
# shape获取到的顺序是高和宽
image_shape = image_np.shape

# 3. 创建灰度图模板，方便后续去接收彩色图所计算的灰度结果
# np.zeros也是按照高和宽的顺序去创建图像
image_gray = np.zeros((image_shape[0], image_shape[1]), dtype=np.uint8)

# 4.遍历彩色图中的每个像素点，使用平均值的方法去计算每个像素点的灰度值
# 使用嵌套的for循环去遍历彩色图的所有像素点
for i in range(image_shape[0]):
    for j in range(image_shape[1]):
        # 在循环中，获取彩色图中的每个像素点的平均值，并将其赋值给灰度模板图的对应位置
        image_gray[i][j] = (int(image_np[i, j][0]) + int(image_np[i, j][1]) + int(image_np[i, j][2])) // 3

# 5. 显示图像
cv2.imshow('image_np', image_np)
cv2.imshow('image_gray', image_gray)

cv2.waitKey(0)