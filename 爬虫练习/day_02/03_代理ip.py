import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'
}
url = 'http://www.66ip.cn/areaindex_2/3.html'
response = requests.get(url, headers=headers).text
print(type(response))

with open('代理ip.html','w',encoding='utf8') as f:
    f.write(response)