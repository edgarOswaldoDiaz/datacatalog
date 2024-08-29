# -*- coding: utf-8 -*-
# El siguiente codigo requiere de hacer uso de la creación de un proyecto de Spiders

import scrapy 

class ExampleSpider(scrapy.Spider): 

    name = 'example' 

    start_urls = ['https://www.facebook.com'] 

    def parse(self, response): 

        for title in response.css('h1::text').getall(): 

            yield {'title': title} 