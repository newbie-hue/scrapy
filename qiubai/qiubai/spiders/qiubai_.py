#encoding:utf-8
import scrapy
from ..items import QiubaiItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai_'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']
    pageNum = 1


    # def start_requests(self):
    #     post_url = 'http://fanyi.baidu.com/sug'
    #     farmdata = {
    #         'kw':'wolf',
    #     }
    #     yield scrapy.FormRequest(url = post_url,formdata=farmdata,callback=self.parse,cookies=cookies,headers=headers)
    #默认cookie会进行进行着保存，可以在settinig 中添加设置  COOKIES_DEGUGGER 这样就可以跟踪cookie的情况


    def parse(self, response):
        items = QiubaiItem()
        odiv = response.xpath('//div[@class = "col1 old-style-col1"]/div')
        for div in odiv:
            #//*[@id="qiushi_tag_124804198"]/a/div/span[1]
            items['author'] = div.xpath('.//div[@class = "author clearfix"]//h2/text()').extract_first().strip('\n')
            items['content'] = div.xpath('.//div[@class = "content"]/span/text()').extract_first().strip('\n')
            yield items

        if self.pageNum < 13:
            self.pageNum += 1
            url = f'https://www.qiushibaike.com/text/page/{self.pageNum}/'
            yield scrapy.Request(url=url,callback=self.parse)

'''
item的问题

item在一个里面并不能够完全的找到完毕，那么在第一个构造Request的时候也需要把item传递过去。。、

比如：
        yield scrapy.Request(url=url,callback=self.parse_detail,meta = {'item':item})
        
    然后在    
    def parse_detail(self.response):
        item = response.meta['item']
        ....
    之后再进行解析  
    
翻页的解决
不一定都能够找到最大的页数。那么可以看看页面中是否存在  >  等文本，如果不为空，那么就可以请求下一页的内容。
否则的话，就可以通过xpath找到下一个的链接，然后发送请求得到下一页的链接

'''











