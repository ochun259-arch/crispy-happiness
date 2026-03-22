import cv2

# 1. 读取图片
image_np = cv2.imread('./picture.png')

image_poly = image_np.copy()

# 2. 灰度化
image_gray = cv2.cvtColor(image_poly, cv2.COLOR_BGR2GRAY)

# 3. 二值化
ret, image_thresh = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)

# 4. 获取轮廓点的坐标
contours, hierarchy = cv2.findContours(image_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 5. 查找凸包，获取凸包点
cnt = contours[0]
hull = cv2.convexHull(cnt)
# print(type(hull))
# 6. 绘制凸包
image_poly = cv2.polylines(image_poly, [hull], True, (0, 0, 255), 2)

# 7. 结果显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_poly', image_poly)
cv2.waitKey(0)