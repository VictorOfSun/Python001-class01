# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    #防止类型顺序排到时间后面
    a_name = scrapy.Field()
    b_type = scrapy.Field()
    c_time = scrapy.Field()
