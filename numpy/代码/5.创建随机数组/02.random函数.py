import numpy as np
# 设置随机数种子
np.random.seed(10)

# 生成一个一维数组，包含五个随机数
arr = np.random.random(5)
print("arr:",arr)

# 生成一个二维数组，形状为（2，3）
arr1 = np.random.random((2,3,1))
print("arr1:",arr1)

arr2 = np.random.rand(2,3,1)
print("arr2:",arr2)