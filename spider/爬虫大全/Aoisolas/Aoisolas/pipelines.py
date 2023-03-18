# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import re
from scrapy.exceptions import DropItem

class AoisolasPipeline(object):
    def get_media_requests(self, item, info):
        return [requests.Request(x) for x in item.get(self.item_completed(), [])]

    def file_path(self, request, response=None, info=None):
        name = request.meta['item']
        # name = filter(lambda x: x not in '()0123456789', name)
        name = re.sub(r'[？\\*|“<>:/()0123456789]', '', name)
        image_guid = request.url.split('/')[-1]
        # name2 = request.url.split('/')[-2]
        filename = u'full/{0}/{1}'.format(name, image_guid)
        return filename
        # return 'full/%s' % (image_guid)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_path
        return item



