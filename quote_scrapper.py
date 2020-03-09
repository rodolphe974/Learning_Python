#quote_scrapper.py
#apprentissage de PYTHON sur OC
#pour executer : scrapy runspider quote_scrapper.py -o quotes.json 
# -*- coding: utf8 -*-
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'quotespider'
    start_urls = ['http://www.1001-citations.com/']

    def parse(self, response):
        for link in response.css('div#content div.entry h2'):
            yield {'quote': link.css('a ::text').extract_first()}
