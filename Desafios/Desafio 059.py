# -*- coding: utf-8 -*-
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.
import time
import os
a = int(0)
menu = 0
print('Realizador de operações matemáticas\n')
while menu != 5:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    menu = 0
    while menu != 4 and menu != 5:
        menu = int(input(
            'Selecione uma opção válida:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nOpção selecionada: '))
        os.system('cls')
        if menu == 1:
            print(f'A soma entre {a} e {b} é: {a+b}')
        elif menu == 2:
            print(f'A multiplicação entre {a} e {b} é: {a*b}')
        elif menu == 3:
            if a > b:
                print(f'{a} é maior que {b}')
            elif a < b:
                print(f'{b} é maior que {a}')
            else:
                print('Os números são iguais.')
        elif menu == 4:
            print('Reiniciando...')
            time.sleep(2)
        elif menu == 5:
            print('Encerrando...')
            time.sleep(2)
        else:
            print('Digite uma opção válida.')
