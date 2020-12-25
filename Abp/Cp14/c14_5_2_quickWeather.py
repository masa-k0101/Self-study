# -*- coding: utf-8 -*-

#! python3
# quickWeather.py - コマンドラインに指定した地名の天気予報を表示する

import json, requests, sys

# コマンドライン引数から地名を組み立てる
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# openweathermap.orgから所得したAPIキーを定義しておく
APPID = '01234567890123456789012345678901' 

# OpenWeatherMap.orgからJSONデータをダウンロードする
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&cnt=3&appid={}'.format(location, APPID)
responce = requests.get(url)
responce.raise_for_status()

# TODO: # JSONデータからPython変数に読み込む