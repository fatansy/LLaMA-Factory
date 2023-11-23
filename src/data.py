import json
import re

data_src_path = 'data/amo/'
# data_src_path = 'G:\\llm\\data\\AMO_chatting\\'

def split_file(input_list, max_size = 15000):
    return [input_list[i:i + max_size] for i in range(0, len(input_list), max_size)]


def read_from_file(file_name):
    with open(data_src_path + file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_to_file(file_name, data):
    result_file_path = data_src_path + file_name
    with open(result_file_path, 'w', encoding='utf-8') as result_file:
        json.dump(data, result_file, ensure_ascii=False, indent=4)

    print(file_name + f" saved to {result_file_path}")


def first_step(data_version):
    # 读取JSON文件
    data = read_from_file(f'original_{data_version}.json')

    # 存储对话数据的变量
    filtered_conversations = []

    # 遍历JSON数据
    for dialog in data:
        messages = []
        current_message = None  # To track consecutive messages of the same gender
        for message in dialog:
            # 截断超过40句
            if len(messages) >= 40:
                break

            # 跳过包含特定词组的message
            if any(phrase in message['消息内容'] for phrase in ["button : Try it", "depth_gift_msg", "depth gift after msg", "send gift :", "Duration:", "Duur:", "Call not answered", "Call wasn't answered", "You've refused the call", "Refuse your call"]):
                continue

            # 将图片或者链接替换为短语
            message['消息内容'] = re.sub(r'http\S+', '[photo]', message['消息内容'])

            # 合并连续同一性别发送的不重复message
            if current_message and current_message['sender_gender'] == message['发送者性别']:
                if message['消息内容'] not in current_message['content']:
                    if current_message['content'].endswith('.') or current_message['content'].endswith('?'):
                        current_message['content'] += message['消息内容']
                    else:
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

        # 删除message数量少于8条的dialog
        if len(messages) >= 10:
            # 如果第一句是女性发的，去掉它
            # 如果最后一句是男性发的，去掉它
            if messages[0]['sender_gender'] == 'WOMAN':
                messages.pop(0)
            if messages[-1]['sender_gender'] == 'MAN':
                messages.pop()
            filtered_conversations.append(messages)

    print(f'filtered_conversations: {len(filtered_conversations)}')
    # 保存中间结果到format.json文件
    save_to_file(f'formated_{data_version}.json', filtered_conversations)


def second_step(data_version):

    data = read_from_file(f'formated_{data_version}.json')
    
    multi_turn_conversations = []
    # 转换为多轮对话数据格式
    for messages in data:
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

    print(f'multi_turn_conversations: {len(multi_turn_conversations)}')
    save_to_file(f'final_{data_version}.json', multi_turn_conversations)
    # 保存最终结果到2_final.json文件
    multi_turn_conversations_splited = split_file(multi_turn_conversations)
    i = 1
    for _convs in multi_turn_conversations_splited:
        save_to_file(f'final_{data_version}_{i}.json', _convs)
        i += 1


if __name__ == "__main__":

    data_version = 'v3'

    # 第一步，初步清理和格式化数据
    # first_step(data_version)
    # 第二步，人工审查数据后，将数据保存为最终训练所需要的格式
    second_step(data_version)
