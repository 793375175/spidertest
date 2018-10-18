"""
1.url规律明显,并且只有13页,页数固定
此时就可以生成一个url列表
https://www.qiushibaike.com/8hr/page/1/
"""
import requests, re, json
from lxml import etree


class QiubaiSpider(object):

    def __init__(self):
        self.url_pattern = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }

    def get_url_list(self):
        """生成url列表"""
        # url_list = []
        # for i in range(1, 14):
        #     url = self.url_pattern.format(i)
        #     url_list.append(url)
        # return url_list  或者
        return [self.url_pattern.format(i) for i in range(1, 14)]

    def get_page_from_url(self, url):
        """发送请求 获取页面数据"""
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            return self.get_page_from_url(url)
        return response.content.decode()

    def get_date_from_page(self, page):
        """从页面中提取需要的数据"""
        element = etree.HTML(page)
        divs = element.xpath('//*[@id="content-left"]/div')
        # 使用xpath提取数据的原则: 先分组,再提取内容
        data_list = []
        for div in divs:
            # 定义字典保存数据
            data = {}
            imgs = div.xpath('./div[1]/a[1]/img/@src')
            data['header_img'] = 'https' + imgs[0] if len(imgs) != 0 else None

            data['name'] = self.get_first_element(div.xpath('./div[1]/a[2]/h2/text()'))
            gender_class = div.xpath('./div[1]/div/@class')
            if len(gender_class) != 0:
                data['gender'] = re.findall('articleGender (.+?)Icon', gender_class[0])[0]

            data['content'] = ''.join([ text.strip() for text in div.xpath('./a/div/span//text()')])
            data['vote'] = self.get_first_element(div.xpath('./div[2]/span[1]/i/text()'))
            data['comments'] = self.get_first_element(div.xpath('./div[2]/span[2]/a/i/text()'))

            data_list.append(data)
        return data_list

    def get_first_element(self, lis):
        return lis[0].strip() if len(lis) != 0 else None

    def save_data(self, data_list):
        """保存数据"""
        with open('糗百.jsonlines', 'a', encoding='utf8') as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')

    def run(self):
        # 1.生成url列表
        url_list = self.get_url_list()
        # 2.遍历url列表
        for url in url_list:
            page = self.get_page_from_url(url)
            # 3.提取数据
            data_list = self.get_date_from_page(page)
            # 4.保存数据
            self.save_data(data_list)


        #
if __name__ == '__main__':
    qbs = QiubaiSpider()
    qbs.run()