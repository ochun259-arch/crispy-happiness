import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# 1. 读取数据集
data = pd.read_excel('Real estate valuation data set.xlsx')
# 打印前几行数据，检查有没有成功读取
print(data.head())

'''
为什么要进行one-hot编码处理？
将分类变量转换为模型可理解的格式，避免错误的数值假设
'''
# 2. 处理数据集
# 对便利店的数量做one-hot编码处理
# pd.get_dummies()函数会将指定列的每个不同取值转换为一个新的二进制列，新的列名由原列名和取值组成
data = pd.get_dummies(data, columns=['X4 number of convenience stores'])

'''
监督学习需要明确的特征和目标
'''
# 提取特征和目标变量
X = data[['X1 transaction date', 'X2 house age',
          'X3 distance to the nearest MRT station', 'X5 latitude', 'X6 longitude',
          'X4 number of convenience stores_0',
          'X4 number of convenience stores_1',
          'X4 number of convenience stores_2',
          'X4 number of convenience stores_3',
          'X4 number of convenience stores_4',
          'X4 number of convenience stores_5',
          'X4 number of convenience stores_6',
          'X4 number of convenience stores_7',
          'X4 number of convenience stores_8',
          'X4 number of convenience stores_9',
          'X4 number of convenience stores_10']]
y = data['Y house price of unit area']

# 将数据随即划分为训练集和测试集
# 第一种方式：使用sklearn自带的函数去随机划分数据集
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 第二种划分数据集的方式：将数据集按顺序划分训练集和测试集
train_ratio = 0.8
X, y = shuffle(X, y)
X_train = X[:int(train_ratio * len(data))]
X_test = X[int((train_ratio) * len(data)):]
y_train = y[:int(train_ratio * len(data))]
y_test = y[int((train_ratio) * len(data)):]

# 对数据进行标准化
# 使用StandardScaler可以将数据标准化为均值为0，方差为1的分布，有利于后续的模型训练
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 将处理好的数据转换为tensor，方便后续使用
X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)
X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)
y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1)


# 定义线性回归模型
class LinearRegressionModel(nn.Module):
    def __init__(self, input_size):
        super(LinearRegressionModel, self).__init__()
        # 定义一个线性层，输入维度是input_size，输出维度为1，对应预测的房价
        self.linear = nn.Linear(input_size, 1)

    def forward(self, x):
        # 前向传播函数，定义了数据如何通过模型计算，在这里直接返回线性层的计算结果
        return self.linear(x)


# 实例化模型
model = LinearRegressionModel(X_train_tensor.shape[1])

# 定义损失函数和优化器
# 使用均方误差损失函数(MSELoss)来衡量预测值和真实值之间的差异
criterion = nn.MSELoss()

# 使用Adam优化器
optimizer = optim.Adam(model.parameters(), lr=0.1)

# 进行模型的训练
# 设置模型训练的次数
num_epochs = 1000
for epoch in range(num_epochs):
    # 将模型设置为训练模式
    model.train()

    # 清空梯度
    optimizer.zero_grad()

    # 前向传播，得到损失
    output = model(X_train_tensor)
    loss = criterion(output, y_train_tensor)

    # 根据得到的损失去进行反向传播
    loss.backward()
    # 根据计算得到的梯度，进行更新模型的参数
    optimizer.step()

    # 设置提示信息，显示训练过程中的一些数据
    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# 评估模型
# model.eval()将模型设置为评估模式
model.eval()

with torch.no_grad():
    # 将测试集的特征输入到模型中，得到预测值
    predictions = model(X_test_tensor)
    # 计算测试集上的损失，用于评估模型在未知数据上的表现
    test_loss = criterion(predictions, y_test_tensor)

# 使用matplotlib进行绘制结果
# 将tensor转换为numpy数据，方便后续绘图
predictions = predictions.numpy()
y_test_numpy = y_test_tensor.numpy()

# 创建第一个图形，用于绘制散点，展示预测值和实际值的对应关系
plt.figure(0)
# 绘制散点
plt.scatter(y_test_numpy, predictions, color='blue')
# 绘制线
plt.plot([min(y_test_numpy), max(y_test_numpy)], [min(y_test_numpy), max(y_test_numpy)], linestyle='--', color='red',
         linewidth=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Regression results')

# 创建第二个图形
plt.figure(1)

# 获取测试集索引的排序后的顺序
sorted_indices = X_test.index.argsort()
# 根据排序后的索引获取对应的实际值
y_test_sorted = y_test.iloc[sorted_indices]

# 将预测值转换为Series类型，并且根据排序后的索引获取对应的值
y_pred_sorted = pd.Series(predictions.squeeze()).iloc[sorted_indices]

# 绘制实际值的曲线，用圆形标记
plt.plot(y_test_sorted.values, label='Acatual Values', marker='o')
# 绘制预测值的曲线，用*标记
plt.plot(y_pred_sorted.values, label='Predicted Values', marker='*')

# 设置轴标签和标题
plt.xlabel('Sorted Index')
plt.ylabel('Values')
plt.title('Actual vs Predicted Values in Linear Regression')
plt.show()