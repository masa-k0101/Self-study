# -*- coding: utf-8 -*-

#! python3
# downloadXkcdy.py - XKCDコミックを一つずつダウンロードする

import requests, os, bs4

url = 'http://xkcd.com'             # 開始URL
os.makedirs('xkcd', exist_ok=True)  # ./xkcdに保存する

while not url.endwidth('#'):
    # ページをダウンロードする
    print('ページをダウンロード中{}...'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulStoneSoup(res.text)

    # TODO: # コミック画像のURLを見つける

    # TODO: # 画像をダウンロードする

    # TODO: # 画像を./xkcdに保存する

    # TODO: # prevボタンのURLを取得する

print('完了')