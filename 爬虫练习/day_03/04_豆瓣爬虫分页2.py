import requests, json


class DoubanMovieSpider(object):

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

        # 生成下一页的url
        # 当前页的start
        start = dic['start']
        # 当前页的请求数据条数
        count = dic['count']
        # 总数据条数
        total = dic['total']
        # 计算下一页start
        next_start = start + count
        # 判断有没有下一页
        if next_start < total:
            next_url = self.url.format(next_start)
        else:
            next_url = None
        return dic['subject_collection_items'], next_url

    def save_data(self, data_list):
        with open('豆瓣电影分页2.jsonlines', 'a', encoding='utf8') as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')

    def run(self):

        url = self.url.format(0)
        while url:
            content = self.get_content_from_url(url)
            data_list, url = self.get_content_from_data(content)
            self.save_data(data_list)


if __name__ == '__main__':
    dbms = DoubanMovieSpider()
    dbms.run()
