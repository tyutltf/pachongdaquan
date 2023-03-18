# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LianjiaPipeline(object):
    def process_item(self, item, spider):
        print('房屋信息:',item['houseinfo'])
        print('房屋链接:', item['houseurl'])
        print('房屋位置:', item['housedizhi'])
        print('房屋详细信息:', item['housexiangxi'])
        print('房屋总价:', item['houseprice'],'万')
        print('平方米价格:', item['houseperprice'])
        print('===='*10)
        return item
