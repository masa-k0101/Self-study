# -*- coding: utf-8 -*-

spam = ['apples', 'banana', 'tofu', 'cats']

def add_command(self):
    if len(self) <= 0:
        return ''
    if len(self) == 1:
        return self[0]
    return ', '.join(self[:-1]) + ', and ' + self[-1]

s = add_command(spam)
print(s)