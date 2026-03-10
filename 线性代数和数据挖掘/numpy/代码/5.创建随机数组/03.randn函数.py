import numpy as np
# 设置随机数
np.random.seed(6)

# 返回一个从标准正态分布中抽取的单个随机数
print(np.random.randn())

# 返回5个从标准正态分布中抽取的5个随机数组
print(np.random.randn(5))

# 返回一个形状为（2，3）的从标准正态分布中抽取的随机数组
print(np.random.randn(2,3))