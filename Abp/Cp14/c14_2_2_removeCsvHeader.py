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

    # CSVファイルを読み込む(最初の行をスキップする)
    csv_rows = []
    csv_file_obj= open(csv_filename)
    reader_obj = csv.reader(csv_file_obj)
    for row in reader_obj:
        if reader_obj.line_num == 1:
            continue    # 最初の行をスキップする
        csv_rows.append(row)
    csv_file_obj.close()

    # TODO: CSVファイルを書き出す