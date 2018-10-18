# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):

    images_name = scrapy.Field()
    images_Urls = scrapy.Field()
    images_Path = scrapy.Field()  # 照片保存在本地的路径
