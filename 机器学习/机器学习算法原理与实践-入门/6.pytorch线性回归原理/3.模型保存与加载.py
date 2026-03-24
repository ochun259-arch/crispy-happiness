import numpy as np
import torch
import torch.nn as nn
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

# 转换为 TensorDataset
dataset = TensorDataset(x_train, y_train)

# 设置随机数种子
seed = 42
torch.manual_seed(seed)


# 2、定义前向模型
class LinearModel(nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        x = self.linear(x)
        return x


model = LinearModel()
# 3、定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 4、开始迭代
epochs = 500

# 创建 DataLoader
dataloader = DataLoader(dataset, batch_size=10, shuffle=True)

for epoch in range(1, epochs + 1):
    total_loss = 0
    for batch_x, batch_y in dataloader:
        # 前向传播
        y_hat = model(batch_x.unsqueeze(1))
        # 计算损失
        loss = criterion(y_hat.squeeze(1), batch_y)
        total_loss += loss.item()

        # 反向传播和优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # 计算平均损失
    avg_loss = total_loss / len(dataloader)

    # 打印损失
    if epoch % 10 == 0 or epoch == 1:
        print(f"Epoch: {epoch}, Loss: {avg_loss}")
# 保存模型
# 这个方法将整个模型保存到文件中，包括模型的结构和参数。
# 文件中将包含模型的所有信息，包括网络结构、权重等。
torch.save(model, 'entire_model.pth')

# 加载保存的模型参数
# 如果保存的是整个模型，使用下面这行代码
model = torch.load('./entire_model.pth')
# 评估模型
model.eval()

# 使用模型进行预测
# 假设有一些输入数据x_test
x_test = torch.tensor([[1.2], [3.4], [5.6]], dtype=torch.float32)
with torch.no_grad():  # 在评估模式下，不需要计算梯度
    y_pred = model(x_test)

print(y_pred)

# 这个方法只保存模型的参数（即模型的状态字典），不保存模型的结构。
# 文件中将只包含模型的参数，没有模型的结构信息。
torch.save(model.state_dict(), 'model.pth')

# 如果保存的是模型的状态字典，使用下面这行代码
model.load_state_dict(torch.load('model.pth'))

# 评估模型
# 这里需要将模型设置为评估模式，即model.eval()
model.eval()

# 使用模型进行预测
# 假设有一些输入数据x_test
x_test = torch.tensor([[1.2], [3.4], [5.6]], dtype=torch.float32)
with torch.no_grad():  # 在评估模式下，不需要计算梯度
    y_pred = model(x_test)

print(y_pred)
