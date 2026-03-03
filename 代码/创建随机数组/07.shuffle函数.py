import numpy as np
# 设置随机数种子
np.random.seed(99)

# 创建一个numpy数组
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# 打乱数组
np.random.shuffle(arr)
print(arr)