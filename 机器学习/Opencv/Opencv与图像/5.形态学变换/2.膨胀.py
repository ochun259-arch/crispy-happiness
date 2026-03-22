# 对二值化图像进行膨胀操作
# 首先去导入opencv库，方便使用opencv的函数
import cv2

# 1. 读取图像
image_np = cv2.imread('./111.png')

# 2. 将彩色图像进行灰度化
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 3. 将灰度图进行二值化
ret, image_thresh = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)

# 4. 构建核
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

# 5. 膨胀操作
# dilate:用来对二值化图像进行膨胀操作
# 必须准备的两个参数：
# 第一个参数： 要膨胀的二值化图像
# 第二个参数： 构建好的结构化元素或者说核
image_dilate = cv2.dilate(image_thresh, kernel)

# 6. 显示图像
cv2.imshow('image_thresh', image_thresh)
cv2.imshow('image_dilate', image_dilate)
cv2.waitKey(0)