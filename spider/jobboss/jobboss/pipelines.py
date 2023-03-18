# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JobbossPipeline(object):
    def process_item(self, item, spider):
        print('职位名:',item["job_title"])
        print('薪资:',item["compensation"])
        print('公司名:',item["company"])
        print('公司地点:',item["address"])
        print('工作经验:',item["seniority"])
        print('学历要求:',item["education"])
        print('公司类型:',item["company_type"])
        print('融资:',item["company_finance"])
        print('公司人数:',item["company_quorum"])
        print('-'*50)
        return item
