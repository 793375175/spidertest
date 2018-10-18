"""
需求: 爬虫58租房上列表上标题,URL,价格信息. 并且要实现翻页
思路:
定义类来封装58租房的代码
准备URL,创建driver对象,并加载页面
通过driver对象解析页面数据
保存数据
实现翻页效果
退出driver
"""
from selenium import webdriver
import time, json
from selenium.webdriver.chrome.options import Options


class ZufangSpider(object):
    def __init__(self):
        options = Options()
        options.set_headless()
        self.url = 'http://sz.58.com/chuzu/'
        self.driver = webdriver.Chrome(options=options)

    def get_data_list(self):
        """获取数据，返回数据列表"""
        # 先分组： 获取包含租房信息的li标签列表
        # 最后两个li标签一个分页，一个广告，不要
        lis = self.driver.find_elements_by_xpath('//ul[@class="listUl"]/li')[:-2]

        # 遍历。提取数据
        data_list = []
        for li in lis:
            data = {}
            if li.get_attribute('class') != 'apartments-pkg apartments':
                data['title'] = li.find_element_by_xpath('./div[2]/h2/a').text
                data['url'] = li.find_element_by_xpath('./div[2]/h2/a').get_attribute('href')
                data['price'] = li.find_element_by_xpath('./div[3]/div[2]').text
                # print(data)
                data_list.append(data)
        # 获取下一页按钮
        next_page = self.driver.find_elements_by_class_name('next')
        print(next_page)
        if len(next_page) != 0:
            next_page = next_page[0]
        else:
            next_page = None
        return data_list, next_page

    def save_data(self, data_list):
        with open('58同城租房.jsonlines', 'a', encoding='utf8')as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')

    def run(self):
        # 加载页面
        self.driver.get(self.url)
        while True:
            # 获取数据
            data_list, next_page = self.get_data_list()
            self.save_data(data_list)
            if next_page:
                next_page.click()
            else:
                break
        self.driver.save_screenshot('58租房.png')
        # time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    zfs = ZufangSpider()
    zfs.run()
