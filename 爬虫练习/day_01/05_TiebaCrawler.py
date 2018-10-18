import requests
"""
 1. 准备URL列表
 2. 发送请求, 获取响应数据
 3. 保存数据
 要求: 可以指定贴吧名称, 起始页与结束页
"""

class TiebaCrawler(object):
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
            url = self.url_pattern.format(self.name, (i-1)*50)
            url_list.append(url)
        return url_list

    def get_page_from_url(self, url):
        """根据URL,发送请求, 获取页面数据"""
        response = requests.get(url, headers=self.headers)
        # 返回页面数据
        return response.content.decode()

    def save_page(self, page, page_num):
        """保存数据"""
        file_namme = "{}第{}页.html".format(self.name, page_num)
        with open(file_namme, 'w', encoding='utf8') as f:
            f.write(page)

    def run(self):
        """程序入口, 主干逻辑"""
        #  1. 准备URL列表
        url_list = self.get_url_list()
        # 2.遍历URL列表,  发送请求, 获取响应数据
        for index,url in enumerate(url_list):
            page = self.get_page_from_url(url)
            # 3. 保存数据
            page_num = self.start + index
            self.save_page(page, page_num)

if __name__ == '__main__':
    name= input('请输入吧名')
    tie = TiebaCrawler(name, 1, 3)
    tie.run()

