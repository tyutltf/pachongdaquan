# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IdeophotosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    li_title=scrapy.Field()
    li_href=scrapy.Field()
    img_src=scrapy.Field()
    img_urls=scrapy.Field()
    photo_urls=scrapy.Field()
    pass
