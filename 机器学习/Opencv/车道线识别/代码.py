import cv2
import numpy as np


# 读取图像
image = cv2.imread("2.png")

# 图像矫正
str = np.array([[50,270],[180,130],[300,130],[460,270]])
str = np.array(str, dtype=np.float32)
str1 = np.array([[0,270],[0,0],[480,0],[480,270]])
str1 = np.array(str1, dtype=np.float32)
M = cv2.getPerspectiveTransform(str,str1)
image_jz = cv2.warpPerspective(image,M,(image.shape[1],image.shape[0]),flags=cv2.INTER_CUBIC)

# 将图像转化为HSV形式
image_hsv = cv2.cvtColor(image_jz,cv2.COLOR_BGR2HSV)

# 定义车道线颜色的阈值
min_white = np.array([0,0,200])
max_white = np.array([180,30,255])

min_yellow = np.array([15,80,100])
max_yellow = np.array([35,255,255])

# inRange函数的作用：生成一个与原始图像大小相同的单通道图
# 第一个参数：原始图像
# 第二个参数：寻找的范围的最小值  是个数组
# 第三个参数：寻找的范围的最大值  是个数组
mask_white = cv2.inRange(image_hsv,min_white,max_white)
mask_yellow = cv2.inRange(image_hsv,min_yellow,max_yellow)

# 使用cv.bitwise_or函数合并两个掩膜
# 参数一：需要合并的掩膜1
# 参数二：需要合并的掩膜2
mask = cv2.bitwise_or(mask_white,mask_yellow)

# 膨胀
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
image_pz = cv2.dilate(mask, kernel,iterations=2)

#
cv2.imshow("image_hsv",image_hsv)
cv2.imshow("make_white",mask_white)
cv2.imshow("make",mask)
cv2.imshow("1",image_pz)
cv2.waitKey(0)