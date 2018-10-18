import requests, json


class DoubanMovieSpidef(object):

    def __init__(self):
        self.url = 'https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start={}&count=18&loc_id=108288'
        self.headers = {
            'Referer': 'https://m.douban.com/movie/nowintheater?loc_id=108288',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'
        }

    def get_content_from_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_from_data(self, content):
        dic = json.loads(content)
        return dic['subject_collection_items']

    def save_data(self, data_list):
        with open('douban分页电影.jsonlines', 'a', encoding='utf8') as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')

    def run(self):
        # 定义变量,用于记录start
        start = 0
        while True:
            # 准备url
            url = self.url.format(start)
            # 发送请求,获取响应数据
            print(url)
            content = self.get_content_from_url(url)
            # 提取数据
            data_list = self.get_content_from_data(content)
            # 保存数据
            self.save_data(data_list)
            # 每获取一页,start递增18
            start += 18
            # 退出循环
            # 当获取到的数据不足18条
            if len(data_list)<18:
                break

if __name__ == '__main__':
    dbms = DoubanMovieSpidef()
    dbms.run()
