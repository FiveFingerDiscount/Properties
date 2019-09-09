# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertiesItem(scrapy.Item):
    # define the fields for your item here like:
    # Primary fields
    build = scrapy.Field()
    city = scrapy.Field()
    living_space = scrapy.Field()
    house_number = scrapy.Field()
    plot_space = scrapy.Field()
    postal_code = scrapy.Field()
    price = scrapy.Field()
    street = scrapy.Field()

    # Calculated fields
    images = scrapy.Field()
    location = scrapy.Field()

    # Housekeeping fields
    url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    date = scrapy.Field()
    pass
