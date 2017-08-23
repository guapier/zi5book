# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Zi5BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field()
    name=scrapy.Field()
    time=scrapy.Field()
    author=scrapy.Field()
    publisher=scrapy.Field()
    comment=scrapy.Field()
    view=scrapy.Field()
    ISBN=scrapy.Field()
    rates=scrapy.Field()
    updated=scrapy.Field()
    desc=scrapy.Field()
    tags=scrapy.Field()
    up=scrapy.Field()
    down=scrapy.Field()
    image_urls=scrapy.Field()
    file_urls=scrapy.Field()
    images=scrapy.Field()
    files=scrapy.Field()

