# -*- coding: utf-8 -*-

def spam(divide_py):
    try:
        return 42 / divide_py
    except ZeroDivisionError:
        print('エラー:不正な引数です')
        
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

