import cv2

# 1. 读取要滤波的图像
image_np = cv2.imread('./lena.png')

# 2. 直接使用函数去进行中值滤波
image_median = cv2.medianBlur(image_np, 3)

# 3. 图像显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_median', image_median)
cv2.waitKey(0)