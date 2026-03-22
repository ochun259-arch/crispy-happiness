import cv2

# 1. 读取要滤波的图像
image_np = cv2.imread('./lena.png')

# 2. 直接进行高斯滤波
image_Gaussian = cv2.GaussianBlur(image_np, (5, 5), 3)

# 3. 图像显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_Gaussian', image_Gaussian)
cv2.waitKey(0)