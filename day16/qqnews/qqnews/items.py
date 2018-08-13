# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QqnewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #顶item的解析字典
    title=scrapy.Field()#新闻的标题
    text = scrapy.Field()#新闻的内容
    pass
