import requests
import random


headers = {
          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
      }
proxies_list = [
    {'http': '121.8.98.198:80'},
    {'http':'121.201.33.99:808'},
    {'http':'115.46.70.190:8123'},
    {'http':'119.127.18.146:9797'}
]
bu_list = []
for i in range(4):
    try:
        proxies = random.choice(proxies_list)
        response = requests.get('http://httpbin.org/get', proxies=proxies,headers=headers,timeout=2)
        print(response.status_code)
        print(response.content.decode())
        print('{}_可用的'.format(proxies))
    except Exception as e:
        print('{}_不可用的'.format(proxies))
        bu_list.append(proxies)
        print(bu_list)
