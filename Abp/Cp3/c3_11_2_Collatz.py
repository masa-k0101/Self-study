# -*- coding: utf-8 -*-

def collatz(number):
    if number % 2 == 0:
        return number / 2
    elif number % 2 == 1:
        return 3*number + 1

while True:
  try:
    print('整数を入力してください：')
    number = int(input())
    break
  except ValueError:
    print('エラー：整数値を入力してください。')

print('Calicurate Clollatz = ')

while number != 1:
    print(int(number))
    number = collatz(number)
print(1)