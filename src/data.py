import json

# 读取JSON文件
with open('G:\\llm\\data\\AMO_chatting\\original_test.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 存储对话数据的变量
conversations = []

# 遍历JSON数据
for dialog in data:
    messages = []
    for message in dialog:
        _message = {
            'content': message['消息内容'],
            'sender_gender': message['发送者性别'],
            'receiver_gender': message['接收者性别']
        }
        messages.append(_message)
    conversations.append(messages)

# 打印结果
print(conversations)
