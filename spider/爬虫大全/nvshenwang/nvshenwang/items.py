# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NvshenwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    zhuanjiurl=scrapy.Field()
    zhuanjititle=scrapy.Field()
    imgurl=scrapy.Field()
    next_page_url=scrapy.Field()
    pass
