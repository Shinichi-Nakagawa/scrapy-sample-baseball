# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class BatterItem(Item):
    year = Field()      # 年度
    team = Field()      # チーム
    name = Field()      # 名前
    games = Field()     # 試合数
    pa = Field()        # 打席数
    ab = Field()        # 打数
    r = Field()         # 得点
    h = Field()         # 安打
    double = Field()    # 二塁打
    triple = Field()    # 三塁打
    hr = Field()        # 本塁打
    tb = Field()        # 塁打
    rbi = Field()       # 打点
    sb = Field()        # 盗塁
    cs = Field()        # 盗塁死
    sh = Field()        # 犠打(バント)
    sf = Field()        # 犠飛(犠牲フライ)
    bb = Field()        # 四球
    ibb = Field()       # 故意四球(敬遠)
    hbp = Field()       # 死球(デットボール)
    so = Field()        # 三振
    dp = Field()        # 併殺
    ba = Field()        # 打率
    slg = Field()       # 長打率
    obp = Field()       # 出塁率
