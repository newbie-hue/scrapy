#-*- coding:utf-8 -*-


import scrapy
from ..items import JingdongItem
from urllib import parse
from copy import deepcopy
import re
import json


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['book.jd.com','list.jd.com','pjapi.jd.com']
    start_urls = ['https://pjapi.jd.com/book/sort?source=bookSort&callback=jsonp_1634328391412_44986']
    page = 1
    s = 30


    def parse(self, response):
        items = JingdongItem()
        source_str = re.findall('jsonp.*?\((.*)\)',response.body.decode())[0]
        source_json = json.loads(source_str)
        #print(source_json)
        for data in source_json['data']:
            items[ 'categoryName_2'] = data['categoryName']
            items['categoryId_2'] = int(data['categoryId'])
            items['fatherCategoryId_2'] = int(data['fatherCategoryId'])
            items['href_2'] = f"https://channel.jd.com/{int(data['fatherCategoryId'])}-{int(data['categoryId'])}.html"
            for sonlist in data['sonList']:
                items['categoryName_3'] = sonlist['categoryName']
                items['categoryId_3'] = int(sonlist['categoryId'])
                items['fatherCategoryId_3'] = int(sonlist['fatherCategoryId'])
                items['href_3'] = f"https://list.jd.com/list.html?cat={int(data['fatherCategoryId'])},{int(data['categoryId'])},{int(sonlist['categoryId'])}&page={self.page}&s={self.s}"

                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'zh,zh-CN;q=0.9',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
                }
                cookies = '__jdc=122270672; __jdv=122270672|direct|-|none|-|1634285751093; __jdu=1634285751092578365451; areaId=19; shshshfp=a87d478ca56afe037dc471f6c1d36ab6; shshshfpa=674ad746-6496-c08d-988f-c732ebbef3a7-1634286066; shshshfpb=mauAr04S8fnE%2F1oZDXwND2A%3D%3D; wlfstk_smdl=u66rgm7nciwq12mflhffkh64ffvf26vw; ipLoc-djd=19-1601-50258-51885; __jda=122270672.1634285751092578365451.1634285751.1634423335.1634457249.4; RT="z=1&dm=jd.com&si=93egj0h55a&ss=kuuyqs2y&sl=1&tt=0&nu=ed8553192c8d124be55949cc1b2e99dc&cl=yt5&obo=1&ld=b9bs&r=dcfd38a96dae573c065e62f7bcd8994e&ul=b9bv&hd=ba2u"; 3AB9D23F7A4B3C9B=DMO3LVO4PM67SO6J3EQXOVZ76DZ5K342KV2S6COKAEDLHKNZ6MTQYCTCWWYPRACA7BNV6XGJAT7NSZYACJBDJTZXIA; __jdb=122270672.14.1634285751092578365451|4.1634457249; shshshsID=7ca91b041b244e347059821d963054c5_6_1634459951144'

                itemDict = {}
                itemss = cookies.split(';')
                for item in itemss:
                    key = item.split('=')[0].replace(' ', '')
                    value = item.split('=')[1]
                    itemDict[key] = value

                yield scrapy.Request(
                    url=items['href_3'],
                    headers=headers,
                    callback=self.parse_book,
                    meta={"item":deepcopy(items)}
                )
                break
            break

    def parse_book(self,response):
        items = response.meta["item"]
        #print(response.body.decode())
        li_list = response.xpath("//ul[@class = 'gl-warp clearfix']/li")
        #print('..............',li_list)
        for li in li_list:
            items['title'] = li.xpath('.//div[@class = "p-name"]//em/text()').extract_first()
            items['text'] = li.xpath('.//i[@class = "promo-words"]/text()').extract_first()
            items['img'] = parse.urljoin(response.url,li.xpath('.//div[@class = "p-img"]/a/img/@data-lazy-img').extract_first())
            items['author'] = li.xpath('.//span[@class = "p-bi-name"]/a/@title').extract()
            items['publish'] = li.xpath('.//span[@class = "p-bi-store"]/a/@title').extract_first()
            items['publish_date'] = li.xpath('.//span[@class = "p-bi-date"]/text()').extract_first()
            items['shop_name'] = li.xpath('.//div[@class = "p-shopnum"]/a/text()').extract_first()
            data_sku = li.xpath('./@data-sku') .extract_first()
            items['shop_href'] = f'https://item.jd.com/{data_sku}.html'
            items['price'] = li.xpath('.//div[@class = "p-price"]/strong/i/text()').extract_first()
            print(f"====================第{self.page}次=================")
            yield items

        #翻页

        self.page += 1
        self.s += 30
        next_url = f"https://list.jd.com/list.html?cat={items['fatherCategoryId_2']},{items['categoryId_2']},{items['categoryId_3'] }&page={self.page}&s={self.s}"
        next_path = response.xpath('//div[@id = "J_scroll_loading"]//text()')
        if  next_path:
            yield scrapy.Request(
                next_url,
                callback=self.parse_book,
                meta={"item":items}
            )




