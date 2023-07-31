# -*- coding: utf-8 -*-
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores, o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

parar = 'N'
maior = menor = 0
cont = 0
soma = 0
while parar != 'S':
    if parar == 'N':
        num = int(input('Digite um número: '))
        if num > maior:
            maior = num
        if menor == 0:
            menor = maior
        if num < menor:
            menor = num
        soma += num
        cont += 1
        parar = input('Deseja parar? [S/N]: ').upper()
    elif parar == 'S':
        break
    else:
        print('Comando inválido')
        break
print(f'Média: {(soma/cont)} / Maior: {maior} / Menor: {menor}')
