# -*- coding: utf-8 -*-

import sys

while True:
    print('終了するにはexitと入力してください')
    responce = input()
    if responce == 'exit':
        sys.exit()
    print(responce + 'と入力されました')