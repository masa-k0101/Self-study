# -*- coding: utf-8 -*-

#! python3
# renameDates.py - 米国式日付MM-DD-YYのファイル名を欧州式DD-MM-YYに置き換える

import shutil, os, re

# 米国式日付のファイル名にマッチする正規表現を作る

date_pattarn = re.compile(r"""^(.*?)
((o|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$
""", re.VERBOSE)

# カレントディレクトリの全ファイルをループする
for amer_filename in os.listdir('.'):
    mo = date_pattarn.search(amer_filename)

    # 日付のないファイルをスキップする
    if mo == None:
        continue

    # ファイル名を部分分解する
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

# 欧州式の日付のファイル名を作る
euro_filename = before_part + day_part + '-' + month_part + year_part + after_part

# ファイル名を変更する
print('Renaming "{}" to "{}"...'.format(amer_filename,euro_filename))
#shutil.move(amer_filename, euro_filename)