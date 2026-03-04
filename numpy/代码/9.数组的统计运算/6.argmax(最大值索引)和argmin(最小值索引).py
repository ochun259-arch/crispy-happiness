"""
numpy.argmax(a, axis=None, out=None)
numpy.argmin(a, axis=None, out=None)
"""
import numpy as np
arr = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
print(arr)
# 找出整个数组中的最大值和最小值的索引位置
max_index = np.argmax(arr)
min_index = np.argmin(arr)
# 找出每一列中的最大值和最小值的索引位置
max_index_col = np.argmax(arr, axis=0)
min_index_col = np.argmin(arr, axis=0)
# 找出每一行中的最大值和最小值的索引位置
max_index_row = np.argmax(arr, axis=1)
min_index_row = np.argmin(arr, axis=1)
print(max_index)
print(min_index)

print(max_index_col)
print(min_index_col)
print(max_index_row)
print(min_index_row)