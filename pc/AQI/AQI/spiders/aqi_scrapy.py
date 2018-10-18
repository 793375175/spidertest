# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime

from ..items import AqiItem


class AqiScrapySpider(scrapy.Spider):
    name = "aqi_scrapy"
    allowed_domains = ["aqistudy.cn"]

    base_url = 'https://www.aqistudy.cn/historydata/'
    # 城市列表页的url地址
    start_urls = [base_url]

    def parse(self, response):
        city_link_list = response.xpath('//div[@class="all"]//li/a/@href').extract()


        for link in city_link_list:
            city_link = self.base_url+link
            yield scrapy.Request(city_link, callback=self.month_parse)

    def month_parse(self,response):
        month_link_list = response.xpath('//tbody//tr/a/@href').extract()
        print(month_link_list)

        for link in month_link_list:
            month_link = self.base_url + link
            yield scrapy.Request(month_link, callback=self.day_parse)

    def day_parse(self, response):
        tr_list = response.xpath('//tbody//tr[2]')

        for tr in tr_list:
            item = AqiItem()
            # item['date'] = tr.xpath('./td[1]/text()').extract_first()
            # item['aqi'] = tr.xpath('./td[2]/text()').extract_first()
            # item['level'] = tr.xpath('./td[3]/text()').extract_first()
            # item['pm2_5'] = tr.xpath('./td[4]/text()').extract_first()
            # item['pm10'] = tr.xpath('./td[5]/text()').extract_first()
            # item['so2'] = tr.xpath('./td[6]/text()').extract_first()
            # item['co'] = tr.xpath('./td[7]/text()').extract_first()
            # item['no2'] = tr.xpath('./td[8]/text()').extract_first()
            # item['o3'] = tr.xpath('./td[9]/text()').extract_first()
            # item['spider'] = self.name
            item['time'] = str(datetime.now())

            yield item