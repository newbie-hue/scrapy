import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E7%99%BE%E5%BA%A6%E8%B4%B4%E5%90%A7%E7%BD%91%E9%A1%B5%E7%89%88&ie=utf-8&pn=0']


    #定义提取url郭泽的地方
    rules = (
        #LinkExtractor 链接提取器，提取url地址。
        #callback  提取到的url地址的response 交给callback(这个链接提取器得到的链接是否需要进行解析里面的内容)进行处理。。而且合理的callback可以有，也可以没有。
        #follow   当前url的地址是否还会通过这个连接提取器来进行提取。不写默认为False
        Rule(LinkExtractor(allow=r'/p/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'//tieba.baidu.com/f?kw=%E7%99%BE%E5%BA%A6%E8%B4%B4%E5%90%A7%E7%BD%91%E9%A1%B5%E7%89%88&ie=utf-8&pn=\d+'), follow=True),
    )


    #没有parse函数，不能定义parse函数。  因为前面提取到的url地址由parse进行解析。拥有特殊功能。
    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        item['title'] = response.xpath('//div[@class = "core_title_wrap_bright clearfix"]/h3/text()').extract_first()
        divs = response.xpath('//div[@class = "l_post l_post_bright j_l_post clearfix"]')
        for div in divs:
            item['author'] = div.xpath('.//li[@class = "d_name]//text()').extract_first()
            item['title'] = div.xpath('//div[@class = "d_post_content j_d_post_content"]//text()').extract_first()
            yield item

