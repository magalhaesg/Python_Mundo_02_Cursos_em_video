# -*- coding: utf-8 -*-
''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos'''
p18 = 0
mas = 0
m20 = 0
while True:
        print(''.center(40, '-'))
        print('CADASTRO DE PESSOAS'.center(40,' '))
        print(''.center(40, '-'))
        idade = int(input('Idade: '))
        sexo = ' '
        while sexo != 'F' and sexo != 'M':
                sexo = input('Sexo: [M/F] ').upper()[0]
        print(''.center(40, '-'))
        increment = ''
        while increment != 'N' and increment != 'S':
                increment = input('Deseja cadastrar mais uma pessoa? [S/N] ').upper()[0]
        print(''.center(40, '-'))
        if idade >= 18:
                p18 += 1
        if sexo == 'M':
                mas += 1
        if sexo == 'F' and idade <= 20:
                m20 += 1
        if increment == 'N' or increment == 'Não':
                print(' FIM DO PROGRAMA '.center(40, '-'))
                print(f'Total de pessoas acima de 18: {p18}')
                print(f'Total de homens cadastrados: {mas}')
                print(f'Total de mulheres com menos de 20: {m20}')
                break
