import cv2
# 读文件
image = cv2.imread('./111.png')
# 灰度化
image_hui = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# 定义阈值和最大值
# thresh = 125
# maxval = 255
# 使用 cv2.THRESH_OTSU + 要二值化的方法的参数 二值化
ret,image_erzhihua = cv2.threshold(image_hui,125,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 打印计算出的阈值
print(ret)
# 显示图像
cv2.imshow('erzhihua',image_erzhihua)
cv2.waitKey(0)