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
      bat text ,
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

    CREATE_TABLE_PITCHER ="""
    CREATE TABLE pitcher (
      id integer primary key,
      year integer,
      name text ,
      team text ,
      throw text ,
      games integer ,
      w integer ,
      l integer ,
      sv integer ,
      hld integer ,
      hp integer ,
      cg integer ,
      sho integer ,
      non_bb integer ,
      w_per real ,
      bf integer ,
      ip real ,
      h integer ,
      hr integer ,
      bb integer ,
      ibb integer ,
      hbp integer ,
      so integer ,
      wp integer ,
      bk integer ,
      r integer ,
      er integer ,
      era real ,
      create_date date,
      update_date date
    ) 
    """

    INSERT_BATTER = """
    insert into batter(
    year, 
    name, 
    team, 
    bat, 
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
    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, 
    datetime('now', 'localtime'), 
    datetime('now', 'localtime')
    )
    """

    INSERT_PITCHER = """
    insert into pitcher(
    year, 
    name, 
    team, 
    throw, 
    games, 
    w, 
    l, 
    sv, 
    hld, 
    hp, 
    cg, 
    sho, 
    non_bb, 
    w_per, 
    bf, 
    ip, 
    h, 
    hr, 
    bb, 
    ibb, 
    hbp, 
    so,
    wp,
    bk,
    r,
    er,
    era,
    create_date,
    update_date
    ) 
    values(
    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, 
    datetime('now', 'localtime'), 
    datetime('now', 'localtime')
    )
    """

    DATABASE_NAME = 'baseball.db'
    conn = None

    def __init__(self):
        """
        Tableの有無をチェック,無ければ作る
        """
        conn = sqlite3.connect(self.DATABASE_NAME)
        if conn.execute("select count(*) from sqlite_master where name='batter'").fetchone()[0] == 0:
            conn.execute(self.CREATE_TABLE_BATTER)
        if conn.execute("select count(*) from sqlite_master where name='pitcher'").fetchone()[0] == 0:
            conn.execute(self.CREATE_TABLE_PITCHER)
        conn.close()

    def open_spider(self, spider):
        """
        初期処理(DBを開く)
        :param spider: ScrapyのSpiderオブジェクト
        """
        self.conn = sqlite3.connect(self.DATABASE_NAME)

    def process_item(self, item, spider):
        """
        成績をSQLite3に保存
        :param item: Itemの名前
        :param spider: ScrapyのSpiderオブジェクト
        :return: Item
        """
        # Spiderの名前で投入先のテーブルを判断
        if spider.name == 'batter':
            # 打者成績
            self.conn.execute(self.INSERT_BATTER,(
                item['year'], item['name'], item['team'], item['bat'], item['games'], item['pa'], item['ab'], item['r'],
                item['h'], item['double'], item['triple'], item['hr'], item['tb'], item['rbi'], item['so'], item['bb'],
                item['ibb'], item['hbp'], item['sh'], item['sf'], item['sb'], item['cs'], item['dp'], item['ba'],
                item['slg'], item['obp'],
            ))
        elif spider.name == 'pitcher':
            # 投手成績
            self.conn.execute(self.INSERT_PITCHER,(
                item['year'], item['name'], item['team'], item['throw'], item['games'], item['w'], item['l'],
                item['sv'], item['hld'], item['hp'], item['cg'], item['sho'], item['non_bb'], item['w_per'], item['bf'],
                item['ip'], item['h'], item['hr'], item['bb'], item['ibb'], item['hbp'], item['so'], item['wp'],
                item['bk'], item['r'], item['er'], item['era'],
            ))
        else:
            raise DropItem('spider not found')
        self.conn.commit()
        return item

    def close_spider(self, spider):
        """
        終了処理(DBを閉じる)
        :param spider: ScrapyのSpiderオブジェクト
        """
        self.conn.close()
