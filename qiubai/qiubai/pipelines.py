# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QiubaiPipeline:

    def __init__(self):
        self.fp = None

    def open_spider(self,spider):
        self.fp = open('./data.txt','w')
        print('爬虫开始！！')


    def process_item(self, item, spider):
        self.fp.write(item['author'] +'\t\t\t'+ item['content'] + '\n\n\n')
        print(item)
        return item

    def close_spider(self,spider):
        self.fp.close()
        print('爬虫结束！！')


#如果有多个爬虫的话，那么就可以在这里定义多个类 在item 中判断spiders 来自于哪一个
#或者也可以是哟个spider.name == .....   来判断当前的spider来自于哪一个
#或者from ..items import ..1.    使用 isinstance(item,..1.)  来判断这里的数据是我们在items中定义的哪一个对象。

'''
注意的地方是 item 是一个类似于字典的格式，但不是。。不过可以通过dict(item)转换为字典的格式

'''
