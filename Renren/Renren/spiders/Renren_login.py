#coding:utf-8

import scrapy


class RenrenSpider(scrapy.Spider):
    name = "renren_login"
    allowed_domains = ["renren.com"]
    #start_urls = []


    def start_requests(self):
        """
            重写父类的start_requests方法，自定义第一个请求为post请求，模拟登录并记录cookies
        """
        post_url = "http://www.renren.com/PLogin.do"

        data = {
            "email" : "mr_mao_hacker@163.com",
            "password" : "alarmchime"
        }

        #scrapy.Request()
        # 1. 发送模拟登录请求提交登录数据，如果登录成功，scrapy会记录登录状态的cookies值，后续的请求会附带这个cookies
        yield scrapy.FormRequest(post_url, formdata = data, callback=self.parse)


    def parse(self, response):
        """
            在回调函数中，附带登录状态的cookies发送好友的页面请求
        """
        url_list = [
            "http://www.renren.com/410043129/profile",
            "http://www.renren.com/965999739/profile"
        ]

        # 2. scrapy会自动记录cookies，并传递给后续的请求发送
        for url in url_list:
            yield scrapy.Request(url, callback=self.parse_page)


    def parse_page(self, response):
        """
            解析好友页面的响应，提取数据
        """
        filename = response.xpath("//title/text()").extract_first()
        with open(filename, "w") as f:
            f.write(response.body)
