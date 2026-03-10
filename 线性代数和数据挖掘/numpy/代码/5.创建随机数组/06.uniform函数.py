import numpy as np
# 设置随机数种子
np.random.seed(100)

# 在 [0, 1) 范围内抽取一个浮点数
print(np.random.uniform())

# 在 [5, 10) 范围内抽取一个浮点数
print(np.random.uniform(5,10))

# 在 [0, 1) 范围内抽取一个 3x3 的浮点数数组
print(np.random.uniform(0,1,(3,3)))

# 在 [5, 10) 范围内抽取一个 2x3 的浮点数数组
print(np.random.uniform(5,10,(2,3)))