import json

# 读取JSON文件
with open('tests\\test_convs.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 存储对话数据的变量
conversations = {}

# 遍历JSON数据
for user_id, dialogs in data.items():
    user_conversations = []
    for dialog in dialogs:
        messages = []
        for message in dialog:
            messages.append({
                'sender': message['发送者'],
                'receiver': message['接收者'],
                'timestamp': message['发送时间'],
                'content': message['消息内容'],
                'sender_id': message['发送者ID'],
                'receiver_id': message['接收者ID']
            })
        user_conversations.append(messages)
    conversations[user_id] = user_conversations

# 打印结果
print(conversations)
