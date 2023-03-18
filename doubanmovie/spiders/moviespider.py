# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanmovieItem

class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    allowed_domains = ['douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        movie_items=response.xpath('//div[@class="item"]')
        for item in movie_items:
            #print(type(item))

            movie =DoubanmovieItem()
            movie['rank']=item.xpath('div[@class="pic"]/em/text()').extract()
            movie['title']=item.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/text()').extract()
            movie['quote'] = item.xpath(
                'div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"][1]/text()').extract()
            movie['star'] = item.xpath(
                'div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()

            movie['src']=item.xpath(
                'div[@class="pic"]/a/img/@src').extract()


            yield movie
            pass

        #取下一页的地址
        nextPageURL = response.xpath('//span[@class="next"]/a/@href').extract()
        #print(nextPageURL)
        if nextPageURL:
            url = response.urljoin(nextPageURL[-1])
            #print('url', url)
            # 发送下一页请求并调用parse()函数继续解析
            yield scrapy.Request(url, self.parse, dont_filter=False)
            pass
        else:
            print("退出")
        pass
