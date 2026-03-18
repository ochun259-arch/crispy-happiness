# 先导入opencv库
import cv2
import numpy as np

# 1. 读取图片
image_np = cv2.imread('lena.png')

# 2. 直接对numpy数组做数值运算
# 为了保证图像的数据处于0-255之内，且数据类型还得是整形
# clip函数： 是一个截断函数，你需要给它提供要截取的范围，提供截取的对象
image_brightness = np.uint8(np.clip(image_np * 1.0 + 50, 0, 255))

# 3. 显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_brightness', image_brightness)
cv2.waitKey(0)