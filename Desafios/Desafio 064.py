# -*- coding: utf-8 -*-
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = int(0)
soma = 0
cont = 0
print('Contador e somador de números infinito.\nPara parar digite o número 999')
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
        cont += 1
print(f'Soma: {soma} / Contagem {cont}')