# 使用openai接口请求
from openai import OpenAI

api_key = 'sk-talrfpdubittuoctscpxqyuhotkkqgcmuxrxxlmmhkqpzlxd'
base_url = 'https://api.siliconflow.cn/v1'
client = OpenAI(api_key=api_key, base_url=base_url)

# # 发送请求到GPT模型, 流式输出
# response = client.chat.completions.create(
#     model='Qwen/Qwen2.5-7B-Instruct',  # 使用的模型，可以选择gpt-3.5-turbo等
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "你好"},
#     ],
#     max_tokens=150,  # 返回文本的最大长度
#     temperature=0.7,  # 控制生成文本的随机性，值越低，输出越确定
#     stream=True
# )

# # 逐块打印返回结果
# for chunk in response:
#     print(chunk)

# 发送请求到GPT模型, 非流式输出
response = client.chat.completions.create(
    model='Qwen/Qwen2.5-7B-Instruct',  # 使用的模型，可以选择gpt-3.5-turbo等
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你好"},
    ],
    max_tokens=150,  # 返回文本的最大长度
    temperature=0.7,  # 控制生成文本的随机性，值越低，输出越确定
    stream=False
)

print(response)