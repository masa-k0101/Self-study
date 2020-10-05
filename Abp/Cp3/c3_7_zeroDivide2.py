# -*- coding: utf-8 -*-

def spam(divide_py):
    return 42 / divide_py

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('エラー:不正な引数です')