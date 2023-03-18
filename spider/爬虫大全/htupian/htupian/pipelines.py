# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HtupianPipeline(object):
    def process_item(self, item, spider):
        print('图片二级URL:{0}'.format(item['newtupianurl']))
        print('图片URL:{0}'.format(item['imgurl']))
        print('张数:{0}'.format(item['zhangshu']))
        print('题目:{0}'.format(item['biaoti']))
        print('发布日期:{0}'.format(item['riqi']))
        print('图片下载:{0}'.format(item['downloadimg']))
        print("====" * 4)
        return item
