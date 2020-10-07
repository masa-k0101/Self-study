# -*- coding: utf-8 -*-

def collatz(number):
    if number % 2 == 0:
        return number / 2
    elif number % 2 == 1:
        return 3*number + 1

print('整数を入力してください')
number = int(input())
print('Calicurate Clollatz = ')

while number != 1:
    print(int(number))
    number = collatz(number)
print(1)