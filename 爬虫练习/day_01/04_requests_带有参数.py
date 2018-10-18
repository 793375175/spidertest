import requests

# 方式一: 拼接
name = input('请输入搜索的关键字')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
# response = requests.get('http://www.baidu.com/s?wd=' + name, headers=headers)

# print(response.content.decode())

# url = 'http://www.baidu.com/s?wd={}'
#
# url= url.format(name)
# response = requests.get(url,headers=headers)
# print(response.content.decode())

# 方式二: params

url = 'https://www.baidu.com/s'
params = {
    'wd':name
}
response = requests.get(url, params=params, headers=headers)
print(response.content.decode())