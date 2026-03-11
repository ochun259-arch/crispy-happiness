# 对二值化图像进行腐蚀操作

# 先导入opencv的库，方便后续直接调用函数
import cv2

# 1. 读取一张要操作的彩色图像
image_np = cv2.imread('./111.png')

# 2. 将彩色图转化为灰度图
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 3. 将灰度图转化为腐蚀操作所需要的二值化图
ret, image_thresh = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)

# 4. 进行腐蚀操作：
# 4.1 构建腐蚀操作所需要用到的核
# cv2.getStructuringElement: 用来生成形态变换所需要用到的核
# 第一个参数：指定核的形状： cv2.MORPH_CROSS 表示十字形， cv2.MORPH_RECT 表示矩形  cv2.MORPH_ELLIPSE表示椭圆
# 第二个参数：指定核的大小： 以元组的形式传递
# 第三个参数：指定十字形核的核值分布
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))

# 4.2 去进行滑动计算
# erode: 用来对二值化图像进行腐蚀操作： 必须要准备两个参数
# 第一个：要进行腐蚀的二值化图像
# 第二个：用来滑动计算的结构化元素
image_erode = cv2.erode(image_thresh, kernel)

# 5. 显示图像
cv2.imshow('image_thresh', image_thresh)
cv2.imshow('image_erode', image_erode)
cv2.waitKey(0)