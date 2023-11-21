import json
import re

# 读取JSON文件
with open('G:\\llm\\data\\AMO_chatting\\original.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 存储对话数据的变量
filtered_conversations = []

# 遍历JSON数据
for dialog in data:
    messages = []
    current_message = None  # To track consecutive messages of the same gender
    for message in dialog:
        # 1. 跳过包含特定词组的message
        if any(phrase in message['消息内容'] for phrase in ["button : Try it", "depth_gift_msg", "depth gift after msg", "send gift :"]):
            continue

        # 2. 将图片或者链接替换为短语
        message['消息内容'] = re.sub(r'http\S+', 'This is my photo.', message['消息内容'])

        # 3. 合并连续同一性别发送的不重复message
        if current_message and current_message['sender_gender'] == message['发送者性别']:
            if message['消息内容'] not in current_message['content']:
                current_message['content'] += f".{message['消息内容']}"
        else:
            if current_message:
                messages.append(current_message)

            current_message = {
                'sender_gender': message['发送者性别'],
                'content': message['消息内容'],
            }

    # 补上最后一条
    if current_message:
        messages.append(current_message)

    # 4. 删除message数量少于5条的dialog
    if len(messages) >= 10:
        filtered_conversations.append(messages)

# 保存结果到result.json文件
result_file_path = 'G:\\llm\\data\\AMO_chatting\\1_formated.json'
with open(result_file_path, 'w', encoding='utf-8') as result_file:
    json.dump(filtered_conversations, result_file, ensure_ascii=False, indent=2)

print(f"Filtered conversations saved to {result_file_path}")
