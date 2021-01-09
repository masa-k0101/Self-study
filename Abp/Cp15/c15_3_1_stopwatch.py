#! python3
# -*- coding: utf-8 -*-

import time

# プログラムの説明を表示する
print('ENterを押すと開始します。Enterを押せば経過時間を表示します。Ctrl-Cで終了します')
input()         # Enterを押すと開始
print('スタート')
start_time = time.time()    # プログラムと最初のラップの開始時間
last_time = start_time
lap_num = 1

# TODO: ラップを計測する