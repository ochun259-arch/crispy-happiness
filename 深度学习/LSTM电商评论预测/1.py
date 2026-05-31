"""数据处理与模型训练。运行: python 1.py"""

import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='jieba')
warnings.filterwarnings('ignore', message='.*pkg_resources.*')

import copy
import os
import logging

import jieba

jieba.setLogLevel(logging.ERROR)

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import pandas as pd
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    precision_recall_fscore_support,
)
from collections import Counter

DATA_CSV = 'online_shopping_10_cats.csv'
MODEL_PATH = 'lstm_sentiment.pt'


def setup_seed(seed):
    torch.manual_seed(seed)
    np.random.seed(seed)


setup_seed(42)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class ReviewDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]


class LSTMModel(nn.Module):
    def __init__(self, vocab_size, embed_dim=128, hidden_dim=128, dropout=0.3):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(hidden_dim, 2)

    def forward(self, x):
        x = self.embedding(x)
        _, (hidden, _) = self.lstm(x)
        return self.fc(self.dropout(hidden[-1]))


class DataProcessor:
    def __init__(self, max_len=100, vocab_size=5000):
        self.max_len = max_len
        self.vocab_size = vocab_size
        self.word2idx = {'<PAD>': 0, '<UNK>': 1}
        self.idx2word = {0: '<PAD>', 1: '<UNK>'}
    # 数据分词
    def tokenize(self, text):
        if text is None or (isinstance(text, float) and np.isnan(text)):    # 处理数据空值和Nan值
            return []
        text = str(text).strip().replace('\ufeff', '')          # 数据转字符串并去除空格和特殊字符
        if not text or text.lower() == 'nan':
            return []
        return [w for w in jieba.cut(text) if w.strip()]                    # jieba分词并过滤空白词
    # 建立词表
    def build_vocab(self, texts):
        counter = Counter()
        for text in texts:
            counter.update(self.tokenize(text))                             # 统计词频

        for word, _ in counter.most_common(self.vocab_size - 2):            # 根据词频大小构建词表，预留2个特殊词位置
            if word not in self.word2idx:                                    # 对没有映射到的数据进行映射
                self.word2idx[word] = len(self.word2idx)
                self.idx2word[len(self.idx2word)] = word

        self.vocab_size = len(self.word2idx)
        print(f'词表大小: {self.vocab_size}')
    # 数据转换
    def text_to_ids(self, text):
        tokens = self.tokenize(text)
        ids = [self.word2idx.get(t, self.word2idx['<UNK>']) for t in tokens]  # 将分词后的词语列表转换成对应的数字ID列表，遇到未知词时用<UNK>的ID代替
        if len(ids) > self.max_len:
            ids = ids[:self.max_len]
        else:
            ids = ids + [0] * (self.max_len - len(ids))
        return ids
    # 数据读取
    def load_data(self, csv_path, text_col='review', label_col='label'):
        df = pd.read_csv(csv_path, encoding='utf-8-sig')
        df = df.dropna(subset=[text_col, label_col])          # 删除数据框中指定列包含空值（NaN）的行
        df[text_col] = (
            df[text_col].astype(str).str.strip()            # 转为字符串并删除首尾空白
            .str.replace('\ufeff', '', regex=False)         # 禁用正则表达式，将模式字符串当作普通文本进行精确匹配和替换
        )
        df = df[df[text_col].str.len() > 0]
        df = df[df[text_col].str.lower() != 'nan']

        if pd.api.types.is_numeric_dtype(df[label_col]):   # 将标签列统一转换为标准的二分类数值（0和1），
            df[label_col] = df[label_col].astype(int)
        else:
            df[label_col] = df[label_col].apply(
                lambda x: 1 if str(x) in ('1', '正面', 'positive') else 0
            )

        df = df[df[label_col].isin([0, 1])].reset_index(drop=True)    # 创建布尔掩码，标记标签为0或1的行，并过滤数据，只保留True的行，再重置索引为0,1,2...，丢弃原索引
        return df[text_col].values, df[label_col].values.astype(np.int64)   # 返回文本数组和标签数组
    # 数据准备
    def prepare_data(self, texts, labels):
        X = torch.tensor([self.text_to_ids(t) for t in texts], dtype=torch.long)
        y = torch.tensor(labels, dtype=torch.long)
        return X, y

