import cv2

# 1. 读取要滤波的图像
image_np = cv2.imread('./lena.png')

# 2. 直接进行双边滤波
image_bil = cv2.bilateralFilter(image_np, 5, 150, 150)

cv2.imshow('image_np', image_np)
cv2.imshow('image_bil', image_bil)
cv2.waitKey(0)

