# -*- coding: utf-8 -*-
''' Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
'''

cont = 1
while True:
    print('(Digite qualquer número negativo para encerrar o programa.)')
    t = int(input('Digite o número da tabuada que deseja ver: '))
    print('--------------------------------------')
    while cont < 11:
        if t < 0:
            print('Tabuada encerrada. Tenha um bom dia!')
            break
        print(f'{t} x {cont} = {t*cont}')
        cont += 1
    cont = 1
    print('--------------------------------------')