# -*- coding: utf-8 -*-

import time
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from taobaoSpider.items import GoodsItem
import redis



class GoodsSpider(CrawlSpider):
    name = 'goods'
    allowed_domains = ['taobao.com']
    start_urls = ['http://www.taobao.com/']


    redis_cli = redis.Redis(host = 'localhost', port = 6379)

    def start_requests(self):
        goods_info = self.redis_cli.lrange('goods_id',0,-1)
        for goods in goods_info:
            goods = list(eval(goods))
            shop_id = goods[1][1]
            goods_id = goods[0][1]
            # print '*************'
            # print goods
            # print goods[0]
            # print goods_id
            goods_url = 'https://item.taobao.com/item.htm?id=' + goods_id
            # print goods_url
            yield scrapy.Request(url = goods_url, meta = {'selenium': '', 'shop_id':shop_id, 'goods_id': goods_id}, callback = self.goods_handler)
            time.sleep(1)


    def goods_handler(self, response):
        """ 商品详细信息 """

        # with open('test.html', 'w') as f:
        #     f.write(response.body)

        # 商品名称
        title = response.xpath('//h3[@class="tb-main-title"]/text()').extract_first()
        # 商品介绍
        introduction = response.xpath('//p[@class="tb-subtitle"]/text()').extract_first()
        # 商品原价
        original_price = response.xpath('//strong[@id="J_StrPrice"]/em[2]/text()').extract_first()
        # 商品现价
        current_price = response.xpath('//strong[@class="tb-promo-price"]/em[2]/text()').extract_first()
        # 可享优惠
        privilege_list = []
        privilege_info = response.xpath('//div[@class="tb-other-discount-content"]//div')
        if privilege_info:
            for info in privilege_info:
                privilege = ''.join(info.xpath('./text()').extract()).strip()
                privilege_list.append(privilege)
        # 商品人气(收藏数)
        collect_content = response.xpath('//li[@class="tb-social-fav"]/a/em/text()').extract_first()
        if collect_content:
            collect = re.findall(u'\d+', collect_content)[0]
        else :
            collect = ''
        # 详细信息
        detail_info = []
        detail_info_content = response.xpath('//ul[@class="attributes-list"]/li/text()').extract()
        if detail_info_content:
            for info in detail_info_content:
                detail_item = info.split(u':')
                detail = {detail_item[0]:detail_item[1]}
                detail_info.append(detail)
        # 累计评论
        comment_count = response.xpath('//strong[@id="J_RateCounter"]/text()').extract_first()
        # 交易成功数
        Trading_count = response.xpath('//strong[@id="J_SellCounter"]/text()').extract_first()


        # print Trading_count
        item = GoodsItem()
        item['goodsID'] = response.meta['goods_id']
        item['shopID'] = response.meta['shop_id']
        item['title'] = title
        item['introduction'] = introduction
        item['original_price'] = original_price
        item['current_price'] = current_price
        item['privilege'] = privilege_list
        item['collect'] = collect
        item['detail_info'] = detail_info
        item['comment_count'] = comment_count
        item['Trading_count'] = Trading_count

        yield item






        # print '==================================='
        # print response.url
        # print title
        # print introduction
        # print original_price
        # print current_price
        # print privilege_list
        # print collect
        # print detail_info
        # print comment_count





