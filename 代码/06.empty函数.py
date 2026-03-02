# empty: 创建空数组/创建未初始化的数组
import numpy as np

# 创建一个形状为 (2, 3) 的空数组
x = np.empty((2, 3))
print(x)

# 创建一个形状为 (2, 3) 的空数组，数据类型为整型
y = np.empty((2, 3), dtype=int)
print(y)