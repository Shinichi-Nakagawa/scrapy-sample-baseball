# -*- coding: utf-8 -*-
import scrapy

from baseball.spiders import TEAMS, LEAGUE_TOP
from baseball.items import BatterItem


class BatterSpider(scrapy.Spider):
    name = 'batter'
    allowed_domains = ['npb.jp']
    URL_TEMPLATE = 'http://npb.jp/bis/{year}/stats/idb{league}_{team}.html'

    def __init__(self, year=2017, league=LEAGUE_TOP):
        self.start_urls = self._get_start_urls(year, league)

    def _get_start_urls(self, year, league):
        return [self.URL_TEMPLATE.format(year=year, league=league, team=t) for t in TEAMS]

    def parse(self, response):
        for tr in response.xpath('//*[@id="stdivmaintbl"]/table').xpath('tr'):
            item = BatterItem()
            item['name'] = tr.xpath('td[2]/text()').extract_first()
            item['games'] = tr.xpath('td[3]/text()').extract_first()
            item['pa'] = tr.xpath('td[4]/text()').extract_first()
            item['ab'] = tr.xpath('td[5]/text()').extract_first()
            item['r'] = tr.xpath('td[6]/text()').extract_first()
            item['h'] = tr.xpath('td[7]/text()').extract_first()
            item['double'] = tr.xpath('td[8]/text()').extract_first()
            item['triple'] = tr.xpath('td[9]/text()').extract_first()
            item['hr'] = tr.xpath('td[10]/text()').extract_first()
            item['tb'] = tr.xpath('td[11]/text()').extract_first()
            item['rbi'] = tr.xpath('td[12]/text()').extract_first()
            item['sb'] = tr.xpath('td[13]/text()').extract_first()
            item['cs'] = tr.xpath('td[14]/text()').extract_first()
            item['sh'] = tr.xpath('td[15]/text()').extract_first()
            item['sf'] = tr.xpath('td[16]/text()').extract_first()
            item['bb'] = tr.xpath('td[17]/text()').extract_first()
            item['ibb'] = tr.xpath('td[18]/text()').extract_first()
            item['hbp'] = tr.xpath('td[19]/text()').extract_first()
            item['so'] = tr.xpath('td[20]/text()').extract_first()
            item['dp'] = tr.xpath('td[21]/text()').extract_first()
            item['ba'] = tr.xpath('td[22]/text()').extract_first()
            item['slg'] = tr.xpath('td[23]/text()').extract_first()
            item['obp'] = tr.xpath('td[24]/text()').extract_first()
            yield item
