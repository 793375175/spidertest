import requests, json, re
from jsonpath import jsonpath


class KrSpider(object):

    def __init__(self):
        self.url = 'https://36kr.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'
        }
    def get_content_from_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_from_data(self,content):
        """从页面中提取数据(重点)"""
        # 1. 通过正则取json字符串数据
        json_str = re.findall(r'<script>var props=(.+?),locationnal=.+?</script> ', content, re.S)[0]
        # 为了调试, 就需要把这个字符串写入文件中
        with open('36kr.txt', 'w', encoding='utf8')as f:
            f.write(json_str)
        data = json.loads(json_str)
        # print(data)
        return data

    def save_data(self, data):
        """保存数据"""
        with open('36kr.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.write('\n')

    def run(self):
        url = self.url
        content = self.get_content_from_url(url)
        data = self.get_content_from_data(content)
        self.save_data(data)

if __name__ == '__main__':
    ks = KrSpider()
    ks.run()

