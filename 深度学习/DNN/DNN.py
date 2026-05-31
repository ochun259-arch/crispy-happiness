import torch
import numpy as np
from torch import nn

# 1.字符输入
text = "hey how are you"

# 2.数据集划分
input_seq = []
output_seq = []
window = 5
for i in range(0, len(text) - window, 1):
    input_seq.append(text[i:i + window])
    output_seq.append(text[i + window])

print("input_seq:", input_seq)
# print("output_seq:", output_seq)


# 3.数据编码：one-hot  做一个词典出来
chars = set(text)
chars = sorted(chars)
# print("chars:", chars)
# {" ":0, "a":1 }
char2int = {char: ind for ind, char in enumerate(chars)}
# print("char2int:", char2int)
# # {0:" ", 1: "a"}
int2char = dict(enumerate(chars))
# print("int2char:", int2char)
vocab_size = len(chars)
print("vocab_size:", vocab_size)
# 4、准备输入数据集
"""
    输入 ： 输入的字符
    输出 :  预测生成的一个字符
    例如 : 
            输入 ： hey h -> [1., 0., 1., 1., 0., 0., 0., 0., 1.]
            输出 ： o - > [0., 0., 0., 0., 1., 0., 0., 0., 0.] 
"""
# 4. 正确编码：每个字符独立 One-Hot
# 输入形状：[样本数, window, 字符数]
input_encoded = []
for seq in input_seq:
    onehots = []
    for c in seq:
        vec = np.zeros(vocab_size, dtype=np.float32)
        vec[char2int[c]] = 1
        onehots.append(vec)
    input_encoded.append(onehots)
# 输出：单个字符
output_encoded = []
for c in output_seq:
    vec = np.zeros(vocab_size, dtype=np.float32)
    vec[char2int[c]] = 1
    output_encoded.append(vec)

# 转 tensor
input_seq = torch.tensor(input_encoded)
output_seq = torch.tensor(output_encoded)

print("input_seq:", input_seq)
print("output_seq:", output_seq)
## 5. 模型（输入要把 5 个字符展平）
class Model(nn.Module):
    def __init__(self, vocab_size, hidden_size):
        super().__init__()
        self.in_dim = window * vocab_size  # 5*字符数
        self.fc1 = nn.Linear(self.in_dim, hidden_size)
        self.fc2 = nn.Linear(hidden_size, vocab_size)

    def forward(self, x):
        # x: [N,5,vocab] → 展平成 [N,5*vocab]
        x = x.reshape(x.size(0), -1)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = Model(vocab_size, 64)

# 打印权重矩阵
for name, param in model.named_parameters():
    print(f"参数名: {name}")
    print(f"形状: {param.shape}")
    print(f"数值: {param[:2]}")  # 只打印前2个值，避免刷屏
    print("-" * 50)

# 6.定义损失函数和优化器
cri = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 7.开始迭代
epochs = 2000
for epoch in range(1, epochs + 1):
    output = model(input_seq)
    loss = cri(output, output_seq)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    # 8.显示频率设置
    if epoch == 0 or epoch % 50 == 0:
        print(f"Epoch [{epoch}/{epochs}], Loss {loss:.4f}")

# 预测下一个字符
input_text = "hey ho"

# 只取后window个字符
input_text = input_text[-window:]
# 编码成 [bs,input_seq,vocab]
vecs = []
for c in input_text:
    v = np.zeros(vocab_size)
    v[char2int[c]] = 1
    vecs.append(v)
vecs = torch.tensor(vecs, dtype=torch.float32).unsqueeze(0)

model.eval()
with torch.no_grad():
    out = model(vecs)
idx = torch.argmax(out).item()
print("输入字符为:", input_text)
print("预测字符为:",int2char[idx])