# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    categoryName_2 = scrapy.Field()
    categoryId_2 = scrapy.Field()
    fatherCategoryId_2 = scrapy.Field()
    href_2 = scrapy.Field()
    categoryName_3 = scrapy.Field()
    categoryId_3 = scrapy.Field()
    fatherCategoryId_3 = scrapy.Field()
    href_3 = scrapy.Field()


    title = scrapy.Field()

    text = scrapy.Field()
    img = scrapy.Field()
    author = scrapy.Field()
    publish = scrapy.Field()
    publish_date = scrapy.Field()
    shop_name = scrapy.Field()
    shop_href = scrapy.Field()
    price = scrapy.Field()

