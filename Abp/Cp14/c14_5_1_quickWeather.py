# -*- coding: utf-8 -*-

#! python3
# quickWeather.py - コマンドラインに指定した地名の天気予報を表示する

import json, requests, sys

# コマンドライン引数から地名を組み立てる
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# TODO: # OpenWeatherMap.orgからJSONデータをダウンロードする

# TODO: # JSONデータからPython変数に読み込む