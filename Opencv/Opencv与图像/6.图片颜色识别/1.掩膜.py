# 对图片中的某些目标颜色进行识别

# 导入opencv的库，方便后续直接调用函数
import cv2
import numpy as np

# 1. 图片输入：准备一张原始图片
image_np = cv2.imread('./tp.jpg')

# resize: 将图像的大小进行修改，方便我们观察现象
image_np = cv2.resize(image_np, (700, 700))

# 2. HSV空间转换：将RGB颜色空间下的图像转化为HSV颜色空间下的图像
hsv_image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2HSV)

# 3. 制作掩膜：为了方便后续遮挡其他不关心的区域，去制作一个掩膜

# 创建hsv颜色区域的最小值数组  针对黄色区域
lowerb = np.array([26, 43, 46])
# 创建hsv颜色区域的最大值数组  针对黄色区域
upperb = np.array([34, 255, 255])

# 使用inRange函数，将hsv图像中的每一个值与lowerb和upperb进行比较
# 当hsv图像中的像素点的hsv值处于数组范围之内，这个像素点就是我们要找的颜色

# inRange函数的作用：生成一个与原始图像大小相同的单通道图，其值要么是255，要么是0
# 第一个参数：原始图像
# 第二个参数：寻找的范围的最小值  是个数组
# 第三个参数：寻找的范围的最大值  是个数组
mask_image_np = cv2.inRange(hsv_image_np, lowerb, upperb)

# 4. 与运算：将原始图像和原始图像进行位与操作，并使用掩膜去遮盖掉不关心的部分
color_image_np = cv2.bitwise_and(image_np, image_np, mask=mask_image_np)

# 5. 图像输出：把结果显示出来
cv2.imshow("mask_image_np", mask_image_np)
cv2.imshow('color_image_np', color_image_np)
cv2.waitKey(0)