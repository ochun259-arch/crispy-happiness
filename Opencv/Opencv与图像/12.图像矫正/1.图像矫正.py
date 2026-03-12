import cv2
import numpy as np

image = cv2.imread("test.png")

image_shape = image.shape

# 定义原始图像中四个顶点
points1 = np.array([[200, 100], [700, 150], [140, 400], [650, 460]])

# 定义目标图像中 这四个顶点坐标所对应的位置
points2 = np.array([[0, 0], [image_shape[1], 0], [0, image_shape[0]], [image_shape[1], image_shape[0]]])

# 转换为浮点型
points1 = np.array(points1, dtype=np.float32)
points2 = np.array(points2, dtype=np.float32)

cv2.line(image, points1[0].astype(np.int64).tolist(), points1[1].astype(np.int64).tolist(), (0, 0, 255), 1,
         lineType=cv2.LINE_8)
cv2.line(image, points1[0].astype(np.int64).tolist(), points1[2].astype(np.int64).tolist(), (0, 0, 255), 1,
         lineType=cv2.LINE_8)
cv2.line(image, points1[3].astype(np.int64).tolist(), points1[1].astype(np.int64).tolist(), (0, 0, 255), 1,
         lineType=cv2.LINE_8)
cv2.line(image, points1[3].astype(np.int64).tolist(), points1[2].astype(np.int64).tolist(), (0, 0, 255), 1,
         lineType=cv2.LINE_8)

# 获取透视变换矩阵
M = cv2.getPerspectiveTransform(points1,points2)

# 进行透视变换
image2 = cv2.warpPerspective(image,M,(image_shape[1],image_shape[0]),flags=cv2.INTER_CUBIC)

cv2.imshow("1",image2)
cv2.waitKey(0)