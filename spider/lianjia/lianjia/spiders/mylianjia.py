# -*- coding: utf-8 -*-
import scrapy


class MylianjiaSpider(scrapy.Spider):
    name = 'mylianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['http://lianjia.com/']

    def parse(self, response):
        pass
