# -*- coding: utf-8 -*-
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

vet_ano = [ ]
cont = 0
for i in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    vet_ano.append(ano)

for ano in vet_ano:
    if 2005 < ano:
        cont += 1
print(f'A quantidade de pessoas que ainda não atingiram a maioridade: {cont}\n'
    f'Pessoas que já atingiram a maior idade: {7 - cont}')


