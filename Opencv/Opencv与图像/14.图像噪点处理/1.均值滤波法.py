import cv2

# 1. 读取要滤波的图像
image_np = cv2.imread('./lena.png')

# 2. 获取卷积核（滤波器）并进行均值滤波操作
image_blur = cv2.blur(image_np, (5, 5))

# 3. 显示结果
cv2.imshow('image_np', image_np)
cv2.imshow('image_blur', image_blur)
cv2.waitKey(0)