import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E7%99%BE%E5%BA%A6%E8%B4%B4%E5%90%A7%E7%BD%91%E9%A1%B5%E7%89%88&ie=utf-8&pn=0']


    #������ȡurl����ĵط�
    rules = (
        #LinkExtractor ������ȡ������ȡurl��ַ��
        #callback  ��ȡ����url��ַ��response ����callback(���������ȡ���õ��������Ƿ���Ҫ���н������������)���д��������Һ����callback�����У�Ҳ����û�С�
        #follow   ��ǰurl�ĵ�ַ�Ƿ񻹻�ͨ�����������ȡ����������ȡ����дĬ��ΪFalse
        Rule(LinkExtractor(allow=r'/p/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'//tieba.baidu.com/f?kw=%E7%99%BE%E5%BA%A6%E8%B4%B4%E5%90%A7%E7%BD%91%E9%A1%B5%E7%89%88&ie=utf-8&pn=\d+'), follow=True),
    )


    #û��parse���������ܶ���parse������  ��Ϊǰ����ȡ����url��ַ��parse���н�����ӵ�����⹦�ܡ�
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

