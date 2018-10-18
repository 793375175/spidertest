import requests
import sys
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'
}
# 1.检查当前要翻译语言类型
# 1.1准备检查语言类型的url
detect_url = 'http://fanyi.baidu.com/langdetect'
# 1.2准备相关数据
cnt = input('请输入要翻译的内容:')
# print(sys.argv)
# cnt = sys.argv
data = {
    'query': cnt
}
# 1.3发送请求获取响应数据
response = requests.post(detect_url,data=data,headers=headers)
json_str = response.content.decode()
dict = json.loads(json_str)
lan = dict['lan']
# 2.翻译
# 2.1准备翻译的url
trans_url = 'http://fanyi.baidu.com/basetrans'
# 2.2准备翻译的数据
to = ['en' if lan=='zh' else 'zh']
trans_data = {
    'query': cnt,
    'from': lan,
    'to': to
}
# 2.3发送翻译请求,获取响应数据
trans_response = requests.post(trans_url, data=trans_data,headers=headers)
# 2.4 解析响应数据,提取翻译结果
rsult = json.loads(trans_response.content.decode())
print(rsult['trans'][0]['dst'])