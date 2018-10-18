# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from .items import TencentItem, PositionItem


class TencentPipeline(object):
    def open_spider(self, spider):
        self.f = open("tencent.json", "w")

    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            json_str = json.dumps(dict(item)) + ",\n"
            self.f.write(json_str)

        return item

    def close_spider(self, spider):
        self.f.close()


class PositionJsonPipeline(object):
    def open_spider(self, spider):
        self.f = open("position.json", "w")

    def process_item(self, item, spider):
        # 判断item所属类型
        if isinstance(item, PositionItem):
            json_str = json.dumps(dict(item)) + ",\n"
            self.f.write(json_str)
        return item

    def close_spider(self, spider):
        self.f.close()
