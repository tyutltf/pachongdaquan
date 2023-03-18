# -*- coding: utf-8 -*-
import scrapy
from ..items import DbmeinvItem

class MeinvspiderSpider(scrapy.Spider):
    name = 'meinvspider'
    allowed_domains = ['https://www.dbmeinv.com/']
    start_urls = ['https://www.dbmeinv.com/']

    def parse(self, response):
        imglis=response.css('.span3')
        #print(imglis)
        for imgli in imglis:
            #print(imgli)
            item=DbmeinvItem()
            imgname=imgli.xpath('div[@class="thumbnail"]/div[@class="img_single"]/a/img/@title').extract_first()
            imgurl=imgli.xpath("div[@class='thumbnail']/div[@class='img_single']/a/img/@src").extract_first()
            #print(imgname,imgurl)
            item['imgname']=imgname
            item['imgurl']=imgurl
            yield item
        pass
        baseurl='https://www.dbmeinv.com'
        next_page_li=response.css('.next.next_page')
        #print(next_page_li)
        nextpageurl=next_page_li.xpath('a/@href').extract_first()
        #print(nextpageurl)
        url=baseurl+nextpageurl
        print(url)
        if url:
            url=url
            yield scrapy.Request(url, dont_filter=True,callback=self.parse)
        else:
            print('退出')
