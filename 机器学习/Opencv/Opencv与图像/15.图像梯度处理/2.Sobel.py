import cv2
import numpy as np

# 1. 图像输入
image_np = cv2.imread('./test.png')

image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 2. 进行卷积运算
image_Sobel = cv2.Sobel(image_np, -1, 1, 0)

# 3. 图像显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_Sobel', image_Sobel)
cv2.waitKey(0)