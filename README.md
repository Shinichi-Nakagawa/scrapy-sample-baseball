# 日本プロ野球の成績を取得してDBに格納するサンプル

## 何ができるのか

* 日本プロ野球機構(NPB)の[ホームページ](http://npb.jp/)から12球団選手の打撃・投球成績を取得
* 取得したデータをDB(SQLite3)に保存

## 動作環境

作者(shinyorke)の動作環境より.

* gitクライアント(何でもOK)
    * ソースコードを取得するために使う
    * 面倒くさい方は直接ダウンロードしてもらってもOK
* Python 3系の最新Ver
    * 3.6以上を推奨
    * 試してはいませんが,3.3.x以上なら動くと思う
    * 2.7.x系は未検証ですが多分動くと思います(がオススメしません&対応する気は無いです)
* Scrapyのインストールが必要(後述)
    * 1.4.0で検証(作成時点の最新バージョン)
* MacOS Sierra(10.12.6)
    * 上記のPythonバージョンおよびScrapyバージョンであればOS関係なく動くハズ

## セットアップ

### 1. リポジトリをclone or ダウンロードする

#### クローンの場合

```bash
$ git clone https://github.com/Shinichi-Nakagawa/scrapy-sample-baseball.git
```

#### ダウンロードの場合

```bash
$ wget https://github.com/Shinichi-Nakagawa/scrapy-sample-baseball/archive/master.zip
$ unzip master.zip
```

### 2. Pythonをインストール

* [ダウンロードサイト(公式)](https://www.python.org/downloads/)
* お使いのOS・プラットフォームに合わせてお使いください
* (繰り返しになりますが)Python 3.6以上が推奨です！

### 3. Scrapyをインストール

```bash
$ pip install scrapy
```

## 使い方

### 1. ディレクトリに移動

Scrapyのエンドポイントにcdします.

```bash
$ cd scrapy-sample-baseball/baseball
```

なお,ダウンロードで手に入れた人は最初のディレクトリ名が変わるので注意

```bash
$ cd scrapy-sample-baseball-master/baseball
```

### 2. 打者成績を取得

scrapyのコマンドで取得します.

初回実施の時はDBファイル(baseball.db)が生成され,同時にSchemeも作成されます.

```bash
$ scrapy crawl batter -a year=2017 -a league=1
```

### 3. 投手成績を取得

同じく,scrapyのコマンドで取得します.

初回実施の時はDBファイル(baseball.db)が生成され,同時にSchemeも作成されます.

```bash
$ scrapy crawl pitcher -a year=2017 -a league=1
```

### [TIPS]オプション引数(打者・投手共通)

いずれも省略可能,省略時はdefault値が使われます.

#### year(default:2017)

取得する成績年度

#### league(default:1)

1軍成績もしくは2軍成績

2軍の場合は

```bash
$ scrapy crawl {batter|pitcher} -a year=2017 -a league=2
```

これで取得可能です.

## データについて

### 構造

[baseball/baseball/item.py](https://github.com/Shinichi-Nakagawa/scrapy-sample-baseball/blob/master/baseball/baseball/items.py)に乗っているカラムと解説が全てです.

カラムの名称は一般的に使われる野球英語の略称を用いています.

詳細は各Itemのコメントを参照ください.

### Table Scheme

[baseball/baseball/pipelines.py](https://github.com/Shinichi-Nakagawa/scrapy-sample-baseball/blob/master/baseball/baseball/pipelines.py)にCreate Table文があります.

カラムの意味と解説はItemと全く同じです(id値とcreate_date/update_dateがあるぐらいの違い)

なお,indexは全く貼っていないので必要な方は随時書き換えてもらえると.