# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HtupianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imgurl = scrapy.Field()
    zhangshu = scrapy.Field()
    newtupianurl = scrapy.Field()
    biaoti = scrapy.Field()
    riqi = scrapy.Field()
    downloadimg=scrapy.Field()
    pass
