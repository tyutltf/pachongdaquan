# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DbmeinvPipeline(object):
    def process_item(self, item, spider):
        print('图片标题:{0}'.format(item['imgname']))
        print('图片url:{0}'.format(item['imgurl']))
        return item
