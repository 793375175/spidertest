# coding=utf-8
# -*- conding: utf-8 -*-
"""
    爬取斗鱼直播平台的所有房间信息
    要求:

    获取房间图片, 房间URL,房间标题,房间类别, 房间所有者, 房间热度信息
    每一个房间的信息,以json格式保存到文件中, 每个房间占一行
    思路:

    初始无界面的ChromeDriver
    使用driver访问斗鱼的所有房间列表
    使用driver获取房间信息列表
    保房间列表信息
    实现分页效果
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json



class DouyuSpider(object):

    def __init__(self):
        options = Options()
        options.set_headless()
        self.driver = webdriver.Chrome(options=options)
        self.url = 'https://www.douyu.com/directory/all'

    def get_data_list(self):
        lis = self.driver.find_elements_by_xpath('//*[@id="live-list-contentbox"]/li/a')
        data_list = []
        for li in lis:
            data = {}
            data['room_url'] = li.get_attribute('href')
            data['room_img'] = li.find_elements_by_xpath('./span/img')
            data['room_img'] = data['room_img'][0].get_attribute('data-original') if len(data['room_img']) != 0 else None


            data['title'] = li.find_elements_by_xpath('./div/div/h3')
            data['title'] = data['title'][0].text if len(data['title']) != 0 else None

            data['class_room'] = li.find_elements_by_xpath('./div/div/span')
            data['class_room'] = data['class_room'][0].text if len(data['class_room']) != 0 else None

            data['author'] = li.find_elements_by_xpath('./div/p/span[1]')
            data['author'] = data['author'][0].text if len(data['author']) != 0 else None

            data['room_hot'] = li.find_elements_by_xpath('./div/p/span[2]')
            data['room_hot'] = data['room_hot'][0].text if len(data['room_hot']) != 0 else None
            print(data)
            data_list.append(data)

        # 获取下一页标签
        next_page = self.driver.find_element_by_link_text('下一页')
        # find 找不到返回-1
        if next_page.get_attribute('class').find('disable') != -1:
            next_page = None
        return data_list, next_page

    def save_page(self, data_list):
        with open('斗鱼.jsonlines', 'a', encoding='utf8') as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')

    def run(self):
        self.driver.get(self.url)

        while True:
            data_list, next_page = self.get_data_list()
            self.save_page(data_list)

            if next_page:
                next_page.click()
            else:
                break

        self.driver.quit()

if __name__ == '__main__':
    dys = DouyuSpider()
    dys.run()


