# -*- coding: utf-8 -*-
import scrapy
from ..items import MeiziItem

class MztSpider(scrapy.Spider):
    name = 'mzt'
    allowed_domains = ['meizitu.com']
    start_urls = ['http://meizitu.com/']

    def parse(self, response):
        tags = response.xpath(".//*[@class='tags']/span/a")
        for i in tags:
            item = MeiziItem()
            tag_href = i.xpath(".//@href").extract()[0]
            tag_name = i.xpath(".//@title").extract()[0]
            item['tag_name'] = tag_name
            item['tag_href'] = tag_href
            #print(item['tag_name'])
            #yield item
            yield scrapy.Request(url=item['tag_href'], meta={'item': item}, callback=self.parse_page)

    def parse_page(self, response):

        item = response.meta['item']
        # 进入某个标签后，爬取底部分页按钮
        page_lists = response.xpath(".//*[@id='wp_page_numbers']/ul/li")
        # 获取底部分页按钮上的文字，根据文字来判断当前标签页下总共有多少分页
        page_list = page_lists.xpath('.//text()')
        # 如果当前标签页下有多个页面，则再根据第一个按钮是否为“首页”来进行再次提取，因为这里有的页面第一个按钮是首页，有的第一个按钮是“1”
        if len(page_lists) > 0:
            if page_list[0].extract() == '首页':
                page_num = len(page_lists) - 3
            else:
                page_num = len(page_lists) - 2
        else:
            page_num = 1

        # 根据当前标签页的链接，来拼成带页码的链接
        if '_' in item['tag_href']:
            index = item['tag_href'][::-1].index('_')
            href_pre = item['tag_href'][:-index]
        else:
            if page_num == 1:
                href_pre = item['tag_href'].split('.html')[0]
            else:
                href_pre = item['tag_href'].split('.html')[0] + '_'
        for i in range(1, page_num + 1):
            item = response.meta['item']
            if page_num == 1:
                href = href_pre + '.html'
            else:
                href = href_pre + str(i) + '.html'
            item['page_list'] = href
            #yield item
            yield scrapy.Request(url=item['page_list'], meta={'item': item}, callback=self.parse_album)

    def parse_album(self, response):
        albums = response.xpath(".//*[@class='pic']")
        for album in albums:
            item = response.meta['item']
            album_href = album.xpath(".//a/@href").extract()[0]
            album_name = album.xpath(".//a/img/@alt").extract()[0]
            item['album_name'] = album_name
            item['album_href'] = album_href
            #yield item
            yield scrapy.Request(url=item['album_href'], meta={'item': item}, callback=self.parse_img)

    def parse_img(self, response):
        img_list = response.xpath(".//*/p/img")
        for img in img_list:
            item = response.meta['item']
            img_title = img.xpath(".//@alt").extract()[0]
            if img_title == '':
                for i in range(1, len(img_list + 1)):
                    img_title = item['album_name'] + '_' + str(i)
            else:
                img_title = img_title
            img_urls = img.xpath(".//@src").extract()
            img_src = img.xpath(".//@src").extract()[0]
            item['img_title'] = img_title
            item['img_src'] = img_src
            item['img_urls'] = img_urls
            yield item

