# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from scrapy.exceptions import DropItem


class BaseballPipeline(object):

    CREATE_TABLE_BATTER ="""
    CREATE TABLE batter (
      id integer primary key,
      year integer,
      name text ,
      team text ,
      games integer ,
      pa integer ,
      ab integer ,
      r integer ,
      h integer ,
      double integer ,
      triple integer ,
      hr integer ,
      tb integer ,
      rbi integer ,
      so integer ,
      bb integer ,
      ibb integer ,
      hbp integer ,
      sh integer ,
      sf integer ,
      sb integer ,
      cs integer ,
      dp integer ,
      ba real ,
      slg real ,
      obp real,
      create_date date,
      update_date date
    ) 
    """

    INSERT_BATTER = """
    insert or ignore into batter(
    year, 
    name, 
    team, 
    games, 
    pa, 
    ab, 
    r, 
    h, 
    double, 
    triple, 
    hr, 
    tb, 
    rbi, 
    so, 
    bb, 
    ibb, 
    hbp, 
    sh, 
    sf,
    sb,
    cs,
    dp,
    ba,
    slg,
    obp,
    create_date,
    update_date
    ) 
    values(
    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, 
    datetime('now', 'localtime'), 
    datetime('now', 'localtime')
    )
    """

    def __init__(self):
        self.conn = sqlite3.connect('baseball.db')
        if self.conn.execute("select count(*) from sqlite_master where name='batter'").fetchone()[0] == 0:
            self.conn.execute(self.CREATE_TABLE_BATTER)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if spider.name == 'batter':
            self.conn.execute(self.INSERT_BATTER,(
                item['year'], item['name'], item['team'], item['games'], item['pa'], item['ab'], item['r'], item['h'],
                item['double'], item['triple'], item['hr'], item['tb'], item['rbi'], item['so'], item['bb'],
                item['ibb'], item['hbp'], item['sh'], item['sf'], item['sb'], item['cs'], item['dp'], item['ba'],
                item['slg'], item['obp'],
            ))
        elif spider.name == 'pitcher':
            # TODO これから作る
            pass
        else:
            raise DropItem('spider not found')
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
