# -*- coding: utf-8 -*-
import scrapy
from ..items import IdeophotosItem

photos_urls=[]
class ImagespiderSpider(scrapy.Spider):
    name = 'imagespider'
    #start_urls = ['http://http://www.win4000.com/meinvtag2.html']
    #start_urls = ['http://www.win4000.com/mt/huge.html']  #胡歌
    start_urls = ['http://www.win4000.com/mt/dilireba.html']   #迪丽热巴
    #start_urls = ['http://www.win4000.com/mt/wjk.html']  # 王俊凯
    #start_urls = ['http://www.win4000.com/mt/luhan.html']  # 鹿晗
    #start_urls = ['http://www.win4000.com/mt/yiyangqianxi.html']   #易烊千玺
    def parse(self, response):
        photos=[]
        tags = response.xpath('.//ul[@class="clearfix"]/li/a/@href').extract()
        intro=response.xpath('.//*[@class="intro_p"]/p/text()').extract()
        intro_p=response.xpath('.//ul[@class="clearfix"]/li/a/p/text()').extract()
        intro_img = response.xpath('.//ul[@class="clearfix"]/li/a/img/@title').extract()[0]
        intro_img_urls=response.xpath('.//ul[@class="clearfix"]/li/a/img/@src').extract()
        #print(tags)
        #print(intro)
        print(intro_p)
        #print(intro_p_i)
        #print(intro_img)
        #print(intro_img_urls)

        for i in range(9,33):
            photos.append(tags[i])
        print(photos)
        for j in range(0,24):
            #print(tags[j])
            item = IdeophotosItem()
            item['li_href'] = photos[j]
            #print('专辑链接:',item['li_href'])
            item['li_title'] = intro_p[j]
            # print('专辑名称:',intro_p_i)
            item['img_src'] = intro_img_urls[j]
            item['img_urls']=intro_img_urls
            #专辑图片链接
            #yield item
            yield scrapy.Request(url=item['li_href'], meta={'item': item}, callback=self.parse_page)
    def parse_page(self,response):
        item = response.xpath(".//*[@class='pic-meinv']/a/@href").extract()[0]
        imgs = response.xpath('.//*[@class="pic-meinv"]/a/img/@url').extract()[0]
        print(item)
        print('图片src:',imgs)
        photos_urls.append(imgs)
        print('图片总集合:',photos_urls)
        item=IdeophotosItem()
        item['photo_urls']=photos_urls
        print(item['photo_urls'])
        nextPageURL = response.xpath('.//*[@class="pic-next-img"]/a/@href').extract()  # 取下一页的地址
        #print(nextPageURL)
        if nextPageURL:
            url = response.urljoin(nextPageURL[-1])
            #print('url', url)
            # 发送下一页请求并调用parse()函数继续解析
            yield scrapy.Request(url, self.parse_page, dont_filter=False,meta={'item': item})
        else:
            print("退出")
        yield item



'''
# 斜杠（/）作为路径内部的分割符。
# 同一个节点有绝对路径和相对路径两种写法。
# 绝对路径（absolute path）必须用"/"起首，后面紧跟根节点，比如/step/step/...。
# 相对路径（relative path）则是除了绝对路径以外的其他写法，比如 step/step，也就是不使用"/"起首。
# "."表示当前节点。
# ".."表示当前节点的父节点

nodename（节点名称）：表示选择该节点的所有子节点

# "/"：表示选择根节点

# "//"：表示选择任意位置的某个节点

# "@"： 表示选择某个属性
'''