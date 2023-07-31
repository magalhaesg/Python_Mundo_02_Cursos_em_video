# -*- coding: utf-8 -*-
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 1, 1, 2, 3, 5, 8

Fn = 0
Fn1 = 1
Fn2 = 0
cont = 0
p_linha = 15
elementos = int(input('Digite o número de termos da Sequência de Fibonacci que deseja visualizar: '))

while not elementos == cont:
    Fn = Fn1 + Fn2
    print(Fn, end=", ")
    Fn1 = Fn2
    Fn2 = Fn
    cont += 1
    if cont == p_linha:
        print('')
        p_linha += 10
print('Fim do requerimento.')
