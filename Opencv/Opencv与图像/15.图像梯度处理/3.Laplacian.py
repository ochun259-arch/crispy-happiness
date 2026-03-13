import cv2
import numpy as np

# 1. 图像输入
image_np = cv2.imread('./shudu.png')

# 2. 进行卷积
image_Laplacian = cv2.Laplacian(image_np, -1)

# 3. 图像显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_Laplacian', image_Laplacian)
cv2.waitKey(0)