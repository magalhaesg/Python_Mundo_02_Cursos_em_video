# -*- coding: utf-8 -*-
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número de 1 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
import time
comp = ''
hum = 0
cont = 0
# hum = int(input('Digite um número entre 1 e 10: '))
while hum != comp:
    comp = random.randint(1, 10)
    hum = int(input('Digite um número entre 1 e 10: '))
    cont += 1
    if hum < 1 or hum > 10:
        print('Por favor, digite um número entre 1 e 10.')
    elif hum != comp:
        print('Tente novamente')
        print(f'Você: {hum} – Computador: {comp}')
    elif hum == comp:
        time.sleep(2)
        print(f'Você: {hum} – Computador: {comp}')
        print('Os números combinam, você conseguiu!')
        print(f'Tentativas até conseguir: {cont}')
