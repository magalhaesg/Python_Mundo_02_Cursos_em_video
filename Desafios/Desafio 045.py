# Crie um programa que faça o computador jogar Jokanpô com você.

import random
import time
import os

print('-=' * 20)
print(f'{" " * 15} Jokanpo')
print('Escolha entre Pedra, Papel e Tesoura.')
print('-=' * 20)
jokanpo = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(jokanpo)
input_jogador = input('Digite sua escolha: ')
jogador = input_jogador.capitalize()
while jogador not in jokanpo:
    print('Opção inválida, tente novamente com Pedra, Papel ou Tesoura')
    input_jogador = input('Digite sua escolha: ').capitalize()
os.system("cls") #comando limpa tela
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(2)
os.system("cls") #comando limpa tela
print(f'{" RESULTADO ".center(40, "=")}')
largura = 10
# situacao pedra ----------------------------------------------
if jogador == 'Pedra' and computador == 'Papel':
    print(f'Computador venceu'.center(40))
    print(f'Computador: {computador} | Jogador: {jogador}')
elif jogador == 'Pedra' and computador == 'Tesoura':
    print('Jogador venceu'.center(40))
    print(f'Computador: {computador} | Jogador: {jogador}')
elif jogador == 'Pedra' and computador == 'Pedra':
    print('Empate'.center(40))
    print(f'Computador: {computador} | Jogador: {jogador}')
# situacao papel ----------------------------------------------
elif jogador == 'Papel' and computador == 'Tesoura':
    print('Jogador venceu'.center(40))
    print(f'Computador: {computador} | Jogador: {jogador}')
elif jogador == 'Papel' and computador == 'Pedra':
    print('Computador venceu'.center(40))
    print(f'Computador: {computador} | Jogador: {jogador}')
elif jogador == 'Papel' and computador == 'Papel':
    print('Empate'.center(40))
    print(f'Computador: {computador} | Jogador: {jogador}')
# situacao tesoura ----------------------------------------------
elif jogador == 'Tesoura' and computador == 'Papel':
    print('Jogador venceu'.center(40))
    print(f'Computador: {computador} | Jogador: {jogador}')
elif jogador == 'Tesoura' and computador == 'Pedra':
    print('Computador venceu'.center(40))
    print(f'Computador: {computador} | Jogador: {jogador}')
elif jogador == 'Tesoura' and computador == 'Tesoura':
    print('Empate'.center(40))
    print(f'Computador: {computador} | Jogador: {jogador}')
print(f'{"="*40}')