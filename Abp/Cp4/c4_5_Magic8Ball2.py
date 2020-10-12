# -*- coding: utf-8 -*-

import random

message = ['確かにそうだ',
           '間違いなくそうだ',
           'はい',
           'うーん、もう一度やってみて',
           'あとでもう一度聞いてみて',
           '集中してもう一度聞いてみて',
           '私の答えはノーです',
           '見通しはそれほど良くない',
           'とても疑わしい']

print(message[random.randint(0, len(message) - 1)])