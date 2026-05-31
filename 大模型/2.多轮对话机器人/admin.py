from openai import OpenAI

# 初始化客户端
api_key = "EMPTY"
base_url = "http://127.0.0.1:10222/v1"
client = OpenAI(api_key=api_key, base_url=base_url)

messages = [
    {"role": "system", "content": "你是一个有用的助手。"}
]


def chat_with_bot(user_input):
    # 将用户的输入放在消息列表中
    messages.append({"role": "user", "content": user_input})
    # 保留system  保留最近的6轮对话
    send_messages = [messages[0]] + messages[-6:]

    # 将消息发给qwen
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=send_messages,
        max_tokens=4096,
        temperature=0.5,
        top_p=0.5
    )

    # 获取大模型的输出
    assistant_response = response.choices[0].message.content
    print(f"assistant: {assistant_response}")

    # 需要将助手的返回结果放在我们的消息列表中
    messages.append({"role": "assistant", "content": assistant_response})


while True:
    user_input = input("你:\n")
    if user_input.lower() in ["quit", "exit"]:
        print("对话结束。")
        break
    chat_with_bot(user_input)