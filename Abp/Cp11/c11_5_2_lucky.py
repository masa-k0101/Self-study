# -*- coding: utf-8 -*-

#! python3
# lucky.py - google検索結果をいくつか開く

import requests, sys, webbrowser, bs4
print('Googling...')    # Googleページをダウンロード中にテキストを表示
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# 上位の検索結果のリンクを取得する
soup = bs4.BeautifulSoup(res.text)
link_elems = soup.select('.r a')

# TODO: 各結果をブラウザで開く