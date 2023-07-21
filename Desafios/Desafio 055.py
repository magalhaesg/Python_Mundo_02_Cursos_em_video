# -*- coding: utf-8 -*-
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []
maior = 0
menor = 0
for i in range(0,5):
    peso = float(input(f'Digite o {i+1}º peso: '))
    pesos.append(peso)

for g in range(0,5):
    if pesos[g] > pesos[g-1]:
        maior = float(pesos[g])
    if pesos[g] < pesos[g-1]:
        menor = float(pesos[g])
print(pesos)
print(f'O maior peso é {maior:.2f} Kg')
print(f'O menor peso é {menor:.2f} Kg')

