# -*- coding: utf-8 -*-
import scrapy
from ..items import SixmaoItem


class SixmaospiderSpider(scrapy.Spider):
    name = 'sixmaospider'
    #allowed_domains = ['http://www.6mao.com']
    start_urls = ['http://www.6mao.com/html/40/40184/12601161.html']  #圣墟

    def parse(self, response):
        novel_biaoti = response.xpath('//div[@id="content"]/h1/text()').extract()
        #print(novel_biaoti)
        novel_neirong=response.xpath('//div[@id="neirong"]/text()').extract()
        print(novel_neirong)
        #print(len(novel_neirong))
        novelitem = SixmaoItem()
        novelitem['novel_biaoti'] = novel_biaoti[0]
        print(novelitem['novel_biaoti'])

        for i in range(0,len(novel_neirong),2):
            #print(novel_neirong[i])

            novelitem['novel_neirong'] = novel_neirong[i]

            yield novelitem

        #下一章
        nextPageURL = response.xpath('//div[@class="s_page"]/a/@href').extract()  # 取下一页的地址
        nexturl='http://www.6mao.com'+nextPageURL[2]
        print('下一章',nexturl)
        if nexturl:
            url = response.urljoin(nexturl)
            # 发送下一页请求并调用parse()函数继续解析
            yield scrapy.Request(url, self.parse, dont_filter=False)
            pass
        else:
            print("退出")
        pass

