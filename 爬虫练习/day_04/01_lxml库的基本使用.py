from lxml import etree


body = '''
<div> <ul> 
<li class="item-1"><a href="link1.html">first item</a></li> 
<li class="item-1"><a href="link2.html">second item</a></li> 
<li class="item-inactive"><a href="link3.html">third item</a></li> 
<li class="item-1"><a href="link4.html">fourth item</a></li> 
<li class="item-0"><a href="link5.html">fifth item</a>  
</ul> </div>
'''
# 把文档转化为一个Element对象
html = etree.HTML(body)
# 获取class为item-1的li下面的a标签的文本
text_list = html.xpath('//li[@class="item-1"]/a/text()')

# 获取class为item-1的li下面的a标签的href属性
hrefs = html.xpath('//li[@class="item-1"]/a/@href')
print(text_list)
print(hrefs)
# print(etree.tostring(html).decode())

# 整合数据; 标题和href属性进行一对一整合
for text in text_list:
    data = {}
    data['title'] = text
    data['href'] = hrefs[text_list.index(text)]
    print(data)
