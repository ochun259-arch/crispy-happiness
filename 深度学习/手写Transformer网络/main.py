import torch
import torch.nn as nn


# 定义一些参数或者超参数
d_model = 512  # 模型的隐藏层的维度
n_heads = 8  # 注意力头的数量
n_layers = 6  # transformer层的数量
d_ff = 2048  # 前馈神经网络中间层维度
batch_size = 32  # batch
src_seq_length = 20  # 源序列长度
trg_seq_length = 10  # 目标序列长度
input_vocab_size = 10000  # 词汇表大小
output_vocab_size = 10000  # 词汇表大小