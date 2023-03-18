# -*- coding: utf-8 -*-
import scrapy
from ..items import LianjiaItem
from scrapy.http import Request
from parsel import Selector
import requests


class MylianjiaSpider(scrapy.Spider):
    name = 'mylianjia'
    #allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/chaoyang/pg']

    def start_requests(self):
        for i in range(1, 101):  #100页的所有信息
            url1 = self.start_urls + list(str(i))
            #print(url1)
            url = ''
            for j in url1:
                url += j + ''
            yield Request(url, self.parse)

    def parse(self, response):
        print(response.url)

        '''
        response1 = requests.get(response.url, params={'search_text': '粉墨', 'cat': 1001})
        if response1.status_code == 200:
            print(response1.text)
        dirPath = os.path.join(os.getcwd(), 'data')
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        with open(os.path.join(dirPath, 'lianjia.html'), 'w', encoding='utf-8')as fp:
            fp.write(response1.text)
            print('网页源码写入完毕')
        '''

        infoall=response.xpath("//div[4]/div[1]/ul/li")
        #infos = response.xpath('//div[@class="info clear"]')
        #print(infos)
        #info1 = infoall.xpath('div/div[1]/a/text()').extract_first()
        #print(infoall)
        for info in infoall:
            item =LianjiaItem()
            #print(info)
            info1 = info.xpath('div/div[1]/a/text()').extract_first()
            info1_url = info.xpath('div/div[1]/a/@href').extract_first()
            #info2 = info.xpath('div/div[2]/div/text()').extract_first()
            info2_dizhi = info.xpath('div/div[2]/div/a/text()').extract_first()
            info2_xiangxi= info.xpath('div/div[2]/div/text()').extract()
            #info3 = info.xpath('div/div[3]/div/a/text()').extract_first()
            #info4 = info.xpath('div/div[4]/text()').extract_first()
            price = info.xpath('div/div[4]/div[2]/div/span/text()').extract_first()
            perprice = info.xpath('div/div[4]/div[2]/div[2]/span/text()').extract_first()
            #print(info1,'--',info1_url,'--',info2_dizhi,'--',info2_xiangxi,'--',info4,'--',price,perprice)
            info2_xiangxi1 = ''
            for j1 in info2_xiangxi:
                info2_xiangxi1 += j1 + ''
            #print(info2_xiangxi1)  #化为字符串

            item['houseinfo']=info1
            item['houseurl']=info1_url
            item['housedizhi']=info2_dizhi
            item['housexiangxi']=info2_xiangxi1
            item['houseprice']=price
            item['houseperprice']=perprice

            yield item