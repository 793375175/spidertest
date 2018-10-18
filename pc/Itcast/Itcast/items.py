# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    # 老师的姓名
    name = scrapy.Field()
    # 职称
    level = scrapy.Field()
    # 个人信息
    info = scrapy.Field()

