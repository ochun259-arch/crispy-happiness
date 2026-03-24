import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import torch
import torch.nn as nn
import numpy as np
from torch.utils.data import DataLoader, TensorDataset

# 1、散点输入
data = [[-0.5, 7.7], [1.8, 98.5], [0.9, 57.8], [0.4, 39.2], [-1.4, -15.7], [-1.4, -37.3], [-1.8, -49.1], [1.5, 75.6],
        [0.4, 34.0], [0.8, 62.3]]
# 转换成Numpy
data = np.array(data)
# 提取x和y
x_data = data[:, 0]
y_data = data[:, 1]

# 将x_data 和 y_data 转换成 tensor
x_train = torch.tensor(x_data, dtype=torch.float32)
y_train = torch.tensor(y_data, dtype=torch.float32)

# 用于封装张量，将输入张量和目标张量组成一个数据集
# 返回值能够按照索引获得数据和标签，例如(x_train[i], y_train[i])
dataset = TensorDataset(x_train, y_train)

# 设置随机数种子
seed = 42
torch.manual_seed(seed)

# 2、定义前向模型
"""
实际上最常用的
"""


class LinearModel(nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = nn.Linear(1, 1)
        self.linear2 = nn.Linear(2, 1)

    def forward(self, x):
        x = self.linear(x)
        return x


model = LinearModel()

# 3、定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 4、开始迭代
epoches = 500

# dataloader可迭代的对象，每次迭代会生成一个批次的数据，由 输入张量和目标张量元组 组成。
dataloader = DataLoader(dataset, batch_size=10, shuffle=True)

for n in range(1, epoches + 1):
    total_loss = 0
    for batch_x, batch_y in dataloader:
        y_hat = model(batch_x.unsqueeze(1))
        # 计算损失
        loss = criterion(y_hat.squeeze(1), batch_y)

        total_loss += loss

        # 作用：清空之前存储在优化器中的梯度
        optimizer.zero_grad()
        # 计算损失函数关于模型参数的梯度
        loss.backward()
        # 根据优化算法去更新参数
        optimizer.step()

    # 计算的是平均损失
    avg_loss = total_loss / len(dataloader)

    # 5、显示频率设置
    if n % 10 == 0 or n == 1:
        print(f"epoches:{n}, avg_loss:{avg_loss}")