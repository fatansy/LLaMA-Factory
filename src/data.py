import json
import re

def save_to_file(file_name, data):
    result_file_path = 'G:\\llm\\data\\AMO_chatting\\' + file_name
    with open(result_file_path, 'w', encoding='utf-8') as result_file:
        json.dump(data, result_file, ensure_ascii=False, indent=4)

    print(file_name + f" saved to {result_file_path}")


def main():
    # 读取JSON文件
    with open('G:\\llm\\data\\AMO_chatting\\original.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 存储对话数据的变量
    filtered_conversations = []
    multi_turn_conversations = []

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

        # 4. 删除message数量少于8条的dialog
        if len(messages) >= 10:
            # 5. 如果第一句是女性发的，去掉它
            # 如果最后一句是男性发的，去掉它
            if messages[0]['sender_gender'] == 'WOMAN':
                messages.pop(0)
            if messages[-1]['sender_gender'] == 'MAN':
                messages.pop()
            filtered_conversations.append(messages)

            # 6. 转换为多轮对话数据格式
            multi_turn_dialog = []
            history = []
            for i in range(1, len(messages), 2):
                instruction = messages[i - 1]['content']
                output = messages[i]['content']
                if i>= 3:
                    history.append([messages[i - 3]['content'], messages[i - 2]['content']])

                multi_turn_dialog.append({
                    "instruction": instruction,
                    "input": "",
                    "output": output,
                    "history": history.copy()
                })

            multi_turn_conversations.extend(multi_turn_dialog)

    # 保存中间结果到1_format.json文件
    save_to_file('1_format.json', filtered_conversations)
    # 保存最终结果到2_final.json文件
    save_to_file('2_final.json', multi_turn_conversations)


if __name__ == "__main__":
    main()
