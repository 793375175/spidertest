# -*- coding: utf-8 -*-
import scrapy
from ..items import ItcastItem


class ItheimaSpider(scrapy.Spider):
    name = 'itheima'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']
    item_list = []

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")

        for node in node_list:
            item = ItcastItem()
            item['name'] = node.xpath("./h3/text()").extract_first()
            item['title'] = node.xpath("./h4/text()").extract_first()
            item['info'] = node.xpath("./p/text()").extract_first()

            # yield item
            self.item_list.append(item)
        return self.item_list