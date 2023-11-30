from eas_prediction import PredictClient
from eas_prediction import StringRequest

if __name__ == '__main__':
    client = PredictClient('http://1975992961854380.cn-hangzhou.pai-eas.aliyuncs.com/api/predict/nvwang_test', 'nvwang_test')
    client.set_token('MjE5MzI1MjdjZTM1NTBmODc2OThkNDk1MmZmOWZhYTQ3MTU1NWUwNA==')
    client.init()

    request = StringRequest('USER: {{hi}} ASSISTANT:')
    for x in range(0, 1000000):
        resp = client.predict(request)
        print(resp)
