import requests, json
from jsonpath import jsonpath


url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'
}

response = requests.get(url, headers=headers)
json_str = response.content.decode()
data = json.loads(json_str)

json_name = jsonpath(data,'$..name')
print(json_name)