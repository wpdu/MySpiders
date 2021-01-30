import scrapy


class FtxspiderSpider(scrapy.Spider):
    name = 'ftxspider'
    allowed_domains = ['newhouse.fang.com']
    start_urls = ['https://zz.newhouse.fang.com/house/s/b92/']

    def parse(self, response):
        li_list = response.xpath("//div[@class='nhouse_list_content']//ul/li")
