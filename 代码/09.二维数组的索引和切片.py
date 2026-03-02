# 二维数组的索引
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print('arr数组为：\n', arr)

# 只有一个索引指标时，会在第0维上索引，后面的维度保持不变
print('arr[0]为：', arr[0])

# 两个索引指标
print('arr[0][0]为：', arr[0][0])
print(arr[0][0])

# 两个索引指标
print('arr[0, 1]为：', arr[0, 1])


# 二维数组的切片
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('arr: \n', arr)

# 选择特定的一行
row1 = arr[1]
print(row1)

# 选择连续的多行
rows = arr[1:3]
print(rows)

# 选择不连续的多行
rows = arr[[0, 2]]
print(rows)

# 选择特定的一列
col1 = arr[:, 1]
print(col1)

# 选择连续的多列
cols = arr[:, 1:3]
print(cols)

# 选择不连续的多列
cols = arr[:, [0, 2]]
print(cols)

# 同时选择行和列
subset = arr[1:3, 1:3]
print(subset)