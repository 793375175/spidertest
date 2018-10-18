# 1. 导入requests模块
import requests

# # 2. 发送请求获取二进制数据(bytes)
# respone = requests.get(
#     "http://imgsrc.baidu.com/image/c0%3Dpixel_huitu%2C0%2C0%2C294%2C40/sign=098c3f828cd6277ffd1f3a7841407a5c/3c6d55fbb2fb4316e3afd1432ba4462309f7d353.jpg")
# # 获取二进制数据; 注意: 这里不要解码, 因为图片,视频等文件都是二进制的不是文本,不需要解码
# # data = respone.content
# # 3. 把数据写入文件
# with open("壁纸.jpg", "wb") as f:
#     f.write(respone.content)
# response = requests.get('http://image.xcar.com.cn/attachments/a/day_140126/2014012615_c67ba76fac797a858991m9i29zYXYwM9_sst_560.jpg')
# with open("imag.jpg", "wb") as f:
#     f.write(response.content)
response = requests.get('https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1662514716,781951703&fm=27&gp=0.jpg')

with open('daniu.jpg', 'wb')as f:
    f.write(response.content)