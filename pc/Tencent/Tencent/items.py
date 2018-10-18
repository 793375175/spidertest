# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
   # 职位名称
   position_name = scrapy.Field()
   # 详情链接
   position_link = scrapy.Field()
   #职位类别
   position_type = scrapy.Field()
   # 人数
   people_number = scrapy.Field()
   # 地点
   work_location = scrapy.Field()
   # 发布时间
   publish_time = scrapy.Field()
 


class PositionItem(scrapy.Item):

	# 工作职责
	publish_zhize = scrapy.Field()
	# 工作要求
	position_yaoqiu = scrapy.Field()