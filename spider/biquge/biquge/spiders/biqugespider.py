# -*- coding: utf-8 -*-
import scrapy
from ..items import BiqugeItem


class BiqugespiderSpider(scrapy.Spider):
    name = 'biqugespider'
    #allowed_domains = ['http://www.banzhu111.com']
    #start_urls = ['http://www.banzhu111.com/7_7328/1255302.html']  #师师系列
    #start_urls=['http://www.banzhu111.com/0_919/59849.html']        #警花相伴
    #start_urls=['http://www.banzhu111.com/0_311/44246.html']         #教师
    #start_urls=['http://www.banzhu111.com/0_294/43553.html']          #校长妈妈
    #start_urls=['http://www.banzhu111.com/1_1260/68766.html']          #荒岛
    #start_urls=['http://www.banzhu111.com/5_5664/945895.html']          #女明星
    #start_urls=['http://www.banzhu111.com/6_6164/949063.html']          #穿越
    #start_urls=['http://www.banzhu111.com/0_369/46513.html']            #女偶像
    start_urls=['http://www.banzhu111.com/6_6973/1234314.html']          #留学

    def parse(self, response):

        novel_items = response.xpath('//div[@id="content"]/text()').extract()
        print(novel_items)
        #print(len(novel_items))
        #print(novel_items[0])
        #print(novel_items[1])
        for i in range(0,len(novel_items),2):
            novelitem=BiqugeItem()
            #print(novel_items[i])
            # for novel_item in novel_items:
            #     print(novel_item)
            novelitem['novel']=novel_items[i]

            yield novelitem

        nextPageURL = response.xpath('//div[@class="bottem2"]/a/@href').extract()  # 取下一页的地址
        #print(nextPageURL)
        #print(nextPageURL[2],nextPageURL[3])
        houzhui=nextPageURL[3].split('/')[-1]
        #print(houzhui)
        nexturl=nextPageURL[2]+houzhui
        #print(nexturl)
        if nexturl:
            url = response.urljoin(nexturl)
            print('下一章', url)
            # 发送下一页请求并调用parse()函数继续解析
            yield scrapy.Request(url, self.parse, dont_filter=False)
            pass
        else:
            print("退出")
        pass



