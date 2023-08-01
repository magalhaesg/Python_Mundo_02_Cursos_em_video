# -*- coding: utf-8 -*-
'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
'''
total = 0
prod1000 = 0
pmaisb = 0
while True:
    prod = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))
    total += preco
    if preco >= 1000:
        prod1000 += 1
    if pmaisb == 0:
        pmaisb = preco
    elif pmaisb > preco:
        n_pmaisb = prod
    cparada = input('Deseja continuar? [S/N] ').upper()
    while cparada != 'S' and cparada != 'N':
        cparada = input('Deseja continuar? [S/N] ').upper()
    if cparada == 'N':
        print(f'Total gasto na compra: {total}')
        print(f'Quantos produtos custam mais de R$1000: {prod1000}')
        print(f'Qual o nome do produto mais barato: {n_pmaisb}')
        break
