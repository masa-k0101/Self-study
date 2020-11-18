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

# TODO: カレントディレクトリの全ファイルをループする

# TODO: 日付のないファイルをスキップする

# TODO: ファイル名を部分分解する

# TODO: 欧州式の日付のファイル名を作る

# TODO: ファイル名を変更する
