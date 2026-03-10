"""
numpy.where(condition)
"""
import numpy as np
# 1、根据条件返回元素的索引
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# 找到大于 5 的元素的索引
print(arr > 5)  # 根据True寻找索引
indices = np.where(arr > 5)

print("大于 5 的元素索引:", indices)
# 2、根据条件选择元素
arr = np.array([1, 2, 3, 4, 5])

# 如果元素大于 3，返回 "大于 3"，否则返回 "小于等于 3"
result = np.where(arr > 3, "大于 3", "小于等于 3")

print(result)
arr = np.array([1, 2, 3, 4, 5])

# 将大于 3 的元素替换为 10，其他元素保持不变
modified_arr = np.where(arr > 3, 10, arr)

print(modified_arr)