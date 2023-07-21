# -*- coding: utf-8 -*-
# Faça um programa que leia um número e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print('Não é primo')
else:
    print('É primo')
