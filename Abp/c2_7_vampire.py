# -*- coding: utf-8 -*-

print('What is your name?')     # 名前を尋ねる
name = input()
if name == 'Alice':
    print('Alice, long time no see')
else:
    print('Hi,' + name)

print('What is your age?')      # 年齢を尋ねる
age = input()
if  int(age) < 12:
    print('Aliceじゃないね、お嬢ちゃん')
elif int(age) > 2000:
    print('Aliceはお前のような不死身ではない、吸血鬼め')
elif int(age) > 100:
    print('Aliceじゃないね、お婆ちゃん')