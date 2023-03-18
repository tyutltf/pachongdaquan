# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeiziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标签名称
    tag_name = scrapy.Field()
    # 标签链接
    tag_href = scrapy.Field()
    # 进入某标签后的所有链接，加页码的
    page_list = scrapy.Field()
    # 图片专辑名称
    album_name = scrapy.Field()
    # 图片专辑链接
    album_href = scrapy.Field()
    # 照片标题
    img_title = scrapy.Field()
    # 照片链接
    img_src = scrapy.Field()
    # 照片链接集合，用于ImagesPipeline下载图片
    img_urls = scrapy.Field()

