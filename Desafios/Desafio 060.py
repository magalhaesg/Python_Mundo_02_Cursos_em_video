# -*- coding: utf-8 -*-
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

resul = int(1)
fat = int(input('Digite um número: '))
fat_ini = fat
lista = []
while fat != 1 and fat != 0:
    lista.append(str(fat))
    if fat == 0:
        fat = 1
    resul = resul * fat
    fat = fat-1
saida = 'x'.join(lista)
print(f'{fat_ini}! = {saida}x1 = {resul}')

