# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class AliexpressItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    product_name = Field()
    product_image = Field()
    price_per_unit = Field()
    unit = Field()
    product_orders = Field()
    # rating = Field()
    # product_reviews = Field()
    # product_origin = Field()
