# 作者 ljc
import scrapy

class QQNewsSpider(scrapy.Spider):
    name = 'qqnews'
    start_urls = ['http://society.qq.com/']

    def parse(self, response):
        # // *[ @ id = "news"] / div[2] / div[3] / div / a
        for url  in response.xpath('// *[ @ id = "news"] / div / div/ div / a/@href'):

            full_url = response.urljoin(url.extract())
            yield scrapy.Request(full_url,callback=self.parse_news)

    def parse_news(self,response):
        # print('----')
        # / html / body / div / div / h1/text()

        print(response.xpath('/ html / body / div / div / h1/text()').extract_first())

