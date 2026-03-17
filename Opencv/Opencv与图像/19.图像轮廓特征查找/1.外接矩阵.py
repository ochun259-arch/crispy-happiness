import cv2

# 1. 读取图片
image_np = cv2.imread('./picture.png')

# 复制出一张图片，专门用来绘制轮廓
image_contour = image_np.copy()

# 2. 灰度化图片
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 3. 二值化图像
ret, image_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)

# 4. 寻找轮廓
contours, hierarchy = cv2.findContours(image_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 5. 绘制轮廓
cv2.drawContours(image_contour, contours, -1, (0, 0, 255), 2)

# 6. 根据轮廓点的坐标寻找外接矩形
# 通过rectangle去画矩形
# 我们需要注意的是：boundingRect 这个函数返回的是 外接矩形的左上角的点的坐标及外接矩形的宽度和高度，它并不会为我们绘制矩形
# 且这个函数一次只能获取一个轮廓的外接矩形
for cnt in contours:
    # 通过cv2.boundingRect获取当前轮廓点所构成的外接矩形的左上角的点的坐标及外接矩形的宽度和高度
    x, y, w, h = cv2.boundingRect(cnt)
    # 此时的(x，y)就是左上角的点的坐标 w是矩形的宽度 h是矩形的高度
    top_left = (x, y)
    # 右下角的点的坐标
    bottom_right = (x + w, y + h)
    # 通过rectangle去绘制矩形
    cv2.rectangle(image_contour, top_left, bottom_right, (255, 0, 0), 2)

# 7. 显示结果
cv2.imshow('image_np', image_np)
cv2.imshow('image_contour', image_contour)
cv2.waitKey(0)