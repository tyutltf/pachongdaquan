# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NvshenwangPipeline(object):
    def process_item(self, item, spider):
        print('专辑标题:{0}'.format(item['zhuanjititle']))
        print('专辑url:{0}'.format(item['zhuanjiurl']))
        print('图片url:{0}'.format(item['imgurl']))
        print('下一页url:{0}'.format(item['next_page_url']))
        return item
