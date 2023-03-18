# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JobspidersPipeline(object):
    def process_item(self, item, spider):
        print('职位:', item['jobPosition'])
        #print('职位url:', item['jobPositionhref'])
        print('公司:', item['jobCompany'])
        print('工作地点:', item['jobArea'])
        print('薪资:', item['jobSale'])
        print('发布时间:', item['jobDate'])
        print('详细信息:', item['jobDescribe'])
        print('----------------------------')
        return item
