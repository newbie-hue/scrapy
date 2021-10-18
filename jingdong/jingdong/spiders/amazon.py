#-*- coding:utf-8 -*-

import html
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import re
from scrapy_redis.spiders import RedisCrawlSpider

from urllib.parse import urljoin


class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    redis_key = 'amazon'

    #start_urls = ['https://www.amazon.cn/s?i=digital-text&bbn=116169071&rh=n%3A116087071%2Cn%3A116169071&dc&fs=true&qid=1634484515&ref=sr_ex_n_1']

    rules = (
        # follow all links
        Rule(LinkExtractor(restrict_xpaths=('//li[@class = "a-spacing-micro s-navigation-indent-2"]',)), follow=True),
        Rule(LinkExtractor(restrict_xpaths=('//a[@class = "a-size-base a-link-normal a-text-normal"]')), callback='parse_detail_book'),
        Rule(LinkExtractor(restrict_xpaths=('//a[@class = "a-size-base a-link-normal a-text-normal"]')), callback='parse_detail_book'),
    )


    def parse_detail_book(self, response):
        item = {}
        item['productTitle'] = response.xpath('//span[@id = "productTitle"]/text()').extract_first().strip()
        item['author_notFaded'] = response.xpath('//span[@class = "author notFaded"]/a/text()').extract()
        item['kindle_price'] = response.xpath('//span[@class = "a-size-medium a-color-price"]/text()').extract_first().strip()
        item['publish'] = response.xpath('//span[contains(text(),"出版社")]/following-sibling::span[1]/text()').extract_first()
        item['publish_date'] = response.xpath('//span[contains(text(),"出版日期")]/following-sibling::span[1]/text()').extract_first()
        item['ASIN'] = response.xpath('//span[contains(text(),"ASIN")]/following-sibling::span[1]/text()').extract_first()
        item['ranking'] = response.xpath('//span[contains(text(),"商品里排第")]/text()').extract()[-1]
        #print(item)
        return item

