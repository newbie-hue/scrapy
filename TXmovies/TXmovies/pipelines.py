# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import time


class TxmoviesPipeline:
    def __init__(self):
        self.start = None

    def open_spider(self,spider):
        self.start = time.time()
        print("开始时间",time.time())

    def process_item(self, item, spider):
        print(item)
        return item

    def close_spider(self,spider):
        print("用时：",time.time()-self.start)