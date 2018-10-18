"""
思路:
1.获取到一个session对象,使用requests中方法完全一样;该session会自动记录
服务器发送的cookie信息,下次请求的时候会自动携带,服务器设置过来的cookie信息
2.发送登录请求,服务器就会向session对象设置cookie信息
3.在使用这个session发送请求,获取数据的时候,会自动携带cookie信息
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'
}
session = requests.session()
login_url = 'http://www.renren.com/PLogin.do'
data = {
    'email':'15768608151',
    'password':'abc123'
}
response = session.post(login_url,data=data,headers=headers)
print(response.content.decode())