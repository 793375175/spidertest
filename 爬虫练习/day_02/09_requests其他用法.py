import requests


response = requests.get('http://www.baidu.com')
print(response.cookies)

#cookie_jar --> dict
dict1 = requests.utils.dict_from_cookiejar(response.cookies)
print(dict1)
print(type(dict1))

# dict-->cookie_jar
cookie_jar = requests.utils.cookiejar_from_dict(dict1)
print(cookie_jar)
print(type(cookie_jar))

response = requests.get("https://www.12306.cn/mormhweb/ ",verify=False)
print(response.content.decode())