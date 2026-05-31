"""终端交互预测入口。运行: python predict.py"""

import importlib.util
import os
from pathlib import Path

import pandas as pd
import torch

_path = Path(__file__).with_name('1.py')
_spec = importlib.util.spec_from_file_location('lstm_train', _path)
_lstm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_lstm)

device = _lstm.device
load_checkpoint = _lstm.load_checkpoint
predict_sentiment = _lstm.predict_sentiment


def format_label(label):
    if label == '正面':
        return '正面评价'
    if label == '负面':
        return '负面评价'
    return label


def read_comments_from_file(file_path):
    path = file_path.strip().strip('"').strip("'")
    if not os.path.exists(path):
        raise FileNotFoundError(f'文件不存在: {path}')

    df = pd.read_csv(path, encoding='utf-8-sig')
    for col in ('review', 'evaluation', 'comment', 'content', 'text', '评论'):
        if col in df.columns:
            texts = df[col].astype(str).tolist()
            break
    else:
        texts = df.iloc[:, 0].astype(str).tolist()

    return [
        t.strip().replace('\ufeff', '') for t in texts
        if t.strip().replace('\ufeff', '')
    ]


@torch.no_grad()
def batch_predict(model, processor, file_path):
    texts = read_comments_from_file(file_path)
    if not texts:
        print('文件中未找到有效评论。')
        return

    stats = {'正面': 0, '负面': 0}
    print(f'\n共读取 {len(texts)} 条评论，预测结果如下：\n')
    for i, text in enumerate(texts, 1):
        label, _ = predict_sentiment(model, processor, text)
        stats[label] = stats.get(label, 0) + 1
        preview = text if len(text) <= 40 else text[:40] + '...'
        print(f'第{i}条 -> {format_label(label)}')
        print(f'       内容: {preview}')

    print('\n--- 整体预测统计 ---')
    for label, count in stats.items():
        pct = count / len(texts) * 100
        print(f'{format_label(label)}: {count} 条 ({pct:.1f}%)')


def show_evaluation_summary(summary):
    print('\n' + '=' * 30)
    print('模型测试集评估结果')
    print('=' * 30)
    print(f"Accuracy : {summary['accuracy']}%")
    print(f"Precision: {summary['precision']}%")
    print(f"Recall   : {summary['recall']}%")
    print(f"F1-score : {summary['f1_score']}%")


def print_menu():
    print('\n' + '=' * 30)
    print('电商评论预测系统')
    print('=' * 30)
    print('1. 单句评论预测')
    print('2. 批量评论预测')
    print('3. 查看模型评估结果')
    print('4. 退出系统')


def main():
    try:
        print('正在加载模型...')
        model, processor, summary = load_checkpoint()
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return

    while True:
        print_menu()
        choice = input('请输入功能编号：').strip()

        if choice == '1':
            text = input('请输入评论内容：').strip()
            if not text:
                print('评论内容不能为空。')
                continue
            label, _ = predict_sentiment(model, processor, text)
            print(f'预测结果：{format_label(label)}')

        elif choice == '2':
            file_path = input('请输入批量预测文件路径：').strip()
            if not file_path:
                print('文件路径不能为空。')
                continue
            try:
                batch_predict(model, processor, file_path)
            except Exception as e:
                print(f'批量预测失败: {e}')

        elif choice == '3':
            if summary:
                show_evaluation_summary(summary)
            else:
                print('模型中未包含评估结果，请重新训练: python 1.py')

        elif choice == '4':
            print('感谢使用，系统已退出。')
            break

        else:
            print('无效编号，请输入 1-4。')


if __name__ == '__main__':
    main()
