# -*- coding: utf-8 -*-


import time
import json
import re
import chardet
import jsonpath
import scrapy
import redis
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from taobaoSpider.items import CommentItem



class CommentSpider(CrawlSpider):
    name = 'comment'
    allowed_domains = ['taobao.com']
    start_urls = ['http://www.taobao.com/']



    redis_cli = redis.Redis(host = 'localhost', port = 6379)

    def start_requests(self):
        comment_count_info = self.redis_cli.lrange('comment_count', 0, -1)
        for comment in comment_count_info:
            comment = list(eval(comment))
            # comment = goods[1][1]
            goods_id = comment[0][1]
            shop_id = comment[1][1]
            comment_count = int(comment[2][1])
            # print '*************'
            # print comment
            # print goods_id
            # print shop_id
            # print comment_count

            # 计算请求页数
            if comment_count != 0:
                if comment_count < 20:
                    page_num = 1
                else:
                    if comment_count//20 == 0:
                        page_num = comment_count//20
                    else:
                        page_num = comment_count//20 + 1

                for num in range(1, page_num + 1):
                    comment_url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId='+ str(goods_id) +'&currentPageNum='+ str(num) +'&pageSize=20'
                    # print comment_url

                    yield scrapy.Request(url = comment_url, meta = {'shop_id':shop_id, 'goods_id': goods_id}, callback = self.comment_handler)
                    time.sleep(0.5)


    def comment_handler(self,response):
        """ 抓取评论信息 """
        
        page_content = re.findall(r'\((.*)\)', response.body)
        # print chardet.detect(page_content[0])
        page_content = json.loads(page_content[0], encoding='GB2312')

        comment_list = jsonpath.jsonpath(page_content, '$..comments')
        for comment in comment_list[0]:
            item = CommentItem()
            item['shopID'] = response.meta['shop_id']
            item['goodsID'] = response.meta['goods_id']
            item['comment_content'] = jsonpath.jsonpath(comment, '$.content')
            item['date'] = jsonpath.jsonpath(comment, '$..date')
            item['reply'] = jsonpath.jsonpath(comment, '$.reply.content')
            item['goods_sku'] = jsonpath.jsonpath(comment, '$.auction.sku')[0]

            yield item





            # print item['shopID']
            # print item['goodsID']
            # print item['comment_content']
            # print item['date']
            # print item['reply']
            # print item['goods_sku']




        # print '=============================='
        # print page_content