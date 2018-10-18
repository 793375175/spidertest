# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # city = scrapy.Field()
    # date = scrapy.Field()
    # aqi = scrapy.Field()
    # # 质量等级
    # level = scrapy.Field()
    # pm2_5 = scrapy.Field()
    # pm10 = scrapy.Field()
    # so2 = scrapy.Field()
    # co = scrapy.Field()
    # no2 = scrapy.Field()
    # o3 = scrapy.Field()
    # # 数据源（以爬虫名命名，数据分类）
    # spider = scrapy.Field()
    # 抓取时间
    time = scrapy.Field()