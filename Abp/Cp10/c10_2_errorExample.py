# -*- coding: utf-8 -*-

#! python3

def spam():
    bacon()

def bacon():
    raise Exception('これはエラーメッセージです')

spam()