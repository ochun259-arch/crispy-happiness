import torch
import torch.nn as nn
from scipy.cluster.hierarchy import weighted
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
from torchvision import models
from torchvision.models import ResNet50_Weights
from torchvision import transforms
import cv2
from PIL import Image
import os
import numpy as np

from 深度学习.垃圾分类系统.xl import valid_dataloader, criterion, valid_dataset

# 设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 定义模型结构
model = models.resnet50(weights=None)
num_classes = 6
model.fc = nn.Linear(model.fc.in_features,num_classes)

# 加载训练好的模型参数
model.load_state_dict(torch.load("best_model.pth", map_location=device))

# 将模型数据加载到设备上
# model.to(device)

# 把模型设置为评估模式
model.eval()

# 数据预处理
# 预测时的预处理（与训练时的验证集一致）
predict_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),      # 中心裁剪，无随机性
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# 定义一个类别名称映射 (需要根据你数据集的文件夹顺序来设定)
class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

def dan():
    # 加载图片，并改为RGB图像
    image_path = input("请输入需要预测的单张图片")
    image = Image.open(image_path).convert('RGB')

    # 应用预处理
    image = predict_transforms(image)

    # 添加batch维度
    input_batch = image.unsqueeze(0)  # 形状: [1, 3, 224, 224]
    input_batch = input_batch.to(device)

    # 进行前向传播
    with torch.no_grad():
        outputs = model(input_batch)

    # 找到最大值的索引
    _, predicted_idx = outputs.max(1)

    # 将结果转化为整数
    predicted_idx = predicted_idx.item()

    # 得到最终预测结果
    predicted_class = class_names[predicted_idx]
    print(f"预测结果: {predicted_class}")

# 预测文件夹里所有图片
def duo():
    folder_path = input("请输入需要预测的文件夹路径")
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(folder_path, filename)

            # 预测
            image = Image.open(path).convert('RGB')
            image = predict_transforms(image)
            input_batch = image.unsqueeze(0).to(device)

            with torch.no_grad():
                outputs = model(input_batch)

            _, predicted_idx = outputs.max(1)
            predicted_class = class_names[predicted_idx.item()]

            print(f"{filename} -> {predicted_class}")

def ck():
    model.eval()
    val_loss = 0
    val_correct = 0

    # 存储所有预测结果和真实标签（用于计算精确率、召回率等）
    all_preds = []
    all_labels = []

    with torch.no_grad():  # 禁用梯度计算
        for images, labels in valid_dataloader:
            images, labels = images.to(device), labels.to(device)  # 将验证数据集传到设备上
            outputs = model(images)  # 前向传播，得到预测值
            loss = criterion(outputs, labels)  # 计算损失

            val_loss += loss.item()  # 因为loss的值是张量，用.item提取数值，让梯度不参与计算，减少占用内存
            _, predicted = outputs.max(1)  # _是用不到这个返回值的意思，outputs.max找到最大值类别索引
            val_correct += (predicted == labels).sum().item()  # 求预测和真实标签相等的布尔值的和，并转换为python数字类型

            # 收集预测结果和真实标签
            all_preds.extend(predicted.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    val_acc = val_correct / len(valid_dataset)  # 计算准确率
    val_loss = val_loss / len(valid_dataloader)  # 计算平均损失

    # ========== 计算精确率、召回率、F1、混淆矩阵 ==========
    # 转换为numpy数组
    all_preds = np.array(all_preds)
    all_labels = np.array(all_labels)

    # 1. 精确率 (Precision)
    precision = precision_score(all_labels, all_preds, average='weighted')

    # 2. 召回率 (Recall)
    recall = recall_score(all_labels, all_preds, average='weighted')

    # 3. F1分数
    f1 = f1_score(all_labels, all_preds, average='weighted')

    # 4. 混淆矩阵
    cm = confusion_matrix(all_labels, all_preds)

    # 打印结果
    print(f"\n验证集评估结果:")
    print(f"  损失值: {val_loss:.4f}")
    print(f"  准确率: {val_acc:.4f} ({val_acc * 100:.2f}%)")
    print(f"  精确率: {precision:.4f} ({precision * 100:.2f}%)")
    print(f"  召回率: {recall:.4f} ({recall * 100:.2f}%)")
    print(f"  F1分数: {f1:.4f} ({f1 * 100:.2f}%)")

    print(f"\n混淆矩阵:")
    print(cm)


if __name__ == "__main__":
    while True:
        print("\n" + "=" * 40)
        print("        垃圾分类系统")
        print("=" * 40)
        print("  1. 单张图片预测")
        print("  2. 多张图片批量预测")
        print("  3. 查看模型评估结果")
        print("  4. 退出系统")
        print("=" * 40)

        choice = input("请选择 (1-4): ").strip()

        if choice == "1":
            dan()
        elif choice == "2":
            duo()
        elif choice == "3":
            ck()
        elif choice == "4":
            print("\n感谢使用，再见！")
            break
        else:
            print("输入无效，请输入 1-4 之间的数字")





