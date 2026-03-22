import cv2

# 1. 读取图像
image_np = cv2.imread('./picture.png')

# 2. 灰度化图像
image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 3. 高斯滤波
image_blur = cv2.GaussianBlur(image_np, (5, 5), 1.5)

# 4. 进行边缘检测
image_canny = cv2.Canny(image_blur, 30, 70)

# 5. 结果显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_canny', image_canny)
cv2.waitKey(0)