# import torch: 导入PyTorch深度学习框架的核心模块，提供张量操作、自动求导、神经网络层等基础功能
import torch

# import torch.nn.functional as F: 导入神经网络函数模块，包含激活函数、池化、卷积等无需可学习参数的函数操作
# 通常使用F别名调用，如F.relu()、F.softmax()等，这些函数不包含可训练参数，直接在forward中使用
import torch.nn.functional as F

# from torchsummary import summary: 导入模型结构可视化工具，可以打印出网络的每层输出形状和参数量
# summary()函数需要传入模型和输入尺寸，自动计算前向传播时各层的输出维度
from torchsummary import summary


# class LeNet5(torch.nn.Module): 定义一个继承自torch.nn.Module的神经网络模型类
# torch.nn.Module是所有神经网络模块的基类，任何自定义网络都必须继承它
class LeNet5(torch.nn.Module):

    # def __init__(self): 构造函数，在创建模型实例时自动调用，用于定义网络层结构
    # super(LeNet5, self).__init__() 调用父类torch.nn.Module的构造函数，必须写在__init__的第一行
    # 这是Python继承的标准写法，确保Module的初始化逻辑被执行
    def __init__(self):
        super(LeNet5, self).__init__()

        # self.conv1 = torch.nn.Conv2d(1, 6, 5, 1, 2): 定义第一个卷积层
        # Conv2d参数详解：
        #   in_channels=1: 输入通道数，灰度图为1，RGB图为3
        #   out_channels=6: 输出通道数（卷积核数量），每个卷积核提取不同特征
        #   kernel_size=5: 卷积核大小5x5，感受野大小为5
        #   stride=1: 卷积步长，卷积核每次移动1个像素
        #   padding=2: 零填充大小，在输入边界外填充2圈0，保持输出尺寸不变（计算公式：(28-5+2*2)/1+1=28）
        self.conv1 = torch.nn.Conv2d(1, 6, 5, 1, 2)

        # self.pool1 = torch.nn.AvgPool2d(2, 2): 定义第一个平均池化层
        # AvgPool2d参数详解：
        #   kernel_size=2: 池化窗口大小2x2，在2x2区域内取平均值
        #   stride=2: 池化步长，窗口每次移动2个像素（通常与kernel_size相同，不重叠池化）
        # 作用：降低特征图分辨率，减少参数量，提取主要特征，输出尺寸变为原来的一半
        self.pool1 = torch.nn.AvgPool2d(2, 2)

        # self.conv2 = torch.nn.Conv2d(6, 16, 5, 1): 定义第二个卷积层
        # Conv2d参数详解：
        #   in_channels=6: 输入通道数为6，承接上一层池化层的输出
        #   out_channels=16: 输出16个特征图，提取更高级的特征
        #   kernel_size=5: 卷积核大小5x5
        #   stride=1: 步长为1
        #   padding=0: 默认不填充，输入尺寸从14x14变为10x10（计算公式：(14-5)/1+1=10）
        self.conv2 = torch.nn.Conv2d(6, 16, 5, 1)

        # self.pool2 = torch.nn.AvgPool2d(2, 2): 定义第二个平均池化层
        # 参数与pool1相同，将10x10的特征图降采样为5x5
        self.pool2 = torch.nn.AvgPool2d(2, 2)

        # self.fc1 = torch.nn.Linear(5 * 5 * 16, 120): 定义第一个全连接层
        # Linear参数详解：
        #   in_features=5*5*16=400: 输入特征数量，需要将池化后的5x5x16特征图展平成一维向量
        #   out_features=120: 输出特征数量，LeNet5原始设计的全连接层神经元数
        # 全连接层的作用：将卷积层提取的局部特征进行全局组合，用于分类决策
        self.fc1 = torch.nn.Linear(5 * 5 * 16, 120)

        # self.fc2 = torch.nn.Linear(120, 84): 定义第二个全连接层
        # 参数：输入120个特征，输出84个特征，进一步降维和抽象特征
        self.fc2 = torch.nn.Linear(120, 84)

        # self.fc3 = torch.nn.Linear(84, 10): 定义输出层全连接层
        # 参数：输入84个特征，输出10个特征（对应MNIST数据集的10个数字类别0-9）
        # 输出层不使用激活函数，原始logits会传递给损失函数（如CrossEntropyLoss）
        self.fc3 = torch.nn.Linear(84, 10)

    # def forward(self, x): 定义前向传播函数，描述数据在网络中的流动路径
    # x: 输入张量，形状为[batch_size, channels, height, width]
    # 这个函数在model(input)时被自动调用，PyTorch的__call__机制会调用forward
    def forward(self, x):
        # x = self.pool1(F.relu(self.conv1(x))): 第一层卷积+激活+池化的组合操作
        # 执行顺序：先卷积(conv1) → 再ReLU激活 → 最后池化(pool1)
        # F.relu(): ReLU激活函数，将负数置为0，正数保持不变，公式: max(0, x)
        # 作用：引入非线性，让网络能够学习复杂模式，解决梯度消失问题
        x = self.pool1(F.relu(self.conv1(x)))

        # x = self.pool2(F.relu(self.conv2(x))): 第二层卷积+激活+池化组合
        # 数据流：conv2卷积提取特征 → ReLU激活增加非线性 → pool2降采样
        x = self.pool2(F.relu(self.conv2(x)))

        # x = x.view(-1, 16 * 5 * 5): 展平操作，将多维特征图转换为一维向量
        # view()是PyTorch的张量重塑函数，类似于NumPy的reshape
        # 参数详解：
        #   -1: 自动推断该维度大小（保持batch_size不变）
        #   16 * 5 * 5 = 400: 将每个样本的16通道x5高x5宽的特征图展平成400维向量
        # 为什么需要展平：全连接层要求输入是一维特征向量，不能直接处理二维特征图
        x = x.view(-1, 16 * 5 * 5)

        # x = F.relu(self.fc1(x)): 第一个全连接层+ReLU激活
        # fc1将400维特征映射到120维，ReLU激活增加非线性
        x = F.relu(self.fc1(x))

        # x = F.relu(self.fc2(x)): 第二个全连接层+ReLU激活
        # fc2将120维映射到84维，继续特征抽象
        x = F.relu(self.fc2(x))

        # x = self.fc3(x): 输出层全连接，不添加激活函数
        # fc3将84维映射到10维，输出每个类别的原始得分（logits）
        # 注意：不使用softmax是因为CrossEntropyLoss内部已经包含了softmax计算
        x = self.fc3(x)

        # return x: 返回前向传播的结果（logits）
        # 训练时这个输出会传给损失函数计算loss，推理时可通过softmax转为概率
        return x


# if __name__ == '__main__': Python标准写法，确保当该脚本被直接运行时执行下面的代码
# 如果该文件被import到其他脚本，则不会执行这部分，避免不必要的初始化
if __name__ == '__main__':
    # model = LeNet5().to("cuda"): 创建LeNet5模型实例并移动到GPU
    # LeNet5(): 实例化网络模型，会自动调用__init__方法
    # .to("cuda"): 将模型的所有参数和张量移动到GPU显存中，如果没有CUDA可用可改为"cpu"
    # 使用GPU可以大幅加速训练和推理
    model = LeNet5().to("cpu")

    # summary(model, (1, 28, 28)): 打印模型的详细结构和参数量统计
    # summary函数参数：
    #   model: 要分析的目标模型
    #   (1, 28, 28): 输入张量的尺寸（通道数，高度，宽度），不包含batch维度
    # 输出内容：每层的名称、输出形状、参数量、以及模型总参数量和可训练参数量
    # 注意：MNIST数据集是28x28的灰度图，所以输入通道为1
    summary(model, (1, 28, 28))