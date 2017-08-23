# -*- coding: utf-8 -*-
from scrapy import Request
import scrapy

from zi5book.items import Zi5BookItem


class Zi5bookSpiderSpider(scrapy.Spider):
    name = 'zi5book_spider'
    start_urls = []

    def start_requests(self):
        page_url='http://book.zi5.me/page/{0}'
        for i in range(1,51):
            yield Request(page_url.format(str(i)))


    def parse(self, response):
        thumbs=response.css('div.thumb-holder')
        for thumb in thumbs:
            detail_url=thumb.css('a.colorbox::attr(href)').extract_first()
            yield Request(detail_url,callback=self.parse_detail)


    def parse_detail(self,response):
        item=Zi5BookItem()
        item['name']=response.css('.h1-wrapper > h1:nth-child(1)::text').extract_first()
        item['author']=response.css('.post-meta-top > div:nth-child(2) > a:nth-child(1)::text').extract_first()
        item['time']=response.css('.post-meta-top > div:nth-child(2)::text').extract_first()
        item['publisher']=response.css('.post-meta-top > div:nth-child(2) > a:nth-child(2)::text').extract_first()
        item['comment']=response.css('.post-meta-top > div:nth-child(1) > a:nth-child(1)::text').extract_first()
        item['view']=response.css('.post-meta-top > div:nth-child(1)::text').extract_first()
        item['ISBN']=response.css('#post-936 > div:nth-child(3) > div:nth-child(1) > a:nth-child(1)::text').extract_first()
        item['rates']=response.css('.rateNum::text').extract_first()
        item['updated']=response.css('#post-936 > div:nth-child(3)::text').extract_first()
        item['desc']=response.css('.post-content > p:nth-child(2)::text').extract_first()
        item['image_urls']=[response.urljoin(image_url) for image_url in response.css('.post-content > img:nth-child(1)::attr(src)').extract()]
        item['up']=response.css('.thumbs-rating-up::text').extract_first()
        item['down']=response.css('.thumbs-rating-down::text').extract_first()
        item['tags']=response.css('.post-meta-category-tag::text').extract_first()
        item['file_urls']=response.css('a.download-link::attr(href)').extract()

        yield item


