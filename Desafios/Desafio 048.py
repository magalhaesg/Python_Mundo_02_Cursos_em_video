# -*- coding: utf-8 -*-
# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo da 1 até 5OO.
soma = 0
for i in range(0, 500, 3):
    if i <= 500 and i % 2 == 1:
        soma += i
        print(f'{i}')
print(soma)
