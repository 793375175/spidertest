# -*- coding: utf-8 -*-


import scrapy


class RenrenSpider(scrapy.Spider):

    name = "Renren_cookie"
    start_urls = [
        "http://www.renren.com/410043129/profile",
        "http://www.renren.com/965999739/profile"
    ]

    def start_requests(self):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "www.renren.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
        cookies = {
            "anonymid": "j7wsz80ibwp8x3",
            "_r01_": "1",
            "ln_uact": "mr_mao_hacker@163.com",
            "ln_hurl": "http://hdn.xnimg.cn/photos/hdn521/20180807/1240/main_GRfq_0ab200000ea8195a.jpg",
            "depovince": "GW",
            "ick_login": "52da33be-0bca-4181-9683-3e95476490ec",
            "first_login_flag": "1",
            "loginfrom": "syshome",
            "JSESSIONID": "abciJSRyxe5He5witJ_vw",
            "jebecookies": "3afe395e-ec5b-4f01-ab1c-8a5e51d88e45|||||",
            "_de": "BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5",
            "p": "905258fcf48cb50262ed92205ed3e0799",
            "t": "8afab1e279e0976c45c0427bf6a5d4a79",
            "societyguester": "8afab1e279e0976c45c0427bf6a5d4a79",
            "id": "327550029",
            "xnsid": "816e3cb4",
            "wp_fold": "0",
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):
        filename = response.xpath("//title/text()").extract_first()

        with open(filename, 'w') as f:
            f.write(response.body)