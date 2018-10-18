"""
1.url规律明显,并且只有13页,页数固定
此时就可以生成一个url列表
https://www.qiushibaike.com/8hr/page/1/

修改为多线程版
1.创建url队列,响应队列和数据队列(init)
2.生成url.添加到url队列中
3.从url队列中,取出url,发送请求,获取响应数据,把响应数据,放到响应队列中
4.从响应队列中取出响应数据,提取数据,把数据放到数据队列中
5.从数据队列中取出数据,进行保存

把多线程版改为线程池版
1.在init方法中,创建线程池对象
2.执行任务地方,使用线程的异步任务
3.run方法,队列的json()方法,上面等待下

把线程池版修改为协程池版
1.把导入线程池改为导入协程池
2.打猴子补丁
3.去掉创建pool指定的个数
"""
# 要尽可能早点打猴子补丁
from gevent import monkey
monkey.patch_all()
import requests, re, json
from lxml import etree
from queue import Queue
# from threading import Thread
# from multiprocessing.dummy import Pool
from gevent.pool import Pool
import time


class QiubaiSpider(object):

    def __init__(self):
        self.url_pattern = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }
        # 1. 创建URL队列, 响应队列和数据队列(init)
        self.url_queue = Queue()
        self.page_queue = Queue()
        self.data_queue = Queue()
        self.pool = Pool()

    def add_url_to_queue(self):
        """把url添加到队列里"""
        for i in range(1, 14):
            url = self.url_pattern.format(i)
            self.url_queue.put_nowait(url)

    def add_page_to_queue(self):
        """从url队列中,取出url,发送请求,获取响应数据,把响应数据,放到响应队列中"""
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                # 如果请求没有成功, 再次放到URL队列
                self.url_queue.put(url)
            else:
                # 把响应数据添加响应队列中
                self.page_queue.put(response.content.decode())
            # 当URL处理完成了,就调用task_done
            self.url_queue.task_done()

    def add_date_to_queue(self):
        """从响应队列中取出响应数据,提取数据,把数据放到数据队列中"""
        while True:
            page = self.page_queue.get()
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
            # 把数据数据,添加数据队列中
            self.data_queue.put(data_list)
            # 页面任务处理完毕了
            self.page_queue.task_done()

    def get_first_element(self, lis):
        return lis[0].strip() if len(lis) != 0 else None

    def save_data(self):
        """保存数据"""
        while True:
            data_list = self.data_queue.get()
            with open('糗百_协程池版.jsonlines', 'a', encoding='utf8') as f:
                for data in data_list:
                    json.dump(data, f, ensure_ascii=False)
                    f.write('\n')
            # 数据任务完成了
            self.data_queue.task_done()

    def execute_task(self, task, count):
        """
        执行线程任务
        :param task: 任务函数
        :param count: 启动线程个数
        """
        for i in range(count):
            self.pool.apply_async(task)

    def run(self):

        self.add_url_to_queue()
        self.execute_task(self.add_page_to_queue, 2)
        self.execute_task(self.add_date_to_queue,1)
        self.execute_task(self.save_data, 2)

        # 让主线等待任务队列的完成
        self.url_queue.join()
        self.page_queue.join()
        self.data_queue.join()

if __name__ == '__main__':
    qbs = QiubaiSpider()
    qbs.run()