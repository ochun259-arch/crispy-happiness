import cv2
image = cv2.imread("lena.png")

# 使用resize进行图片缩放
# dsize和fx、fy不能同时使用，如果同时出现，会以dsize的标准进行缩放
# 如果想要使用resize函数，就必须填入两个参数：src和dsize （src就是要操作的对象）
# 如果不想使用dsize，也要填写这个参数，可以赋值为None
# 参数1：操作对象
# 参数2：输出图像大小
# 参数3：fx是水平方向缩放的值，fy是垂直方向缩放的值
# 参数4：插值方法
image1 = cv2.resize(image,dsize=None,fx=0.1,fy=1,interpolation=cv2.INTER_LINEAR)

cv2.imshow("1",image1)
cv2.waitKey(0)