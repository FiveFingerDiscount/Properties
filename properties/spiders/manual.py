# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from properties.items import PropertiesItem
from properties.helperfuntions import (no_build_year,
                                       no_price_available,
                                       convert_to_int)


class BasicSpider(scrapy.Spider):
    name = 'manual'
    allowed_domains = ['www.huizenzoeker.nl']
    start_urls = ['https://www.huizenzoeker.nl/koop/overijssel/zwolle/1/',
                  ]

    def parse(self, response):
        # Load fields using XPath expressions
        l = ItemLoader(item=PropertiesItem(),
                       response=response)
        l.add_xpath('build', '//tbody/tr[@id]/td[3]/text()',
                    #no_build_year,
                    )
        l.add_xpath('city', '//tbody/tr[@id]/td/text()[following-sibling::br]',
                    MapCompose(lambda i: i[9:])
                    )
        l.add_xpath('house_number', '//tbody/tr[@id]/td/a/strong/text()',
                    re='[0-9]+.')
        l.add_xpath('living_space', '//tbody/tr[@id]/td[4]/text()',
                    MapCompose(lambda i: i.split()[0],
                               convert_to_int
                               )
                    )
        l.add_xpath('plot_space', '//tbody/tr[@id]/td[5]/text()',
                    MapCompose(lambda i: i.split()[0],
                               convert_to_int
                               ),
                    default='Null'
                    )
        l.add_xpath('postal_code',
                    '//tbody/tr[@id]/td/text()[following-sibling::br]',
                    MapCompose(lambda i: i[1:8])
                    )
        l.add_xpath('price', '//tbody/tr[@id]/td/strong/text()',
                    MapCompose(no_price_available,
                               lambda i: i.replace('.', '')[2:],
                               convert_to_int
                               )
                    )
        l.add_xpath('street', '//tbody/tr[@id]/td/a/strong/text()',
                    re=r'\D+\S[A-Za-z][^- ]')
        yield l.load_item()

        # Get the next index URLs
        for url in response.xpath('//a[contains(@class, "volgende")]//@href'):
            yield response.follow(url, callback=self.parse)

# Als er None wordt gereturned moet deze als Null worden weggeschreven
