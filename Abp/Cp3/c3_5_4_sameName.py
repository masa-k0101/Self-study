# -*- coding: utf-8 -*-

def spam():
    eggs = 'spam local'
    print(eggs)     # spam localを表示

def bacon():
    eggs = 'bacon local'
    print(eggs)     # bacon localを表示
    spam()
    print(eggs)     # bacon localを表示
    
eggs = 'global'
bacon()
print(eggs)         # global を表示