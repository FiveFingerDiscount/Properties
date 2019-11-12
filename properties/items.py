# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from properties.helper_functions import (no_build_year,
                                         no_price_available,
                                         convert_to_int,
                                         )


class PropertiesItem(scrapy.Item):
    # define the fields for your item here like:
    # Primary fields
    build = scrapy.Field(
        input_processor=MapCompose(no_build_year),
        output_processor=TakeFirst()
    )
    city = scrapy.Field(
        input_processor=MapCompose(lambda i: i[9:]),
        output_processor=TakeFirst()
    )
    house_number = scrapy.Field()
    living_space = scrapy.Field(
        input_processor=MapCompose(lambda i: i.split()[0],
                                   convert_to_int
                                   ),
        output_processor=TakeFirst()
    )
    plot_space = scrapy.Field(
        input_processor=MapCompose(lambda i: i.split()[0],
                                   convert_to_int
                                   ),
        output_processor=TakeFirst()
    )
    postal_code = scrapy.Field(
        input_processor=MapCompose(lambda i: i[1:8]),
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(no_price_available,
                                   lambda i: i.replace('.', '')[2:],
                                   convert_to_int
                                   ),
        output_processor=TakeFirst()
    )
    street = scrapy.Field()
    
    # # Calculated fields
    # images = scrapy.Field()
    # location = scrapy.Field()

    # # Housekeeping fields
    # url = scrapy.Field()
    # project = scrapy.Field()
    # spider = scrapy.Field()
    # server = scrapy.Field()
    # date = scrapy.Field()
