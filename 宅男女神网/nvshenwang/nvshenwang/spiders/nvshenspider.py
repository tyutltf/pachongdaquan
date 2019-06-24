# -*- coding: utf-8 -*-
import scrapy
from ..items import NvshenwangItem


class NvshenspiderSpider(scrapy.Spider):
    name = 'nvshenspider'
    allowed_domains = ['https://www.nvshens.com/']
    start_urls = ['https://www.nvshens.com/gallery/']

    def parse(self, response):
        gallerylis=response.css('.galleryli')
        #print(gallerylis)
        base_url='https://www.nvshens.com/'
        for galleryli in gallerylis:
            item = NvshenwangItem()
            zhuanjiurl=galleryli.xpath('div[2]/a/@href').extract_first()
            zhuanjiurl=base_url+zhuanjiurl
            zhuanjititle=galleryli.xpath('div[2]/a/text()').extract_first()
            #print(zhuanjiurl,zhuanjititle)
            item['zhuanjiurl']=zhuanjiurl
            item['zhuanjititle']=zhuanjititle
            #yield item
            #print(item['zhuanjiurl'],item['zhuanjititle'])
            yield scrapy.Request(url=item['zhuanjiurl'], dont_filter=True, meta={'item': item}, callback=self.get_img)
    def get_img(self,response):
        base_url='https://www.nvshens.com'
        item=response.meta['item']
        #print(item)
        imgs=response.css('.gallery_wrapper')
        for img in imgs:
            #item=NvshenwangItem()
            imgurl=img.xpath('ul/img/@src').extract()
            item['imgurl']=imgurl
            #print(item['imgurl'])
        #print(item)
        next_page_url = response.css('.a1::attr(href)').extract()[1]
        base_url = 'https://www.nvshens.com'
        next_page_url = base_url + next_page_url
        item['next_page_url']=next_page_url
        #print(item)
        if next_page_url:
            url = next_page_url
            # 发送下一页请求并调用get_img()函数继续解析
            yield scrapy.Request(url, self.get_img, dont_filter=True,meta={'item': item})
        else:
            print("退出")
        yield item
        #yield scrapy.Request(url=item['next_page_url'], callback=self.get_img, dont_filter=True)

    # def next_page(self,response):
    #     item=response.meta['item']
    #     print(item)
    #     next_page_url=item['next_page_url']
    #     #print(next_page_url)
    #     if next_page_url:
    #         yield scrapy.Request(next_page_url, dont_filter=False,callback=self.get_img, meta={'item': item})
    #     else:
    #         yield scrapy.Request(url=item['zhuanjiurl'], dont_filter=False,callback=self.parse, meta={'item': item})
    #     yield item
