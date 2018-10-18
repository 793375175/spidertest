"""
总体思路:
1. 提取一页的标题和url
2. 列表进行分页处理
3. 提取详情页中的图片url

1. 提取一页标题和URL的数据
1.1. 准备URL
1.2. 发送请求, 获取响应数据
1.3. 提取数据, 标题和URL,
1.4. 保存数据

2.列表进行分页处理
2.1 获取下一页a标签href属性
2.2 如果a标签列表不为0,就说明有下一页,否则就说明没有下一页
"""
import requests, json
from lxml import etree


class TieBaSpider(object):

    def __init__(self, name):
        self.name = name
        # self.pn = pn
        self.url = 'http://tieba.baidu.com/mo/q---8DF4A6278C21C5F331E3F89A7D56AE96:FG=1-sz@320_240,-1-3-0--2--wapp_1534557617920_512/m?kw={}&lp=5011&lm=&pn=0'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
        }
        self.pre_url = 'http://tieba.baidu.com/mo/q---8DF4A6278C21C5F331E3F89A7D56AE96:FG=1-sz@320_240,-1-3-0--2--wapp_1534557617920_512/'

    def get_page_from_url(self, url):
        response = requests.get(url, headers=self.headers)
        # ValueError: Unicode strings with encoding declaration are not supported. Please use bytes input or XML fragments without declaration.
        # 由于在 文档中有 <?xml version="1.0" encoding="UTF-8"?> 声明, 那么HTML放中就只能传入字节数据, 不能传入编码后的字符串
        # return response.content.decode()
        return response.content

    def get_page_from_data(self, page):
        """提取数据,标题跟url"""
        element = etree.HTML(page)
        a_s = element.xpath('//div[contains(@class, "i")]/a')

        data_list = []
        for a in a_s:
            data = {}
            data['title'] = a.xpath('./text()')[0]
            data['url'] = self.pre_url + a.xpath('./@href')[0]
            data['imgs'] = self.get_imgs_detail_url(data['url'])
            data_list.append(data)

        # 获取下一页a标签href属性
        next_url = element.xpath('.//a[text()="下一页"]/@href')
        if len(next_url) != 0:
            next_url = self.pre_url + next_url[0]
        else:
            next_url = None

        return data_list, next_url

    def save_data(self, data_list):

        file_name = "{}_列表分页_图片.jsonlines".format(self.name)
        with open(file_name, 'a', encoding='utf8') as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')

    def get_imgs_detail_url(self, detail_url):
        """从详情页中提取所有图片数据"""
        imgs_list = []
        while True:
            # 1. 发送请求, 从详情页的URL中, 获取响应数据
            detail_page = self.get_page_from_url(detail_url)
            # 2. 解析数据, 把page转为为element对象
            element = etree.HTML(detail_page)
            # 3. 从element中提取所有图片的URL
            imgs = element.xpath('.//img[@class="BDE_Image"]/@src')
            # 遍历解析切割
            imgs = [requests.utils.unquote(img).split('&src=')[1] for img in imgs]
            # 这里不能使用append
            # imgs_list.extend(imgs)  或者
            imgs_list += imgs
            # print(imgs)
            detail_url = element.xpath('.//a[text()="下一页"]/@href')
            if len(detail_url) != 0:
                detail_url = self.pre_url + detail_url[0]
            else:
                break
        return imgs_list

    def run(self):
        url = self.url.format(self.name)

        while url:
            print(url)
            page = self.get_page_from_url(url)
            data_list, url = self.get_page_from_data(page)
            self.save_data(data_list)


if __name__ == '__main__':
    tbs = TieBaSpider('做头发')
    tbs.run()
