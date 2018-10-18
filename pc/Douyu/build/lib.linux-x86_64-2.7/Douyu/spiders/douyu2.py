# coding: utf-8

import scrapy, json
from ..items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = "douyu2"
    allowed_domains = ['douyucdn.cn']
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0

    start_urls = [base_url + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']

        if not data_list:
            return

        for data in data_list:
            item = DouyuItem()
            item['images_name'] = data['nickname']
            item['images_Urls'] = data['vertical_src']