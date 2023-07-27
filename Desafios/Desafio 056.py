# -*- coding: utf-8 -*-
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# * A média da idade do grupo.
# * Qual é o nome do homem mais velho.
# * Quantas mulheres têm menos de 20 anos.

pessoas = []
soma = int(0)
homem_old = ""
jovem_f = 0
for i in range(0, 4):
    print(f' {i+1}ª Pessoa '.center(30,'-'))
    nome = str(input('Digite seu nome: ')).capitalize()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): ')).upper()
    pessoas.append([nome, idade, sexo])

for g in range(0,4):
    soma += pessoas[g][1]
    if pessoas[g][2] == 'M' and pessoas[g][1] > pessoas[g-1][1]:
        homem_old = pessoas[g][0]
    elif pessoas[g][2] == 'F' and pessoas[g][1] < 20:
        jovem_f += 1

print(f'''
A média da idade do grupo é de {soma/4} anos;\n
Qual é o nome do homem mais velho: {homem_old};\n
Quantas mulheres têm menos de 20 anos: {jovem_f}.
''')