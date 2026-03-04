import numpy as np
# 设置随机数种子
np.random.seed(5)

# 从0到10（不包含）之间随机生成一个整数
print(np.random.randint(10))

# 从3到10（不包含）之间随机生成一个整数
print(np.random.randint(3,10))

# 从 1 到 10（不包含）之间随机生成一个 3x3 的整数数组
print(np.random.randint(1,10,(3,3)))

# 从 1 到 10（不包含）之间随机生成一个 3x3 的整数数组，数据类型为 'int32'
print(np.random.randint(1,10,(3,3),"int32"))
