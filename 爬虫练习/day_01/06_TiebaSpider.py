import requests


class TiebaSpider(object):
    """贴吧"""

    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        # 准备url模板
        self.url_pattern = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
        # 准备请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }
    def get_url_list(self):
        url_list = []
        for i in range(self.start, self.end+1):
            url = self.url_pattern.format(self.name,(i-1)*50)
            url_list.append(url)
        return url_list


    def get_page_from_url(self,url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_list(self, page, page_num):
        file_name = "{}第{}页.html".format(self.name, page_num)
        with open(file_name, 'w', encoding='utf8') as f:
            f.write(page)
    def run(self):
        """程序入口"""
        url_list = self.get_url_list()
        for index,url in enumerate(url_list):
            page = self.get_page_from_url(url)
            page_num = self.start + index
            self.save_list(page, page_num)


if __name__ == '__main__':
    tbs = TiebaSpider('赵丽颖', 1, 3)
    tbs.run()
