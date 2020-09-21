# -*- coding: utf-8 -*-

print('What is your name?')     # 名前を尋ねる
name = input()
print('What is your age?')      # 年齢を尋ねる
age = input()

if name == 'Alice':
    print('Alice, long time no see')
elif  int(age) < 12:
    print('Aliceじゃないね、お嬢ちゃん')
else:
    print('君はAliceでも子供でもないね')
