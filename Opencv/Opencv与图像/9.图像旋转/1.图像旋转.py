import cv2
image = cv2.imread("lena.png")
# 定义旋转角度和图片缩放的比例
angle = 45
scale = 0.5

# 获取原始图像大小
image_shape = image.shape

# 构建旋转矩阵
# cv2.getRotationMatrix2D的参数：
# 参数1：旋转中心
# 参数2：旋转角度
# 参数3：缩放比例
M = cv2.getRotationMatrix2D((image_shape[1],image_shape[2]),angle,scale)

# 进行图像旋转
# cv2.warpAffine的参数：
# 参数1：要旋转的对象
# 参数2：旋转矩阵
# 参数3：输出图像的大小
# 参数4：插值方法
# 参数5：边界模式
image_rotation = cv2.warpAffine(image,M,(image_shape[1],image_shape[0]),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_WRAP)
# cv2.INTER_LINEAR是线性插值
# cv2.BORDER_WRAP是包裹填充

# 显示结果
cv2.imshow("image_rotation",image_rotation)
cv2.waitKey(0)