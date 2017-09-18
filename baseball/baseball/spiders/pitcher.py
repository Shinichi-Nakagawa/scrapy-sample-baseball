# -*- coding: utf-8 -*-
import scrapy

from baseball.items import PitcherItem
from baseball.spiders import TEAMS, LEAGUE_TOP, THROW_RIGHT, THROW_LEFT
from baseball.spiders import BaseballSpidersUtil as Util


class PitcherSpider(scrapy.Spider):
    name = 'pitcher'
    allowed_domains = ['npb.jp']
    allowed_domains = ['npb.jp']
    URL_TEMPLATE = 'http://npb.jp/bis/{year}/stats/idp{league}_{team}.html'

    def __init__(self, year=2017, league=LEAGUE_TOP):
        """
        初期処理(年度とURLの設定)
        :param year: シーズン年
        :param league: 1 or 2(1軍もしくは2軍)
        """
        self.year = year
        # URLリスト(12球団)
        self.start_urls = [self.URL_TEMPLATE.format(year=year, league=league, team=t) for t in TEAMS]

    def parse(self, response):
        """
        選手一人分の投球成績
        :param response: 取得した結果(Response)
        :return: 投球成績
        """
        for tr in response.xpath('//*[@id="stdivmaintbl"]/table').xpath('tr'):
            item = PitcherItem()
            if not tr.xpath('td[3]/text()').extract_first():
                continue
            item['year'] = self.year
            item['team'] = Util.get_team(response.url)
            item['name'] = Util.get_text(tr.xpath('td[2]/text()').extract_first())
            item['throw'] = self._get_throw(Util.get_text(tr.xpath('td[1]/text()').extract_first()))
            item['games'] = Util.text2digit(tr.xpath('td[3]/text()').extract_first(), digit_type=int)
            item['w'] = Util.text2digit(tr.xpath('td[4]/text()').extract_first(), digit_type=int)
            item['l'] = Util.text2digit(tr.xpath('td[5]/text()').extract_first(), digit_type=int)
            item['sv'] = Util.text2digit(tr.xpath('td[6]/text()').extract_first(), digit_type=int)
            item['hld'] = Util.text2digit(tr.xpath('td[7]/text()').extract_first(), digit_type=int)
            item['hp'] = Util.text2digit(tr.xpath('td[8]/text()').extract_first(), digit_type=int)
            item['cg'] = Util.text2digit(tr.xpath('td[9]/text()').extract_first(), digit_type=int)
            item['sho'] = Util.text2digit(tr.xpath('td[10]/text()').extract_first(), digit_type=int)
            item['non_bb'] = Util.text2digit(tr.xpath('td[11]/text()').extract_first(), digit_type=int)
            item['w_per'] = Util.text2digit(tr.xpath('td[12]/text()').extract_first(), digit_type=float)
            item['bf'] = Util.text2digit(tr.xpath('td[13]/text()').extract_first(), digit_type=int)
            # 小数点以下が別のカラムに入ってるのでこういう感じになります
            if tr.xpath('td[15]/text()').extract_first():
                ip = tr.xpath('td[14]/text()').extract_first() + tr.xpath('td[15]/text()').extract_first()
            else:
                ip = tr.xpath('td[14]/text()').extract_first()
            item['ip'] = Util.text2digit(ip, digit_type=float)
            item['h'] = Util.text2digit(tr.xpath('td[16]/text()').extract_first(), digit_type=int)
            item['hr'] = Util.text2digit(tr.xpath('td[17]/text()').extract_first(), digit_type=int)
            item['bb'] = Util.text2digit(tr.xpath('td[18]/text()').extract_first(), digit_type=int)
            item['ibb'] = Util.text2digit(tr.xpath('td[19]/text()').extract_first(), digit_type=int)
            item['hbp'] = Util.text2digit(tr.xpath('td[20]/text()').extract_first(), digit_type=int)
            item['so'] = Util.text2digit(tr.xpath('td[21]/text()').extract_first(), digit_type=int)
            item['wp'] = Util.text2digit(tr.xpath('td[22]/text()').extract_first(), digit_type=int)
            item['bk'] = Util.text2digit(tr.xpath('td[23]/text()').extract_first(), digit_type=int)
            item['r'] = Util.text2digit(tr.xpath('td[24]/text()').extract_first(), digit_type=int)
            item['er'] = Util.text2digit(tr.xpath('td[25]/text()').extract_first(), digit_type=int)
            item['era'] = Util.text2digit(tr.xpath('td[26]/text()').extract_first(), digit_type=float)
            yield item

    def _get_throw(self, text):
        """
        右投げもしくは左投げか
        :param text: テキスト
        :return: 右投げ or 左投げ
        """
        if text == '*':
            return THROW_LEFT
        return THROW_RIGHT
