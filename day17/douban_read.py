# 作者 ljc
import scrapy


class douban_read(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 顶item的解析字典
    name = scrapy.Field()
    price = scrapy.Field()
