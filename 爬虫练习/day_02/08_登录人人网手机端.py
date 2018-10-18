import requests, json, js2py

# 获取rkeyurl相关数据
# 1.1准备rkey_url
rkey_url = 'http://activity.renren.com/livecell/rKey'
# 1.2准备请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36',
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/x-www-form-urlencoded",
}
# 1.3发送请求,获取rkey数据,
response = requests.get(rkey_url, headers=headers)
# 1.4解析数据,获取data数据
data = json.loads(response.content.decode())['data']
print(data)
print(type(data))

# 2生成password
"""
t.password = t.password.split("").reverse().join(""),
setMaxDigits(130);
var o = new RSAKeyPair(n.e,"",n.n)
, r = encryptedString(o, t.password);
"""


# 2.1加载依赖的js文件
def load_js_from_url(url):
    response = requests.get(url, headers=headers)
    return response.content.decode()


# 2.2获取js的执行环境
context = js2py.EvalJs()
# 2.3使用js的执行环境,去加载需要的js文件
context.execute(load_js_from_url('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js'))
context.execute(load_js_from_url('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js'))
context.execute(load_js_from_url('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js'))
context.execute(load_js_from_url('http://s.xnimg.cn/a86836/wap/mobile/wechatLive/js/celllog.js'))

# 2.4设置执行js需要的数据
context.t = {
    'password': 'abc123',
}
context.n = data
# 2.5准备要执行的代码
js_code = '''
t.password = t.password.split("").reverse().join(""),
setMaxDigits(130);
var o = new RSAKeyPair(n.e,"",n.n)
, r = encryptedString(o, t.password);
'''
# 2.6执行js获取加密
context.execute(js_code)
# 2.7 获取加密后的密码
print(context.r)

# 3.1登录的url
login_url = 'http://activity.renren.com/livecell/ajax/clog'

# 3.2准备数据
data = {
    'phoneNum': '15768608151',
    'password': context.r,
    'c1': -100,
    'rKey': data['rkey']
}
# 3.3 发送登录请求
response = requests.post(login_url, data=data, headers=headers)
print(response.content.decode())
