# -*- coding: utf-8 -*-
import scrapy


class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def parse(self, response):
        pass
