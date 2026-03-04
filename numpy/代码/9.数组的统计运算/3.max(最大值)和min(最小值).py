"""
numpy.max(a, axis=None, out=None, keepdims=<no value>, initial=<no
value>, where=<no value>)
"""
import numpy as np

# 1、基本用法
arr = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
print(arr)
# 计算整个数组的最大值
max_val = np.max(arr)
# 计算每一列的最大值
max_val_col = np.max(arr, axis=0)
# 计算每一行的最大值
max_val_row = np.max(arr, axis=1,initial=0)
print(max_val)
print(max_val_col)
print(max_val_row)

"""
numpy.min(a, axis=None, out=None, keepdims=<no value>, initial=<no
value>, where=<no value>)
"""
import numpy as np
arr = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
print(arr)
# 计算整个数组的最小值
min_val = np.min(arr)
# 计算每一列的最小值
min_val_col = np.min(arr, axis=0)
# 计算每一行的最小值
min_val_row = np.min(arr, axis=1)
print(min_val)
print(min_val_col)
print(min_val_row)