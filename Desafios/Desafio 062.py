# -*- coding: utf-8 -*-
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que não quer mais mostrar os termos.

n = int(input('Digite o primeiro termo: '))
a1 = n
r = int(input('Digite uma razão: '))
cont = 0
lim = 10
resp = ''

while not resp == 'N':
    while cont != lim:
        cont += 1
        print(f'a{cont} = {a1 + (cont - 1) * r}', end=' -> ')
    print('Pausa da PA')
    resp = input('Deseja mostrar mais termos? [S/N]').upper()
    if resp == 'S':
        lim += 10
    elif resp == 'N':
        print('Programa finalizado.')
        break
    else:
        print('Opção inválida.')

