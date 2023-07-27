# -*- coding: utf-8 -*-
# Desenvolva um programa que leia o primeiro termo e a razão de uma P.A. (Progressão Aritmética). No final, mostre os 10 primeiros termos dessa progressão.

#an = a1 + (n - 1) * r

#"an" é o "n-ésimo" termo da P.A.
#"a1" é o primeiro termo da P.A.
#"r" é a razão da P.A.
#"n" é o número do termo que você deseja encontrar.

n = int(input('Digite o primeiro termo: '))
a1 = n
r = int(input('Digite uma razão: '))

#print(f'a{n} = {a1 + (n - 1) * r}')
for i in range(1, 11):
    print(f'a{i} = {a1 + (i - 1) * r}', end=' >>> ')
print('Fim')
