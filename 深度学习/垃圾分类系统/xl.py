import random
import numpy as np
import os
import torch
from torchvision import datasets,transforms
from torch.utils.data import DataLoader, random_split
import torchvision.models as models
import torch.nn as nn
import torch.optim as optim
from torchvision.models import ResNet50_Weights


"""设置随机数种子"""
def setup_seed(seed):
    np.random.seed(seed)
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True

setup_seed(42)

"""设置设备"""
device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
print(f"使用的设备为{device}")

"""数据预处理"""
# transforms.Compose()会将括号内的操作打包为一个组合操作
train_transforms = transforms.Compose([
    transforms.Resize(256),             # 同一尺寸
    transforms.RandomCrop(224),         # 将图像随机裁剪
    transforms.RandomHorizontalFlip(),    # 将图像随机翻转
    transforms.ToTensor(),              # 转化为张量并缩放到[0,1]（因为计算机只看得懂向量）
    transforms.Normalize(               # 数据标准化
        mean=[0.485, 0.456, 0.406],     # ImageNet的均值
        std=[0.229,0.224,0.225]         # ImageNet的标准差
    )
])

"""加载数据集"""
# 设置参数transform = train_transforms，让每个加载进来的数据都经过train_transforms处理
full_dataset = datasets.ImageFolder('./data_xl',transform = train_transforms)

"""获取数据集的种类"""
num_classes = len(full_dataset.classes)

"""划分数据集和验证集"""
total_size = len(full_dataset)
train_size = int(0.8 * total_size)     # 将数据集的百分之八十划为训练集
val_size = total_size - train_size     # 剩余的百分之二十为测试集
#random_split会从这一个完整的数据集中，随机抽取样本，组成两个新的数据集
train_dataset,valid_dataset = random_split(
    full_dataset,                                   # 要切分的完整数据集
[train_size, val_size],                     # 切分后每个子集的样本数量
    generator=torch.Generator().manual_seed(66)     # 设置随机数
)

"""为不同数据集创建 DataLoader"""
# 把数据集变成一个可以批量、高效、自动打乱地给模型喂数据的迭代器
train_dataloader = DataLoader(train_dataset,batch_size=32,shuffle=True)
valid_dataloader = DataLoader(valid_dataset,batch_size=32,shuffle=False)

"""加载预训练模型resnet50"""
model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
"""添加冻结层，防止过拟合，加快训练"""
for param in model.parameters():
    param.requires_grad = False

"""维度转换"""
# model.fc是resnet最后一层的名字
# model.fc.in_features是resnet模型最后一层的维度
model.fc = nn.Linear(model.fc.in_features,num_classes)       # 将resnet模型的最后一层维度转为与数据集相同的维度，用于全连接计算

"""定义损失函数和优化器"""
criterion = nn.CrossEntropyLoss()                             # nn.CrossEntropyLoss交叉熵损失函数
optimizer = torch.optim.Adam(model.fc.parameters(),lr=0.001)  # 使用Adam优化器优化未冻结的model.fc.parameters()层

if __name__ == "__main__":
    """模型训练"""
    num_epoch = 30
    best_val_acc = 0  # 用来记录最佳模型的准确率

    for epoch in range(num_epoch):
        model.train()  # 把模型调到训练模式
        train_loss = 0
        train_correct = 0

        for images, labels in train_dataloader:
            # 把数据放在设备上
            images, labels = images.to(device), labels.to(device)
            # 前向传播
            outputs = model(images)
            # 计算损失
            loss = criterion(outputs, labels)
            # 反向传播
            optimizer.zero_grad()  # 清空旧的梯度
            loss.backward()  # 计算新的梯度
            # 更新参数
            optimizer.step()
            # 统计（用于打印进度）
            train_loss += loss.item()  # 因为loss的值是张量，用.item提取数值，让梯度不参与计算，减少占用内存
            _, predicted = outputs.max(1)  # _是用不到这个返回值的意思，outputs.max找到最大值类别索引
            train_correct += (predicted == labels).sum().item()  # 求预测和真实标签相等的布尔值的和，并转换为python数字类型

        train_acc = train_correct / len(train_dataset)  # 计算准确率
        train_loss = train_loss / len(train_dataloader)  # 计算平均损失

        # 验证模型
        model.eval()
        val_loss = 0
        val_correct = 0

        with torch.no_grad():  # 禁用梯度计算
            for images, labels in valid_dataloader:
                images, labels = images.to(device), labels.to(device)  # 将验证数据集传到设备上
                outputs = model(images)  # 前向传播，得到预测值
                loss = criterion(outputs, labels)  # 计算损失

                val_loss += loss.item()  # 因为loss的值是张量，用.item提取数值，让梯度不参与计算，减少占用内存
                _, predicted = outputs.max(1)  # _是用不到这个返回值的意思，outputs.max找到最大值类别索引
                val_correct += (predicted == labels).sum().item()  # 求预测和真实标签相等的布尔值的和，并转换为python数字类型

        val_acc = val_correct / len(valid_dataset)  # 计算准确率
        val_loss = val_loss / len(valid_dataloader)  # 计算平均损失

        print(f"Epoch [{epoch + 1}/{num_epoch}] "
              f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f} | "
              f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")

        """保存模型"""
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), 'best_model.pth')
            print(f"  ✓ 保存最佳模型 (验证准确率: {val_acc:.4f})")

    print(f"\n训练完成！最佳验证准确率: {best_val_acc:.4f}")