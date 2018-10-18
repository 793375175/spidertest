# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
import redis
from taobaoSpider.items import ShopItem
from taobaoSpider.items import GoodsIdItem
from taobaoSpider.items import GoodsItem
from taobaoSpider.items import CommentItem



# class TaobaospiderPipeline(object):


#     def process_item(self, item, spider):
#         """ 写入本地文件 """

#         if not os.path.exists('data/'+ item['_id']+'_shop'):
#             os.mkdir('data/'+ item['_id']+'_shop')
        
#         folder = 'data/'+ item['_id']+'_shop'

#         if isinstance(item, ShopItem):
#             with open(folder+'/shop_info.json','w') as f:
#                 content = json.dumps(dict(item), ensure_ascii=False).encode('utf-8') + "\n"
#                 print '8**************************************************'
#                 print content
#                 f.write(content)


class RedisPipline(object):
    """ 写入redis数据库 """

    def process_item(self, item, spider):
        redis_cli = redis.Redis(host = 'localhost', port = 6379)
        if isinstance(item, ShopItem):
            item = dict(item).items()
            # print '*****'
            # print item
            redis_cli.lpush("shop_info", item)
            redis_cli.sadd('shop_id', item[10][1])

        if isinstance(item, GoodsIdItem):
            item = dict(item).items()
            # print type(item)
            redis_cli.lpush("goods_id", item)

        if isinstance(item, GoodsItem):
            item = dict(item).items()
            # print item
            redis_cli.lpush("goods_info", item)
            comment_count = [item[2], item[6], item[8]]
            redis_cli.lpush("comment_count", comment_count)

        if isinstance(item, CommentItem):
            item = dict(item).items()
            # print item
            redis_cli.lpush("comment_info", item)








