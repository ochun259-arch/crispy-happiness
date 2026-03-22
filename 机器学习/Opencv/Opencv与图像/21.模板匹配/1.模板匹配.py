# 导入Opencv库
import cv2
import numpy as np

# 1. 读取图片
image_np = cv2.imread('./picture.png')
template = cv2.imread('./muban.png')

# 2. 对读取到的模板图及原图像进行灰度化
image_np_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# 获取模板图的宽和高，方便后面进行绘图
h, w = template_gray.shape[:2]

# 3. 进行模板匹配的操作
res = cv2.matchTemplate(image_np_gray, template_gray, cv2.TM_CCOEFF_NORMED)
print(res)

# 4. 对返回的结果做进一步处理
threshold = 0.57

# 对某数组的数据进行判断，如果满足条件，就返回其对应的坐标
# 这里要注意的是，他返回的是行和列的坐标。
# 对应到Opencv里，就是某一个点的y和x的坐标
location = np.where(res > threshold)

# print(location)
# print(location[::-1])
# for i in zip(*location[::-1]):
#     print(i)

# 5. 对得到的点的坐标进行翻转处理，并再原图中框出来
for left_top in zip(*location[::-1]):
    right_bottom = (left_top[0] + w, left_top[1] + h)
    cv2.rectangle(image_np, left_top, right_bottom, (0, 0, 255))

# # 6. 显示模板匹配的结果
cv2.imshow('image_np', image_np)
cv2.waitKey(0)