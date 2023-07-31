# -*- coding: utf-8 -*-
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até obter um valor correto.
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite seu sexo [M/F]: ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Tente novamente.')
    else:
        print('Entrada registrada!')

