# -*- coding: utf-8 -*-

import time
import re

import redis
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from taobaoSpider.items import GoodsIdItem




class GoodsidSpider(CrawlSpider):
    name = 'goodsID'
    allowed_domains = ['taobao.com']
    start_urls = ['http://www.taobao.com/']

    redis_cli = redis.Redis(host = 'localhost', port = 6379)

    def start_requests(self):
        while True:
            shop_id = self.redis_cli.spop('shop_id')
            all_goods_url = 'https://shop'+ shop_id +'.taobao.com/search.htm?pageNo='
            time.sleep(0.2)
            yield scrapy.Request(url = all_goods_url, meta = {'selenium': '', 'shop_id': shop_id, 'page_falg': ''}, callback = self.all_goods_handler)



    def all_goods_handler(self, response):
        """ 提取所有商品id """

        goods_id_list = response.xpath('//div[@class="shop-hesper-bd grid"]//dl/@data-id').extract()
        for goods_id in goods_id_list:
            item = GoodsIdItem()
            item['goodsID'] = goods_id
            item['shopID'] = response.meta['shop_id']
            yield item

        if response.meta.has_key('page_falg'):
            page_info = response.xpath('//span[@class="page-info"]/text()').extract_first()
            page_count = re.findall(ur'/(\d+)', page_info)
            # print 'page_info',page_info
            # print page_count[0]
            for page in range(2, int(page_count[0]) + 1):
                # print page
                url = 'https://shop'+ response.meta['shop_id'] +'.taobao.com/search.htm?pageNo=' + str(page)

                yield scrapy.Request(url = url, meta = {'selenium': '', 'shop_id': response.meta['shop_id']}, callback = self.all_goods_handler)

            
