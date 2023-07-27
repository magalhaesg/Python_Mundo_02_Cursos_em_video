# -*- coding: utf-8 -*-
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []
# cont1 = 0
# cont2 = 150
for i in range(0,5):
    peso = float(input(f'Digite o {i+1}º peso: '))
    pesos.append(peso)
maior = max(pesos) #usei as funções max e min para testar.
menor = min(pesos)
# for g in range(0,5):
#     if pesos[g] > cont1:
#         maior = float(pesos[g])
#         cont1 = pesos[g]
#     if pesos[g] < cont2:
#         menor = float(pesos[g])
#         cont2 = pesos[g]
print(pesos)
print(f'O maior peso é {maior:.2f}Kg')
print(f'O menor peso é {menor:.2f}Kg')

