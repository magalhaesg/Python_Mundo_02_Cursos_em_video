# -*- coding: utf-8 -*-
# Faça um programa que leia um número e diga se ele é ou não um número primo.
import os
num = int(input('Digite um número: '))
os.system('cls')
if num == 2 or num == 3 or num == 5 or num == 7:
    print('\033[32m'f'{num} É primo' + '\033[0;0m')
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print('\033[31m'+f'{num} Não é primo'+'\033[0;0m')
else:
    print('\033[32m'f'{num} É primo'+'\033[0;0m')
for i in range(1, num+1):
    if i == 2 or i == 3 or i == 5 or i == 7:
        print('\033[32m'+f'{i}'+'\033[0;0m', end=' ')
    elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print('\033[31m'+f'{i}'+'\033[0;0m', end=' ')
    else:
        print('\033[32m'+f'{i}'+'\033[0;0m', end=' ')

print('\nOs números escritos em '+'\033[31m'+'VERMELHO '+'\033[0;0m'+'correspondem aos não primos')
print('Os números escritos em'+'\33[32m'+' VERDE '+'\33[0;0m'+'correspondem aos primos')
