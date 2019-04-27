# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyBJItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    CompanyName = scrapy.Field()
    mode = scrapy.Field()
    location = scrapy.Field()
    ContentHtml = scrapy.Field()
    # location = scrapy.Field()
    # pass
