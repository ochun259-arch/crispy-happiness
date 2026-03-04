# 使用arange函数创建Ndarray数组
import numpy as np

# 创建一个从0到9的数组
arr1 = np.arange(10)
print(arr1)

# 创建一个从5到14的数组，步长为2
arr2 = np.arange(5, 15, 2)
print(arr2)

# 创建一个从0到1的数组，包含10个值（步长为0.1）
arr3 = np.arange(0, 1, 0.1)
print(arr3)

# 指定数据类型
arr4 = np.arange(10, dtype=np.float32)
print(arr4)