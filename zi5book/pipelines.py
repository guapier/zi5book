# -*- coding: utf-8 -*-


import logging

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
# Define your item pipelines here
#
from scrapy.conf import settings
from scrapy.exceptions import DropItem
# from scrapy.contrib.pipeline.images import ImagesPipeline
# from scrapy.contrib.pipeline.files import FilesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self.db = connection[settings['MONGODB_DB']]
        self.collection = self.db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            try:
                self.collection.insert(dict(item))
                logging.debug("add {}".format(item['item_name']))
            except (pymongo.errors.WriteError, KeyError) as err:
                raise DropItem("Duplicated Item: {}".format(item['name']))
        return item


class MyImagePipelines(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            # 这里我把item传过去,因为后面需要用item里面的书名和章节作为文件名
            yield scrapy.Request(image_url, meta={'item': item})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        # 从URL提取图片的文件名
        image_guid = request.url.split('/')[-1].split('.')[1]
        # 拼接最终的文件名,格式:full/{书名}/{章节}/图片文件名.jpg
        filename = u'full/{0[author]}/{0[name]}/{0[name]}.{1}'.format(item, image_guid)
        return filename


class MyFilePipelines(FilesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['file_urls']:
            # 这里我把item传过去,因为后面需要用item里面的书名和章节作为文件名
            yield scrapy.Request(image_url, meta={'item': item})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        # 从URL提取图片的文件名
        image_guid = request.url.split('/')[-1].split('.')[1]
        # 拼接最终的文件名,格式:full/{书名}/{章节}/图片文件名.jpg
        filename = u'full/{0[author]}/{0[name]}/{0[name]}.{1}'.format(item, image_guid)
        return filename
