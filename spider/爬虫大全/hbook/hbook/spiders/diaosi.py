# -*- coding: utf-8 -*-
import scrapy
from ..items import HbookItem
import re

class DiaosiSpider(scrapy.Spider):
    name = 'diaosi'
    allowed_domains = ['https://m.diaosixs.org']
    start_urls = ['https://m.diaosixs.org/top/allvisit_1/']

    def parse(self, response):
        item=HbookItem()
        xsms=response.css('.xsm')
        base_url='https://m.diaosixs.org/'
        for xsm in xsms:
            bookname=xsm.xpath("a/text()").extract_first()
            url = xsm.xpath("a/@href").extract_first()
            bookurl=base_url+url
            # print(bookname,bookurl)


            item['bookname']=bookname
            item['bookurl']=bookurl

            yield scrapy.Request(url=item['bookurl'], dont_filter=True, meta={'item': item}, callback=self.get_text)


    def get_text(self,response):
        item = response.meta['item']
        yuedu=response.css('.dise')[1]
        neirong_url=yuedu.xpath("@href").extract_first()
        book_neirong_url='https://m.diaosixs.org'+neirong_url
        # print(book_neirong_url)
        item['book_neirong_url']=book_neirong_url

        yield scrapy.Request(url=item['book_neirong_url'], dont_filter=True, meta={'item': item}, callback=self.get_neirong)

    def get_neirong(self,response):
        item =response.meta['item']
        zi=response.css('.zj')[0]
        xiaoshuos=zi.xpath(".//*[@id='nr']/text()").extract()
        for xiaoshuo in xiaoshuos:
            xiaoshuo =re.sub('\xa0\xa0\xa0\xa0','',xiaoshuo)
            # print(xiaoshuo)
        next_page=response.css('.dise.rt::attr(href)').extract()
        next_page_url='https://m.diaosixs.org'+next_page[0]
        print(next_page_url)
        if next_page_url:
            yield scrapy.Request(next_page_url, self.get_neirong, dont_filter=False)



