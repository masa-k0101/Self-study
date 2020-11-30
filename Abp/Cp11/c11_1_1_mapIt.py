# -*- coding: utf-8 -*-

#! python3
# mapIt.py - コマンドラインやクリップボードに指定した住所の地図を開く

import webbrowser, sys
if len(sys.argv) > 1:
    # コマンドラインから住所を取得する
    address = ' '.join(sys.argv[1:])

# TODO: クリップボードから住所を取得する
