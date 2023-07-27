# -*- coding: utf-8 -*-
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: Apos a sopa

#usando slice para inverter texto
def inverter_txt(txt_invertido):
    return txt_invertido[::-1] # estudar por "anotação de slice"

#usando replace para remover espaço entre texto
def remove(txt_unido):
    return txt_unido.replace(" ","")
    #PODERIA USAR .strip() também

txt = input(str('Digite seu texto para checarmos se é palíndromo: ')).upper()

if remove(txt) == (inverter_txt(remove(txt))):
    print('É um palíndromo')
    print('\33[32m' + f'{remove(txt)}' ' = ' f'{(inverter_txt(remove(txt)))}')
else:
    print('Não é um palíndromo')
    print('\33[31m' + f'{remove(txt)}' ' ≠ ' f'{(inverter_txt(remove(txt)))}')

