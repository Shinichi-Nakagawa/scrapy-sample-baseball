# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class BatterItem(Item):
    year = Field()
    team = Field()
    name = Field()
    games = Field()
    pa = Field()
    ab = Field()
    r = Field()
    h = Field()
    double = Field()
    triple = Field()
    hr = Field()
    tb = Field()
    rbi = Field()
    sb = Field()
    cs = Field()
    sh = Field()
    sf = Field()
    bb = Field()
    ibb = Field()
    hbp = Field()
    so = Field()
    dp = Field()
    ba = Field()
    slg = Field()
    obp = Field()


