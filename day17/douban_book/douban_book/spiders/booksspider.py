# 作者 ljc
import scrapy



class BookSpider(scrapy.Spider):
    name = 'douban_book'
    start_url = ['https://book.douban.com/top250']

    # 定义解析函数

    def parse(self, response):
        # 首先对第一页进行解析,可以自动去重
        print('1111')
        yield scrapy.Request(response.url, callback=self.parse_page)
        # 查找后面所需要的解析的界面
        for page in response.xpath('//div[@class="paginator"]/a'):
            link = page.xpath('@href').extract()[0]
            print('2222', link)
            yield scrapy.Request(link, callback=self.parse_page)

    def parse_page(self, response):
        # // *[ @ id = "content"] / div / div[1] / div / div / a[1]
        for item in response.xpath('//tr[@class="item"]'):
            print('----',item)
            # book = DoubanBookItem()
            # book['name'] = item.xpath('td[2]/div[1]/a/@title').extract()[0]
            # print(book['name'])
            # book['rating'] = item.xpath('td[2]/div[2]/span[@class="rating_nums"]/text()').extract()[0]
            # print(book['rating'])
            book_info = item.xpath('td[2]/p[1]/text()').extract()[0]
            book_info_contents = book_info.strip().split(' / ')
            print(book_info_contents)
            # book['author'] = book_info_contents[0]
            # book['publisher'] = book_info_contents[1]
            # book['edition_year'] = book_info_contents[2]
            # book['price'] = book_info_contents[3]
            yield book
