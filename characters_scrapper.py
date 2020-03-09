#characters_scrapper.py
#apprentissage de PYTHON sur OC
#pour executer : scrapy runspider characters_scrapper.py -o characters.json 
# -*- coding: utf8 -*-
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'characterspider'
    start_urls = ['https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d\'animation']

    def parse(self, response):
        for link in response.css('div#content div.entry h2'):
            yield {'character': link.css('a ::text').extract_first()}
