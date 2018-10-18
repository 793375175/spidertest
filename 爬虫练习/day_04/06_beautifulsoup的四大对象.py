from bs4 import BeautifulSoup
# 准备html字符串数据
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
bs = BeautifulSoup(html, 'lxml')
# print(bs)
# print(type(bs))
# 获取一个p标签
# tag就是一个标签对象
p = bs.find('p')
# print(p)
# print(type(p)) # 'bs4.element.Tag'

# 获取标签的属性
b = bs.find('a').get('id')
# print(b)
# 获取文本
# print(dir(p))
# print(p.text)
# print(type(p.text))  # str'

# print(p.string)
# print(type(p.string))  #bs4.element.NavigableString
# print(dir(p.string))

# 获取父标签
f = p.string.find_parent()
# print(f)

# 获取下一个标签
n = p.string.find_next()
# print(n)

a = bs.find('a')
print(a.string)
print(type(a.string))