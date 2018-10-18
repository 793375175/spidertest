# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from datetime import datetime
from scrapy.exporters import CsvItemExporter


# class AqiPipeline(object):
#
#
#     def process_item(self, item, spider):
#         item['time'] = str(datetime.now())
#         item['spider'] = spider.name
#
#         return item

class AqiCsvPipeline(object):

    def open_spider(self,spider):

        self.csv_file = open('aqi.csv', 'w')
        # 创建csv文件读写对象，调用export_time()写入item数据
        self.csv_exporter = CsvItemExporter(self.csv_file)
        # 开始进行item数据写入
        self.csv_exporter.start_exporting()

    def process_item(self, item, spider):
        # 写入item数据到指定cava文件中
        print(dict(item))
        self.csv_exporter.export_item(item)

        return item

    def close_spider(self, spider):
        # 结束item数据写入
        self.csv_exporter.finish_exporting()
        # 关闭文件
        self.csv_file.close()
