# -*- coding: utf-8 -*-
import scrapy


class PitcherSpider(scrapy.Spider):
    name = 'pitcher'
    allowed_domains = ['npb.jp']
    start_urls = ['http://npb.jp/']

    def parse(self, response):
        pass
