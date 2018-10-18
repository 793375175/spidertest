from lxml import etree


html = '''
<div> <ul> 
<li class="item-1"><a href="link1.html">first item</a></li> 
<li class="item-1"><a href="link2.html">second item</a></li> 
<li class="item-inactive"><a href="link3.html">third item</a></li> 
<li class="item-1"><a href="link4.html">fourth item</a></li> 
<li class="item-0"><a href="link5.html">fifth item</a>  
</ul> </div>
'''
# 把文档转化为一个Element对象
element = etree.HTML(html)

# 找出 class="item-1"的li标签下面的a标签列表(先分组)
a_s = element.xpath('//li[@class="item-1"]/a')

# 遍历a标签列表
for a in a_s:
    data = {}
    data['title'] = a.xpath('./text()')[0] if len(a.xpath('./text()')) != 0 else None
    data['href'] = a.xpath('./@href')[0] if len(a.xpath('./@href'))!= 0 else None
    print(data)