# -*- coding: utf-8 -*-
# Refaça o desafio 09. Mostrar a tabuada de um número que o usuário escolher, utilizando um laço for.

n = int(input('Digite o número da tabuada que deseja visualizar: '))
for i in range(0, 11):
    print(f'{n} x {i} = {n * i}')

