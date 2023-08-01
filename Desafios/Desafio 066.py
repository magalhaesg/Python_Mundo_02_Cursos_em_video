# -*- coding: utf-8 -*-
"""
Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar 999,
que é a condição de parada (flag).
No final, mostre quantos números foram digitados
e qual foi a acc entre eles (desconsiderando o flag)
"""
cont = 0
soma = 0
while True:
    v = int(input('Digite um valor (use 999 para parar o programa.): '))
    if v == 999:
        break
    cont += 1
    soma += v
print(f'A soma dos {cont} valores equivale a {soma}.')
