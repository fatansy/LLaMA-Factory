import json

from websockets.sync.client import connect

headers = {
    "Authorization": "ZTM4YjFiMGVjMmExOTY1OTg1NzcwNjY3YzY1YmU0NjliMjgwOTg5Zg=="
}
url = "ws://1918537650540564.cn-hangzhou.pai-eas.aliyuncs.com/api/predict/test_v2/generate_stream"
with connect(url, additional_headers=headers) as websocket:
    prompt = "hi"
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