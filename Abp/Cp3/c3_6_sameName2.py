# -*- coding: utf-8 -*-

def spam():
    global eggs
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)         # global を表示