# -*- coding: utf-8 -*-
import scrapy
from ..items import HtupianItem
import urllib.request
import os
import requests

class HtupianspiderSpider(scrapy.Spider):
    name = 'htupianspider'
    allowed_domains = ['https://bx88333.com']
    start_urls = ['https://bx88333.com/html/category/photo/']  #图片
    # /bx88333.com/html/category/photo/list_7_1.html  第一页

    # def start_requests(self):
    #     for i in range(2,34,1):
    #         nextpage='https://bx88333.com/html/category/photo/list_7_'+str(i)+'.html'
    #         if nextpage:
    #             url = nextpage
    #             yield scrapy.Request(url, self.parse, dont_filter=False,)
    #         else:
    #             print("退出")

    def parse(self, response):
        tupians = response.css('.t_p')
        wenzis = response.css('.w_z')
        base_url = 'https://bx88333.com'

        for i in range(len(tupians)):
            item = HtupianItem()
            movieurl = tupians[i].xpath("a/@href").extract_first()
            imgurl = tupians[i].xpath("a/img[@class='lazy']/@data-original").extract_first()
            zhangshu = tupians[i].xpath("span/text()").extract_first()
            newtupianurl = base_url + movieurl
            biaoti = wenzis[i].xpath("h3/a/text()").extract_first()
            riqi = wenzis[i].xpath("span/text()").extract_first()

            #print(imgurl,zhangshu,newtupianurl,biaoti,riqi)
            item['imgurl']=imgurl
            item['zhangshu']=zhangshu
            item['newtupianurl']=newtupianurl
            item['biaoti']=biaoti
            item['riqi']=riqi
            #print(item['newtupianurl'])
            #yield item
            yield scrapy.Request(url=item['newtupianurl'], dont_filter=True, meta={'item': item}, callback=self.get_img)
    def get_img(self,response):
        item = response.meta['item']
        imgs=response.css('.pc_ban')
        #print(imgs)
        for img in imgs:
            dowloadimgurls=img.xpath('div/img/@src').extract()
            for dowloadimgurl in dowloadimgurls:
                #print(dowloadimgurl)
                item['downloadimg']=dowloadimgurl
                #print(item['downloadimg'])
                # r = requests.get(item['downloadimg'])
                # print(r.content)
                # imgfile=u'G:/htupian/'+item['biaoti']+'/'+item['downloadimg'][-6:]
                # print(imgfile)
                # with open(imgfile, 'wb') as f:
                #     f.write(r.content)
                with open('htupian1.txt', 'a', encoding="utf-8") as f:
                    f.write(item['biaoti']+','+item['downloadimg']+ '\n')
                yield item


                #yield scrapy.Request(url=item['downloadimg'], dont_filter=True, meta={'item': item}, callback=self.xiazai_tp)

    # def xiazai_tp(self,response):
    #     item = response.meta['item']
    #     imgPath=item['downloadimg']
    #     #imgPath='https://baxgood.com/p2/20190519-06/0012.jpg'
    #     print(imgPath)
    #     r = requests.get(imgPath)
    #     #with open('./image/img2.png', 'wb') as f:
    #     imgfile='G:/htupian/'+item['biaoti']+'/'+imgPath[-6:]
    #     print(imgfile)
    #     with open(imgfile,'wb') as f:
    #         f.write(r.content)
    #     yield item