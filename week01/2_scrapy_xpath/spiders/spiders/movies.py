import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

    # 解析函数
    def parse(self, response):
        # 打印网页的url
        print(response.url)

        # 用于计数-爬取10个电影数据
        i = 0

        # 电影列表
        movie_list = []

        movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        for movie in movies:
            i += 1
            if i == 11:
                break

            # 路径使用 / .  .. 不同的含义　
            title=movie.xpath('./a/text()')
            link='https://maoyan.com'+movie.xpath('./a/@href').extract_first()

            print('-----------')
            print(title.extract())
            print(link)

            yield scrapy.Request(url=link, callback=self.parse2)

    # 解析具体页面
    def parse2(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        item = SpidersItem()

        string=''

        item['name'] = movies.xpath('./h1/text()').extract_first()
        item['time'] = movies.xpath('.//li[3]/text()').extract_first()[:10]

        for x in movies.xpath('.//a/text()').extract():
            string += x

        item['type'] = string.strip()

        yield item

