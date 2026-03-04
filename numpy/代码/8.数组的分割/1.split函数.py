import numpy as np

# 1d等分
arr = np.arange(10)  # 创建数组[0,1,2,3....9]
print("原数组：",arr)

# 将数组等分为2份
result = np.split(arr,2)
print("分割结果：",result)
for sub_arr in result:
    print(sub_arr)

# 1d索引位置切割
arr = np.arange(10)
print("原数组：",arr)

# 在索引3和6处分割数组，返回三个部分：arr[:3],arr[3:6],arr[6:]
result = np.split(arr,[3,6])
print("分割结果：",result)
for sub_arr in result:
    print(sub_arr)

# 2d行方向分割
arr = np.arange(12).reshape(4,3)
print("原始数组：\n",arr)

# 沿轴0分割为2部分，每部分包含2行
result = np.split(arr,2,axis=0)
print("沿轴0分割的结果：",result)
for sub_arr in result:
    print(sub_arr)

# 2d列方向分割
arr = np.arange(12).reshape(4,3)
print("原数组:\n",arr)

# 沿轴1分割为3部分，每部分都包含1列
result = np.split(arr,3,axis=1)
print("沿轴1分割的结果：",result)
for sub_arr in result:
    print(sub_arr)
