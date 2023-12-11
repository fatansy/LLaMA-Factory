import json

from websockets.sync.client import connect

headers = {
    "Authorization": "Y2NhMTE0YjkwNGI2ZjUzOWY4MWY5OTA0YzI4ZGFiNWUyZTllOWE1OA=="
}
url = "ws://1918537650540564.cn-hangzhou.pai-eas.aliyuncs.com/api/predict/test_v4/generate_stream"
with connect(url, additional_headers=headers) as websocket:
    prompt = "USER:hi ASSISTANT:how are you USER: not bad , what about you ASSISTANT:im good.what are you looking here USER:a girl friend , can you be my girl ASSISTANT:"
    websocket.send(
        json.dumps(
            {
                "prompt": prompt,
                "sampling_params": {
                    "temperature": 0.95,
                    "top_p": 0.7
                },
                "stopping_criterial": {
                    "max_new_tokens": 512
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