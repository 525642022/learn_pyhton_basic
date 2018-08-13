#by 寒小阳(hanxiaoyang.ml@gmail.com)

import scrapy


class JulyeduSpider(scrapy.Spider):
    name = "julyedu"
    start_urls = [
        'http://www.cnblogs.com/pick/#p%s'% p for p in range(1,21)
    ]

    def parse(self, response):
        for blog in response.xpath('//div[@class="post_item"]'):
            print(blog.xpath('div[@class="digg"]/div/span/text()').extract_first())
            # print julyedu_class.xpath('a/h4/text()').extract_first()
            # print julyedu_class.xpath('a/p[@class="course-info-tip"][1]/text()').extract_first()
            # print julyedu_class.xpath('a/p[@class="course-info-tip"][2]/text()').extract_first()
            # print response.urljoin(julyedu_class.xpath('a/img[1]/@src').extract_first())
            # print "\n"



