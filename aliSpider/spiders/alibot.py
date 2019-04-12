# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin, urlparse
from ..items import AliexpressItem


class AlibotSpider(scrapy.Spider):
    name = 'alibot'
    start_urls = ['https://www.aliexpress.com/home.htm']

    def parse(self, response):
        urls = response.xpath(
            '// div[@class="categories-list-box"]/dl/dt/span/a/@href').extract()
        for url in urls:
            # print(urljoin('http://www.aliexpress.com', url))
            yield response.follow(url, callback=self.parse_categorie_pages)

    def parse_categorie_pages(self, response):
        urls = response.xpath(
            '//*[@id="refine-category-list"]/dl/dd/dl/ul/li/a/@href').extract()
        for url in urls:
            yield response.follow(url, callback=self.handle_product_listings)

    def handle_product_listings(self, response):
        urls = response.xpath(
            '//*[@id = "list-items"]/ul/li/div/div/h3/a/@href').extract()
        for url in urls:
            # print(urljoin('http://www.aliexpress.com', url))
            yield response.follow(url, callback=self.parse_product_detail)

        # next_page = response.xpath(
        #     '//*[@id="pagination-bottom"]/div/a[@class="page-next ui-pagination-next"]')
        # if next_page:
        #     yield response.follow(next_page, callback=self.handle_product_listings)

    def parse_product_detail(self, response):
        item = AliexpressItem()
        item['url'] = response.url.split('?')[0]
        item['product_name'] = response.xpath(
            '//*[@id="j-product-detail-bd"]/div/div/h1/text()').extract()[0].strip()
        item['product_image'] = response.urljoin(response.xpath(
            '//*[@id="magnifier"]/div/a/img/@src').extract()[0])

        price_per_unit = response.xpath(
            '//*[@id="j-sku-price"]/text()').extract()
        if price_per_unit:
            item['price_per_unit'] = price_per_unit[0].strip()

        item['product_orders'] = response.xpath(
            '//*[@id="j-order-num"]/text()').extract()[0].strip()

        print(item['product_name'])

        # yield item
