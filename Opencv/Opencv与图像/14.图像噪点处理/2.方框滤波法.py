import cv2

# 1. 读取要滤波的图像
image_np = cv2.imread('./lena.png')

# 2. 直接进行方框滤波
image_box = cv2.boxFilter(image_np, -1, (3, 3), normalize=False)

# 图像显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_box', image_box)
cv2.waitKey(0)