import requests

data = {
    "name": 'laowang'
}
response = requests.post('http://httpbin.org/post', data=data)

print(response.content.decode())