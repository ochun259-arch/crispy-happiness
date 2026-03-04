import numpy as np
# 创建两个数组
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(f'数组a的形状为{a.shape}, 数组a为：\n', a)
print(f'数组b的形状为{b.shape}, 数组b为：\n', b)
# 沿着第一个轴（垂直方向）连接数组
c = np.concatenate((a, b), axis=0)
print(f'数组c的形状为{c.shape}, 数组c为：\n', c)
# 沿着第二个轴（水平方向）连接数组
d = np.concatenate((a, b.T), axis=1)
print(f'数组b的转置的形状为{b.T.shape}, 数组b的转置为：\n', b.T)
print(f'数组d的形状为{d.shape}, 数组d为：\n', d)