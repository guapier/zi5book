# -*- coding: utf-8 -*-
from scrapy import Request
import scrapy

from zi5book.items import Zi5BookItem


class Zi5bookSpiderSpider(scrapy.Spider):
    name = 'zi5book_spider'
    start_urls = []
    headers = {
        'pragma': "no-cache",
        'cookie': "pgv_pvi=2762272768; PHPSESSID=a987cbecdca352e260c085da785d8aa7; pgv_si=s1139271680",
        'dnt': "1",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.96 Safari/537.36",
        'accept': "text/html, */*; q=0.01",
        'cache-control': "no-cache",
        'x-requested-with': "XMLHttpRequest",
        'proxy-connection': "keep-alive",
        'referer': "http://book.zi5.me/",
    }

    def start_requests(self):
        page_url = 'http://book.zi5.me/page/{0}'
        for i in range(1, 51):
            yield Request(page_url.format(str(i)), headers=self.headers)

    def parse(self, response):
        thumbs = response.css('div.thumb-holder')
        for thumb in thumbs:
            detail_url = thumb.css('a.colorbox::attr(href)').extract_first()
            yield Request(detail_url, callback=self.parse_detail, headers=self.headers)

    def parse_detail(self, response):
        item = Zi5BookItem()
        item['name'] = response.css('.h1-wrapper > h1:nth-child(1)::text').extract_first()
        item['author'] = response.css('.post-meta-top > div:nth-child(2) > a:nth-child(1)::text').extract_first()
        item['time'] = response.css('.post-meta-top > div:nth-child(2)::text').extract_first()
        item['publisher'] = response.css('.post-meta-top > div:nth-child(2) > a:nth-child(2)::text').extract_first()
        item['comment'] = response.css('.post-meta-top > div:nth-child(1) > a:nth-child(1)::text').extract_first()
        item['view'] = response.css('.post-meta-top > div:nth-child(1)::text').extract_first()
        item['ISBN'] = response.css(
            '#post-936 > div:nth-child(3) > div:nth-child(1) > a:nth-child(1)::text').extract_first()
        item['rates'] = response.css('.rateNum::text').extract_first()
        item['updated'] = response.css('#post-936 > div:nth-child(3)::text').extract_first()
        item['desc'] = response.css('.post-content > p:nth-child(2)::text').extract_first()
        item['image_urls'] = [response.urljoin(image_url) for image_url in
                              response.css('.post-content > img:nth-child(1)::attr(src)').extract()]
        item['up'] = response.css('.thumbs-rating-up::text').extract_first()
        item['down'] = response.css('.thumbs-rating-down::text').extract_first()
        item['tags'] = response.css('.post-meta-category-tag::text').extract_first()
        item['file_urls'] = response.css('a.download-link::attr(href)').extract()

        yield item
