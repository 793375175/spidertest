# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem, PositionItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    # 固定的url地址
    base_url = 'https://hr.tencent.com/position.php?start='
    # 偏移量
    offset = 0

    start_urls = [base_url + str(offset)]

    # start_urls = [base_url + str(page) for page in range(0, 1409, 10)]

    def parse(self, response):
        node_list = response.xpath('//tr[@class="odd"] | //tr[@class="even"]')

        for node in node_list:
            item = TencentItem()
            item['position_name'] = node.xpath("./td[1]/a/text()").extract_first()
            item['position_link'] = u"https://hr.tencent.com/" + node.xpath("./td[1]/a/@href").extract_first()
            item['position_type'] = node.xpath("./td[2]/text()").extract_first()
            item['people_number'] = node.xpath("./td[3]/text()").extract_first()
            item['work_location'] = node.xpath("./td[4]/text()").extract_first()
            item['publish_time'] = node.xpath("./td[5]/text()").extract_first()

            yield item
            # 发送详情页的请求

            yield scrapy.Request(item['position_link'], callback=self.parse_detail)

            # if self.offset < 1390:
            #     self.offset += 10
            #     next_url = self.base_url + str(self.offset)
            #     # callback: 表示该请求发送后，返回的响应交给指定的 回调函数解析 parse
            #     yield scrapy.Request(next_url, callback=self.parse)

        if not response.xpath("//a[@class='noactive' and @id='next']"):
            next_url = u"https://hr.tencent.com/" + response.xpath(".//a[@id='next']/@href").extract_first()

            yield scrapy.Request(next_url, callback=self.parse)


def parse_detail(self, response):
    item = PositionItem()

    # 工作职责
    item['position_zhize'] = response.xpath("//ul[@class='squareli']")[0].xpath('.//li/text()').extract()

    # 工作要求
    item['position_yaoqiu'] = response.xpath("//ul[@class='squareli']")[1].xpath('.//li/text()').extract()

    yield item
