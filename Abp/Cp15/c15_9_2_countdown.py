#! python3
# -*- coding: utf-8 -*-

import time, subprocess

time_left = 60
while time_left > 0:
    print(time_left, end='')
    time.sleep(1)
    time_left = time_left - 1

# カウントダウン後に音声ファイルを再生する
subprocess.Popen(['start','alarm.wav'], shell=True)