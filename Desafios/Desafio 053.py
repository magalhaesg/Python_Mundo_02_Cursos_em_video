# -*- coding: utf-8 -*-
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: Apos a sopa

def inverter_txt(txt_invertido):
    return txt_invertido[::-1] # estudar por "anotação de slice"


txt = input(str('Digite seu texto para checarmos se é palíndromo: ')).upper()

print(inverter_txt(txt))

if txt == inverter_txt(txt):
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

