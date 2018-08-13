# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QqnewsPipeline(object):
    def open_spilder(self,out_file):
        out = open('file' )
    def process_item(self, item, spider):
        #对item进行处理 例如保存到数据库等等
        return item
