# week02 第一份作业

import scrapy
from scrapy.selector import Selector
from spiders.items import PhoneItem, CommentItem
import datetime
# export http_proxy='http://52.179.231.206:80'
# setting 增加 scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
# 通过 Request.meta['proxy'] 读取 http_proxy 环境变量加载代理


class SodaSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['smzdm.com']
    # 起始URL列表
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']

    # 解析函数
    def parse(self, response):
        item = PhoneItem()

        # 打印网页的url
        print(response.url)

        soda = Selector(response=response).xpath('//div[@class="z-feed-content "]')

        for s in soda[:10]:
            item['name'] = s.xpath('./h5/a/text()').extract_first()
            item['time'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            link = s.xpath('./h5/a/@href').extract_first()

            print('-----------')
            print(item['name'])
            print(link)

            # 增加异常处理
            try:
                yield item
                yield scrapy.Request(url=link, meta={'name': item['name']}, callback=self.parse2)
            except Exception as ex:
                print(ex)

    # 解析具体页面
    def parse2(self, response):
        item = CommentItem()

        item['name'] = response.meta['name']

        page = Selector(response=response).xpath('//li[@class="pagedown"]')
        next_page = page.xpath('./a/@href').extract_first()

        content = Selector(response=response).xpath('//div[@class="comment_con"]')
        for con in content:
            item['time'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            item['comment'] = con.xpath('./p/span/text()').extract_first()
            yield item

        if next_page:
            try:
                print(next_page)
                yield scrapy.Request(url=next_page, meta={'name': item['name']}, callback=self.parse2)
            except Exception as ex:
                print(ex)

        print('------------')


