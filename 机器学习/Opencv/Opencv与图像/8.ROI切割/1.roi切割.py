import cv2
# 读取图片
image_np = cv2.imread("lena.png")

# 获取图像的宽和高
height,width = image_np.shape[0],image_np.shape[1]

# 指定切割区域
x_min,x_max = 270,400
y_min,y_max = 270,400

# 使用cv2.rectangle去画一个矩形框，方便调整切割范围
# rectangle()参数：
# 参数1：image_np要切割的图像
# 参数2：要切割的左上角坐标点
# 参数3：要切割的右下角坐标点
# 参数4：切割线条的颜色
# 参数5：切割线条的粗细程度
image_1= cv2.rectangle(image_np,(x_min-2,y_min-2),(x_max-2,y_max-2),(0,0,255),2)

# 使用np数组的切片进行图片切割
image_roi = image_np[y_min:y_max,x_min:x_max]

# 显示结果
cv2.imshow("1",image_1)
cv2.imshow("image_roi",image_roi)
cv2.waitKey(0)