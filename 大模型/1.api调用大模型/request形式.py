# 使用request请求
import requests
import json

# 设置请求的URL
url = "https://api.siliconflow.cn/v1/chat/completions"

# 设置请求头，包括授权信息
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-talrfpdubittuoctscpxqyuhotkkqgcmuxrxxlmmhkqpzlxd"
}

# # 定义请求的数据体，开启非流式响应
# data = {
#     "model": "Qwen/Qwen2.5-7B-Instruct",
#     "messages": [
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "你好"}
#     ],
#     "max_tokens": 150,
#     "stream": False
# }

# # 发送POST请求
# response = requests.post(url, headers=headers, data=json.dumps(data))

# print(response.text)

# 定义请求的数据体，开启流式响应
data = {
    "model": "Qwen/Qwen2.5-7B-Instruct",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你好"}
    ],
    "max_tokens": 150,
    "stream": True
}

# 发送POST请求，开启流式响应
response = requests.post(url, headers=headers, data=json.dumps(data))

# 检查响应状态
if response.status_code == 200:
    # 实时接收和打印每个流块
    for chunk in response.iter_content(chunk_size=None):
        print(chunk.decode('utf-8'))