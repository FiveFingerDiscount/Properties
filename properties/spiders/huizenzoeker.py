# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from properties.items import PropertiesItem


class BasicSpider(scrapy.Spider):
    name = 'huizenzoeker'
    allowed_domains = ['www.huizenzoeker.nl']
    start_urls = ['https://www.huizenzoeker.nl/koop/overijssel/zwolle/1/',
                  ]

    def parse(self, response):
        # Convert rows into items
        rows = response.xpath('//tbody/tr[@id]')
        for row in rows:
            # Load fields using XPath expressions
            l = ItemLoader(item=PropertiesItem(),
                           selector=row, response=response)
            l.add_xpath('build', './td[3]/text()')
            l.add_xpath(
                'city', './td/text()[following-sibling::br]')
            l.add_xpath('house_number', './td/a/strong/text()',
                        re='[0-9]+.')
            l.add_xpath('living_space', './td[4]/text()')
            l.add_xpath('plot_space', './td[5]/text()')
            l.add_xpath('postal_code',
                        './td/text()[following-sibling::br]')
            l.add_xpath('price', './td/strong/text()')
            l.add_xpath('street', './td/a/strong/text()',
                        re=r'\D+\S[A-Za-z][^- ]')
            yield l.load_item()

        # Get the next index URL
        urls = response.xpath(
            '//a[contains(@class, "volgende")]//@href').extract()
        if len(urls) > 0:
            yield response.follow(urls[0], callback=self.parse)
