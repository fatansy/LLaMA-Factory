import json

from websockets.sync.client import connect

headers = {
    "Authorization": "Y2NhMTE0YjkwNGI2ZjUzOWY4MWY5OTA0YzI4ZGFiNWUyZTllOWE1OA=="
}
url = "ws://1918537650540564.cn-hangzhou.pai-eas.aliyuncs.com/api/predict/test_v4/generate_stream"
with connect(url, additional_headers=headers) as websocket:
    prompt = "USER: can you send me photo? ASSISTANT:wait a minute. USER: Come on! ASSISTANT:"
    websocket.send(
        json.dumps(
            {
                "prompt": prompt,
                "sampling_params": {
                    "temperature": 0.9,
                    "top_p": 0.9,
                    "top_k": 50
                },
                "stopping_criterial": {
                    "max_new_tokens": 100
                },
            }
        )
    )
    while True:
        msg = websocket.recv()
        msg = json.loads(msg)
        if msg['is_ok']:
            print(msg['tokens'][0]["text"], end="", flush=True)
            if msg['is_finished']:
                break
    print()
    print("-" * 40)