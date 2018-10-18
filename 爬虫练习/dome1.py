import requests
from pyquery import PyQuery as pq
import io

url = "https://www.zhihu.com/explore"

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
}

html = requests.get(url, headers=headers).text

doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()

    with io.open('explore.txt', 'a', encoding='utf8')as file:
        file.write('\n'.join([question, author, answer]))
        # file.write('\n' + '=' * 50 + '\n')