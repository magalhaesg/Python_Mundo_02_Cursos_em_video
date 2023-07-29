# -*- coding: utf-8 -*-
# Refazer o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

#an = a1 + (n - 1) * r

#"an" é o "n-ésimo" termo da P.A.
#"a1" é o primeiro termo da P.A.
#"r" é a razão da P.A.
#"n" é o número do termo que você deseja encontrar.

n = int(input('Digite o primeiro termo: '))
a1 = n
r = int(input('Digite uma razão: '))
cont = 0

while cont != 10:
    cont += 1
    print(f'a{cont} = {a1 + (cont - 1) * r}', end=' >>> ')
print('Fim da PA')
