# 使用阈值法去二值化一张图像，且该图像必须是灰度图

import cv2
import numpy as np

# 首先还是使用opencv去读取一张图片
image_np = cv2.imread(r'..\test\tp.jpg')    # 中文路径会报错
# image_shape = image_np.shape

# 使用opencv的函数 cvtColor去灰度化彩色图
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 定义阈值法所需要的阈值
thresh = 150

# 定义阈值法所需要的最大值
maxval = 255

# 使用opencv的接口函数去二值化灰度图
# 其中，ret存放的是二值化所用的阈值，如果我们使用阈值法等方法时，ret没有任何作用
# 当我们使用OTSU去计算最合适的阈值时，ret就有用了
# image_thresh里存放的是二值化的图(本质上是与image_gray大小相同的单通道数组)
ret, image_thresh = cv2.threshold(image_gray, thresh, maxval, cv2.THRESH_BINARY)

# 为了能够遍历到灰度图的所有像素点，所以需要获取灰度图的形状
image_shape = image_gray.shape

# 创建一个与灰度图大小相同的单通道图像，用来接收灰度图与阈值比较的结果
image_thresh1 = np.zeros((image_shape[0], image_shape[1]), dtype=np.uint8)




# 因为需要将灰度图中的所有像素点的像素值与阈值进行比较
# 所以需要使用循环去遍历灰度图，并去除所有的像素值与阈值进行一一比较
# 如果像素值大于阈值，就设置为maxval，否则就设置0
for i in range(image_shape[0]):
    for j in range(image_shape[1]):
        # 使用if判断灰度图中的第i行第j列的像素点的像素值与阈值的大小关系
        # 如果灰度图的第i行第j列比阈值大，就将该像素设置为maxval
        if image_gray[i, j] > thresh:
            image_thresh1[i, j] = maxval
        # 否则的话，就设置为0
        else:
            image_thresh1[i, j] = 0

# 使用opencv的函数  imshow去显示结果
# 显示原图像
cv2.imshow('image_np', image_np)

# 显示灰度图
cv2.imshow('image_gray', image_gray)

# # 显示二值化结果
cv2.imshow('image_thresh', image_thresh)

# 显示opencv的接口二值化后的图像
cv2.imshow('image_thresh1', image_thresh1)

# 使用waitKey()去固定窗口
cv2.waitKey(0)