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

    # コミック画像のURLを見つける
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('コミック画像が見つかりませんでした')
    else:
        comic_url = 'http:' + comic_elem[0].get('src')
        # 画像をダウンロードする
        print('画像をダウンロード中{}...'.format(comic_url))
        res = requests.get(url)
        res.raise_for_status()    

    # TODO: # 画像を./xkcdに保存する

    # TODO: # prevボタンのURLを取得する

print('完了')