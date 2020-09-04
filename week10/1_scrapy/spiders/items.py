# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhoneItem(scrapy.Item):
    name = scrapy.Field()
    time = scrapy.Field()


class CommentItem(scrapy.Item):
    name = scrapy.Field()
    time = scrapy.Field()
    comment = scrapy.Field()

