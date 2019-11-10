# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

print('正在爬取,请耐心等待...')
class IdeophotosPipeline(object):
    def process_item(self, item, spider):
        print('专辑名称:',item['li_title'])
        print('专辑链接:',item['li_href'])
        print('图片链接:', item['img_src'])
        print('图片链接集合:', item['img_urls'])
        print('一页所有图片:',item['photo_urls'])
        print('-'*50)
        return item
