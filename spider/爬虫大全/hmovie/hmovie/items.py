# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movieurl = scrapy.Field()
    imgurl = scrapy.Field()
    shichang = scrapy.Field()
    biaoti = scrapy.Field()
    riqi = scrapy.Field()
    mp4url = scrapy.Field()
    pass
