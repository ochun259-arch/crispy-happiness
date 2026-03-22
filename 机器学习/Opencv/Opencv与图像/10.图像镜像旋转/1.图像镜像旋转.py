import cv2
image = cv2.imread("lena.png")
# 使用flip函数去对图像进行镜像翻转
# cv2.flip参数：
# 参数1：要翻转的对象
# 参数2：标志位，0表示绕x轴翻转，>0表示绕y轴翻转，<0表示绕x轴和y轴各进行一次翻转
image_flip = cv2.flip(image,0)
image_flip1 = cv2.flip(image,-1)
image_flip2 = cv2.flip(image,1)

cv2.imshow("image_flip",image_flip)
cv2.imshow("1",image_flip1)
cv2.imshow("2",image_flip2)
cv2.waitKey(0)