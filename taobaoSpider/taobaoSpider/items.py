# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopItem(scrapy.Item):
    """ 店铺信息 """

    _id = scrapy.Field()                  # 店铺id
    uid = scrapy.Field()                  # 店铺uid
    title = scrapy.Field()                # 店铺名称
    nick = scrapy.Field()                 # 卖家昵称
    provCity = scrapy.Field()             # 所在地区
    shopUrl = scrapy.Field()              # 店铺链接
    totalSold = scrapy.Field()            # 销售总量
    goodsCount = scrapy.Field()           # 线上商品数
    goodPercent = scrapy.Field()          # 好评率
    shopUrl = scrapy.Field()              # 店铺链接
    sellGenus = scrapy.Field()            # 主营种类
    score_description = scrapy.Field()    # 店铺动态评分-描述相符
    score_manner = scrapy.Field()         # 店铺动态评分-服务态度
    score_logistics = scrapy.Field()      # 店铺动态评分-物流服务

class GoodsItem(scrapy.Item):
    """ 商品信息 """

    goodsID = scrapy.Field()              # 商品ID
    shopID = scrapy.Field()               # 店铺ID
    title = scrapy.Field()                # 商品名称
    introduction = scrapy.Field()         # 商品介绍
    original_price = scrapy.Field()       # 商品原价
    current_price = scrapy.Field()        # 商品现价
    privilege = scrapy.Field()            # 可享优惠
    collect = scrapy.Field()              # 商品人气(收藏数)
    detail_info = scrapy.Field()          # 详细信息
    comment_count = scrapy.Field()        # 累计评论
    Trading_count = scrapy.Field()        # 交易成功数

class CommentItem(scrapy.Item):
    goodsID = scrapy.Field()              # 商品ID
    shopID = scrapy.Field()               # 店铺ID
    comment_content = scrapy.Field()      # 评论内容
    date = scrapy.Field()                 # 评论时间
    reply = scrapy.Field()                # 店家答复
    goods_sku = scrapy.Field()            # 所购商品型号


class GoodsIdItem(scrapy.Item):
    """ 
    此表用于提取商品ID向数据库中存储，
    取出后可以组成商品页的url
    不会存储数据
    
    """

    goodsID = scrapy.Field()              # 商品ID
    shopID = scrapy.Field()               # 店铺id

 


