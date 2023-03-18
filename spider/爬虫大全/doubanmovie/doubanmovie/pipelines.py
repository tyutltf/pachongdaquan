# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        print('电影排名:{0}'.format(item['rank'][0]))
        print('电影名称:{0}'.format(item['title'][0]))
        print('电影短评:{0}'.format(item['quote'][0]))
        print('评价分数:{0}'.format(item['star'][0]))
        print('评价人数:{0}'.format(item['star'][1]))
        print('图片链接:{0}'.format(item['src']))
        print('-' * 20)
        return item

