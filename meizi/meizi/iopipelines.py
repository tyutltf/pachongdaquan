
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class MztImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['img_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("该Item没有图片")
        return item
