import requests, json


class DoubanMovieSpider(object):

    def __init__(self):
        self.url = 'https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=18&loc_id=108288'
        self.headers = {
            'Referer': 'https://m.douban.com/movie/nowintheater?loc_id=108288',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'
        }
    def get_content_from_url(self, url):
        # 发送请求获取响应数据
        response = requests.get(url, headers = self.headers)
        return response.content.decode()

    def get_data_from_content(self,content):
        """提取数据,json字符串"""
        dic = json.loads(content)
        return dic['subject_collection_items']

    def save_data(self, data_list):
        """保存数据"""
        with open('豆瓣不分页电影.jsonlines', 'a', encoding='utf8') as f:
            for data in data_list:
                json.dump(data,f,ensure_ascii=False)
                f.write('\n')
    def run(self):
        # 准备url
        url = self.url
        # 发送请求获取响应数据
        content = self.get_content_from_url(url)
        # 提取数据
        data_list = self.get_data_from_content(content)
        # 保存数据
        self.save_data(data_list)
if __name__ == '__main__':
    dbs = DoubanMovieSpider()
    dbs.run()


