import numpy as np
# 设置随机数
np.random.seed(6)

# 返回一个均值为0.0，标准差为1.0的正态分布中的单个随机数
print(np.random.normal())

# 返回一个均值为0.0，标准差为1.0的正态分布中的5个随机数
print(np.random.normal(size=5))

# 返回一个均值为5.0，标准差为3.0的正态分布中的5个随机数
print(np.random.normal(5,2,5))

# 返回一个均值为10.0，标准差为3.0的正态分布中的一个两行三列的二维数组
print(np.random.normal(10,3,(2,3)))