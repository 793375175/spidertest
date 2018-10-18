"""
总体思路:
1. 提取一页的标题和url
2. 列表进行分页处理
3. 提取详情页中的图片url
http://tieba.baidu.com/m?kw={}&lp=5011&lm=&pn={}
http://tieba.baidu.com/m?kw={}&lp=5011&lm=&pn={}
"""
import requests, json
from lxml import etree


class TieBaSpider(object):

    def __init__(self, name):
        self.name = name
        # self.pn = pn
        self.url = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw={}&lp=5011&lm=&pn=20'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
        }

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
        print(a_s)
        data_list = []
        for a in a_s:
            data = {}
            data['title'] = a.xpath('./text()')[0]
            data['url'] = a.xpath('./@href')[0]
            data_list.append(data)

        return data_list

    def save_data(self, data_list):

        file_name = "{}.jsonlines".format(self.name)
        with open(file_name, 'a', encoding='utf8') as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')


    def run(self):
        url = self.url.format(self.name)
        page = self.get_page_from_url(url)
        data_list = self.get_page_from_data(page)
        self.save_data(data_list)


if __name__ == '__main__':
    tbs = TieBaSpider('赵丽颖')
    tbs.run()
