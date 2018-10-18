#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from scrapy.http import HtmlResponse
from scrapy.conf import settings
import time
import random
import base64


class ChoiceAgent(object):
    """随机更换user-agent"""

    def process_request(self, request, spider):
        agent = random.choice(settings['USER_AGENTS'])
        request.headers.setdefault('User-Agent',agent)
        # print '向请求添加User-Agent'


user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent
# 不在PhantomJS里加载图片
driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--load-images=false'])
driver = webdriver.PhantomJS(desired_capabilities=dcap)

headers = {"User-Agent" : user_agent}


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://122.114.214.159:16816')
chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get('http://httpbin.org/ip')
print(chrome.page_source)
chrome.quit()

# mr_mao_hacker:sffqry9r

class SeleniumMiddleware(object):

    def process_request(self, request, spider):
        """ selenium 处理没有数据的代码"""
        if request.meta.has_key('selenium'):

            # agent = random.choice(settings['USER_AGENTS'])
            # dcap = dict(DesiredCapabilities.PHANTOMJS)
            # dcap["phantomjs.page.settings.userAgent"] = (agent)
            # # 不在PhantomJS里加载图片
            # driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--load-images=false'])

            driver = webdriver.Chrome()
            # print request.url
            # driver = webdriver.PhantomJS()
            driver.get(request.url)
            # driver.get("http://www.baidu.com/")
            # print driver.page_source
            time.sleep(2)


            body = driver.page_source
            url = driver.current_url
            driver.close()

            # with open('test.html','w') as f:
            #     f.write(body.encode('utf-8'))

            return HtmlResponse(url, body=body, encoding='utf-8', request=request)


class RandomProxy(object):
    """ 使用代理 """
    def __init__(self):

        self.proxy_auth = "mr_mao_hacker:sffqry9r"
        self.proxy = '122.114.136.239:16816'


    def process_request(self, request, spider):
        # freeProxy = random.choice(proxy)
        # freeproxy = freeProxy.keys()[0] + ':' + freeProxy.values()[0]
        # print '向请求添加代理'

        # request.meta['proxy'] = 'http://' + freeproxy

        base64_userpass = base64.b64encode(self.proxy_auth)
        #print proxy
        request.meta['proxy'] = "http://" + self.proxy
        #if self.proxy_auth != None:
        request.headers['Proxy-Authorization'] = "Basic " + base64_userpass
