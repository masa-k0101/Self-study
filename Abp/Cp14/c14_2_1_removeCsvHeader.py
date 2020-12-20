# -*- coding: utf-8 -*-

#! python3
# removeCsvHeader.py - カレントディレクトリの全CSVファイルから見出しを削除する

import csv, os

os.makedirs('headerRemoves', exist_ok=True)

# カレントディレクトリの全ファイルをループする
for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'):
        continue # CSVファイルでなければスキップ

    print('見出し削除中' + csv_filename + '...')

    # TODO: CSVファイルを読み込む(最初の行をスキップする)

    # TODO: CSVファイルを書き出す
