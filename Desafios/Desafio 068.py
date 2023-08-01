# -*- coding: utf-8 -*-
''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou,
no final do jogo.'''
import random

cont = 0
while True:
    compN = random.randint(0, 10)
    userN = int(input('Diga um valor: '))
    userC = ' '
    while userC not in 'PI':
        userC = input('Par ou Impar [P/I]: ').upper()
    resultado = (userN + compN) % 2
    if userC == 'P' or userC == 'PAR':
        if resultado == 0:
            print('Vitória!')
            cont += 1
            decisao = 'PAR'
            print(f'Escolha: Computador: {compN} | Usuário: {userN}\nGanhou quem escolheu {decisao}')
        else:
            decisao = 'IMPAR'
            print(f'Infelizmente você perdeu :(\nVocê teve um total de {cont} vitórias consecutivas.')
            print(f'Escolha: Computador: {compN} | Usuário: {userN}\nGanhou quem escolheu {decisao}')
            break
    elif userC == 'I' or userC == 'IMPAR':
        if resultado == 1:
            print('Vitória!')
            cont += 1
            decisao = 'IMPAR'
            print(f'Escolha: Computador: {compN} | Usuário: {userN}\nGanhou quem escolheu {decisao}')
        else:
            decisao = 'PAR'
            print(f'Infelizmente você perdeu :(\nVocê teve um total de {cont} vitórias consecutivas.')
            print(f'Escolha: Computador: {compN} | Usuário: {userN}\nGanhou quem escolheu {decisao}')
            break
