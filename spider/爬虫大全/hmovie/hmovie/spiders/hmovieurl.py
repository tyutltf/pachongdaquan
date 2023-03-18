# -*- coding: utf-8 -*-
import scrapy
from ..items import HmovieItem


class HmovieurlSpider(scrapy.Spider):
    name = 'hmovieurl'
    allowed_domains = ['https://bx88222.com']
    start_urls = ['https://bx88222.com/html/category/video/']  #电影
    # secondurl='https://bx88222.com/html/category/video/page_2.html'
    def start_requests(self):
        for i in range(1,1000,1):
            nextpage='https://bx88222.com/html/category/video/page_'+str(i)+'.html'
            if nextpage:
                url = nextpage
                yield scrapy.Request(url, self.parse, dont_filter=False,)
            else:
                print("退出")

    def parse(self, response):
        url=response.url
        #print(url)
        tupians=response.css('.t_p')
        wenzis = response.css('.w_z')
        base_url='https://bx88222.com'

        for i in range(len(tupians)):
            item = HmovieItem()
            movieurl = tupians[i].xpath("a/@href").extract_first()
            imgurl = tupians[i].xpath("a/img[@class='lazy']/@data-original").extract_first()
            shichang = tupians[i].xpath("span/text()").extract_first()
            newmovieurl = base_url + movieurl
            biaoti = wenzis[i].xpath("h3/a/text()").extract_first()
            riqi = wenzis[i].xpath("span/text()").extract_first()
            #print(newmovieurl,imgurl,shichang,biaoti,riqi)
            item['movieurl']=newmovieurl
            item['imgurl']=imgurl
            item['shichang']=shichang
            item['biaoti']=biaoti
            item['riqi']=riqi
            yield scrapy.Request(url=item['movieurl'],dont_filter=True,meta={'item': item}, callback=self.get_mp4)
    def get_mp4(self,response):
        item= response.meta['item']
        mp4=response.css(".x_z")
        mp4url=mp4.xpath("a/@href").extract_first()
        item['mp4url']=mp4url
        #yield item
        yield scrapy.Request(url=item['movieurl'], dont_filter=True, meta={'item': item}, callback=self.xieru_txt)

    def xieru_txt(self,response):
        item=response.meta['item']
        #print(item['movieurl'])
        with open('hmovie.txt','a',encoding="utf-8") as f:
            f.write(item['mp4url']+','+item['biaoti']+','+item['shichang']+','+item['riqi']+'\n')
        yield item
        pass

