# -*- coding: utf-8 -*-
import scrapy

"from properties.items import PropertiesItem"


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['https://www.huizenzoeker.nl/koop/overijssel/zwolle/',
                  ]

    def parse(self, response):
        """ This function parses a property page.

        @url https://www.huizenzoeker.nl/koop/overijssel/zwolle/
        @returns items 1
        @returns requests 1
        @scrapes address postal_code price build living_space plot_space
        """
        for info in response.xpath('//tbody/tr[@id]'):
            yield {
                    'address': info.xpath('td/a/strong/text()').get(),
                    'postal_code': info.xpath(
                            'td/text()[following-sibling::br]'
                            ).get().strip('\n'),
                    'price': info.xpath('td/strong/text()').re('[.0-9]+'),
                    'build': info.xpath('td[3]/text()').get(),
                    'living_space': info.xpath('td[4]/text()').re('[.0-9]+'),
                    'plot_space': info.xpath('td[5]/text()').re('[.0-9]+'),
                    }
