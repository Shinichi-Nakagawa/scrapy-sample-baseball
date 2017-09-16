# -*- coding: utf-8 -*-
import scrapy

from baseball.items import BatterItem
from baseball.spiders import TEAMS, LEAGUE_TOP
from baseball.spiders import BaseballSpidersUtil as Util


class BatterSpider(scrapy.Spider):
    name = 'batter'
    allowed_domains = ['npb.jp']
    URL_TEMPLATE = 'http://npb.jp/bis/{year}/stats/idb{league}_{team}.html'

    def __init__(self, year=2017, league=LEAGUE_TOP):
        self.year = year
        self.start_urls = self._get_start_urls(year, league)

    def _get_start_urls(self, year, league):
        return [self.URL_TEMPLATE.format(year=year, league=league, team=t) for t in TEAMS]

    def parse(self, response):
        for tr in response.xpath('//*[@id="stdivmaintbl"]/table').xpath('tr'):
            item = BatterItem()
            item['year'] = self.year
            item['team'] = Util.get_team(response.url)
            item['name'] = Util.get_text(tr.xpath('td[2]/text()').extract_first())
            item['games'] = Util.text2digit(tr.xpath('td[3]/text()').extract_first(), digit_type=int)
            item['pa'] = Util.text2digit(tr.xpath('td[4]/text()').extract_first(), digit_type=int)
            item['ab'] = Util.text2digit(tr.xpath('td[5]/text()').extract_first(), digit_type=int)
            item['r'] = Util.text2digit(tr.xpath('td[6]/text()').extract_first(), digit_type=int)
            item['h'] = Util.text2digit(tr.xpath('td[7]/text()').extract_first(), digit_type=int)
            item['double'] = Util.text2digit(tr.xpath('td[8]/text()').extract_first(), digit_type=int)
            item['triple'] = Util.text2digit(tr.xpath('td[9]/text()').extract_first(), digit_type=int)
            item['hr'] = Util.text2digit(tr.xpath('td[10]/text()').extract_first(), digit_type=int)
            item['tb'] = Util.text2digit(tr.xpath('td[11]/text()').extract_first(), digit_type=int)
            item['rbi'] = Util.text2digit(tr.xpath('td[12]/text()').extract_first(), digit_type=int)
            item['sb'] = Util.text2digit(tr.xpath('td[13]/text()').extract_first(), digit_type=int)
            item['cs'] = Util.text2digit(tr.xpath('td[14]/text()').extract_first(), digit_type=int)
            item['sh'] = Util.text2digit(tr.xpath('td[15]/text()').extract_first(), digit_type=int)
            item['sf'] = Util.text2digit(tr.xpath('td[16]/text()').extract_first(), digit_type=int)
            item['bb'] = Util.text2digit(tr.xpath('td[17]/text()').extract_first(), digit_type=int)
            item['ibb'] = Util.text2digit(tr.xpath('td[18]/text()').extract_first(), digit_type=int)
            item['hbp'] = Util.text2digit(tr.xpath('td[19]/text()').extract_first(), digit_type=int)
            item['so'] = Util.text2digit(tr.xpath('td[20]/text()').extract_first(), digit_type=int)
            item['dp'] = Util.text2digit(tr.xpath('td[21]/text()').extract_first(), digit_type=int)
            item['ba'] = Util.text2digit(tr.xpath('td[22]/text()').extract_first(), digit_type=float)
            item['slg'] = Util.text2digit(tr.xpath('td[23]/text()').extract_first(), digit_type=float)
            item['obp'] = Util.text2digit(tr.xpath('td[24]/text()').extract_first(), digit_type=float)
            yield item
