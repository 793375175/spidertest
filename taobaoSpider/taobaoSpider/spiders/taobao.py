# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re
import json

import scrapy
from taobaoSpider.items import ShopItem
import jsonpath
from taobaoSpider.spiders.startURL import StartURL



class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["taobao.com"]
    start_urls = StartURL.startURL


    def parse(self, response):

        info_list = re.findall(u'{"uid.*?}}',response.body)
        with open("info_list.txt", "w") as f:
            f.write(str(info_list))

        for info in info_list:
            item = ShopItem()
            info_json = json.loads(info, encoding = "utf-8")
            with open("info_json.txt", "w") as f:
                f.write(str(info_json))

            item['shopUrl'] = jsonpath.jsonpath(info_json, '$..shopUrl')[0]
            item['_id'] = re.findall(u'\d+', json.dumps(item['shopUrl']))[0]

            item['uid'] = jsonpath.jsonpath(info_json, '$..uid')[0]
            item['title'] = jsonpath.jsonpath(info_json, '$..title')[0]
            item['nick'] = jsonpath.jsonpath(info_json, '$..nick')[0]
            item['provCity'] = jsonpath.jsonpath(info_json, '$..provcity')[0]
            item['totalSold'] = jsonpath.jsonpath(info_json, '$..totalsold')[0]
            item['goodsCount'] = jsonpath.jsonpath(info_json, '$..procnt')[0]
            item['goodPercent'] = jsonpath.jsonpath(info_json, '$..goodratePercent')[0]
            item['sellGenus'] = jsonpath.jsonpath(info_json, '$..mainAuction')[0]

            score = jsonpath.jsonpath(info_json, '$..dsrStr')[0]
            item['score_description'] = re.findall(u'"mas":"(.*?)"',score)[0]
            item['score_manner'] = re.findall(u'"sas":"(.*?)"',score)[0]
            item['score_logistics'] = re.findall(u'"cas":"(.*?)"',score)[0]

            #yield item



            # print '================'
            # print 'score_description' + item['score_description']
            # print 'score_manner' + item['score_manner']
            # print 'score_logistics' + item['score_logistics']
            # #print 'shopURL' + item['shopURL']
            # print '_id' + item['_id']
            # print 'uid' + item['uid']
            # print 'title' + item['title']
            # print 'nick' + item['nick']
            # #print 'provCity' + item['provCity']
            # print 'totalSold' + str(item['totalSold'])
            # print 'goodsCount' + str(item['goodsCount'])
            # print 'goodPercent' + str(item['goodPercent'])
            # print 'sellGenus' + str(item['sellGenus'])
            #print 'score' + str(item['score'])

            yield item
