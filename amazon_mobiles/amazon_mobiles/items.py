# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonMobilesItem(scrapy.Item):
    # define the fields for your item here like:
    mobile_name = scrapy.Field()
    mobile_price = scrapy.Field()
    mobile_image = scrapy.Field()