# 模型训练
def train_model(model, train_loader, val_loader, epochs=10, lr=0.001):
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    best_acc = 0.0
    best_state = None

    for epoch in range(epochs):
        model.train()
        train_loss = 0.0
        train_preds, train_labels = [], []

        for X, y in train_loader:
            X, y = X.to(device), y.to(device)
            optimizer.zero_grad()
            outputs = model(X)
            loss = criterion(outputs, y)
            loss.backward()
            optimizer.step()

            train_loss += loss.item()
            train_preds.extend(outputs.argmax(dim=1).cpu().numpy())
            train_labels.extend(y.cpu().numpy())

        model.eval()
        val_preds, val_labels = [], []
        with torch.no_grad():
            for X, y in val_loader:
                X, y = X.to(device), y.to(device)
                outputs = model(X)
                val_preds.extend(outputs.argmax(dim=1).cpu().numpy())
                val_labels.extend(y.cpu().numpy())

        train_acc = accuracy_score(train_labels, train_preds)
        val_acc = accuracy_score(val_labels, val_preds)
        print(f'Epoch {epoch + 1}/{epochs} | 训练损失: {train_loss / len(train_loader):.4f} | '
              f'训练准确率: {train_acc:.4f} | 验证准确率: {val_acc:.4f}')

        if val_acc >= best_acc:
            best_acc = val_acc
            best_state = copy.deepcopy(model.state_dict())
            print(f'  -> 更新最佳模型 (val_acc={val_acc:.4f})')

    if best_state is not None:
        model.load_state_dict(best_state)
    return best_acc

# 计算准确率
def evaluate_model(model, test_loader, verbose=True):
    model.eval()
    preds, labels = [], []

    with torch.no_grad():
        for X, y in test_loader:
            X, y = X.to(device), y.to(device)
            outputs = model(X)
            preds.extend(outputs.argmax(dim=1).cpu().numpy())
            labels.extend(y.cpu().numpy())

    acc = accuracy_score(labels, preds)
    p, r, f1, _ = precision_recall_fscore_support(
        labels, preds, average='macro', zero_division=0)

    summary = {
        'accuracy': round(acc * 100, 2),
        'precision': round(p * 100, 2),
        'recall': round(r * 100, 2),
        'f1_score': round(f1 * 100, 2),
    }

    if verbose:
        print(f'\n测试准确率: {acc:.4f}')
        print('\n分类报告:')
        print(classification_report(labels, preds, target_names=['负面', '正面']))

    return summary

# 保存最佳模型
def save_checkpoint(model, processor, summary, path=MODEL_PATH):
    torch.save({
        'model_state_dict': model.state_dict(),
        'word2idx': processor.word2idx,
        'max_len': processor.max_len,
        'vocab_size': processor.vocab_size,
        'metrics_summary': summary,
    }, path)
    print(f'最佳模型已保存: {path}')


def load_checkpoint(path=MODEL_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(f'未找到模型文件 {path}，请先运行: python 1.py')

    ckpt = torch.load(path, map_location=device, weights_only=False)
    processor = DataProcessor(max_len=ckpt['max_len'], vocab_size=ckpt['vocab_size'])
    processor.word2idx = ckpt['word2idx']
    processor.idx2word = {i: w for w, i in processor.word2idx.items()}

    model = LSTMModel(vocab_size=processor.vocab_size).to(device)
    model.load_state_dict(ckpt['model_state_dict'])
    model.eval()
    return model, processor, ckpt.get('metrics_summary')


@torch.no_grad()
def predict_sentiment(model, processor, text):
    model.eval()
    X = torch.tensor([processor.text_to_ids(text)], dtype=torch.long).to(device)
    pred = model(X).argmax(dim=1).item()
    return ('正面' if pred == 1 else '负面'), None


def main():
    print('=' * 30)
    print('LSTM 电商评论预测 - 训练')
    print('=' * 30)

    print('\n1. 加载数据...')
    processor = DataProcessor(max_len=100, vocab_size=5000)
    texts, labels = processor.load_data(DATA_CSV)
    print(f'数据量: {len(texts)} 条')

    print('\n2. 划分数据集...')
    train_texts, temp_texts, train_labels, temp_labels = train_test_split(
        texts, labels, test_size=0.3, random_state=42, stratify=labels)
    val_texts, test_texts, val_labels, test_labels = train_test_split(
        temp_texts, temp_labels, test_size=0.5, random_state=42, stratify=temp_labels)
    print(f'训练集: {len(train_texts)}, 验证集: {len(val_texts)}, 测试集: {len(test_texts)}')

    print('\n3. 构建词表...')
    processor.build_vocab(train_texts)

    print('\n4. 准备数据...')
    X_train, y_train = processor.prepare_data(train_texts, train_labels)
    X_val, y_val = processor.prepare_data(val_texts, val_labels)
    X_test, y_test = processor.prepare_data(test_texts, test_labels)

    batch_size = 64
    train_loader = DataLoader(ReviewDataset(X_train, y_train), batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(ReviewDataset(X_val, y_val), batch_size=batch_size)
    test_loader = DataLoader(ReviewDataset(X_test, y_test), batch_size=batch_size)

    print('\n5. 创建并训练模型...')
    model = LSTMModel(vocab_size=processor.vocab_size).to(device)
    print(f'模型参数量: {sum(p.numel() for p in model.parameters()):,}')
    train_model(model, train_loader, val_loader, epochs=10)

    print('\n6. 测试集评估...')
    summary = evaluate_model(model, test_loader)
    save_checkpoint(model, processor, summary)

    print('\n训练完成。启动终端交互请运行: python predict.py')


if __name__ == '__main__':
    main()
