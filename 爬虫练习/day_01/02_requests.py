import requests

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
response = requests.get('http://www.baidu.com', headers = headers)

print(response.status_code)
# print(response.headers)
print(response.request.headers)
# print(response.content.decode())