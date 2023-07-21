# -*- coding: utf-8 -*-
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

vet_ano = [ ]
cont = 0
for i in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    vet_ano.append(ano)

for ano in vet_ano:
    if 2005 < ano:
        cont += 1
print(f'A quantidade de pessoas que ainda não atingiram a maioridade: {cont}')
