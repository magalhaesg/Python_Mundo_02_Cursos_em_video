# Crie um programa que faça o computador jogar Jokanpô com você.

import random
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
    input_jogador = input('Digite sua escolha: ')
    jogador = input_jogador.capitalize()
# situacao pedra ----------------------------------------------
if jogador == 'Pedra' and computador == 'Papel':
    print('Computador venceu')
    print(f'Computador: {computador} | Jogador: {jogador}')
elif jogador == 'Pedra' and computador == 'Tesoura':
    print('Jogador venceu')
    print(f'Computador: {computador} | Jogador: {jogador}')
elif jogador == 'Pedra' and computador == 'Pedra':
    print('Empate')
    print(f'Computador: {computador} | Jogador: {jogador}')
# situacao papel ----------------------------------------------
elif jogador == 'Papel' and computador == 'Tesoura':
    print('Jogador venceu')
    print(f'Computador: {computador} | Jogador: {jogador}')
elif jogador == 'Papel' and computador == 'Pedra':
    print('Computador venceu')
    print(f'Computador: {computador} | Jogador: {jogador}')
elif jogador == 'Papel' and computador == 'Papel':
    print('Empate')
    print(f'Computador: {computador} | Jogador: {jogador}')
# situacao tesoura ----------------------------------------------
elif jogador == 'Tesoura' and computador == 'Papel':
    print('Jogador venceu')
    print(f'Computador: {computador} | Jogador: {jogador}')
elif jogador == 'Tesoura' and computador == 'Pedra':
    print('Computador venceu')
    print(f'Computador: {computador} | Jogador: {jogador}')
elif jogador == 'Tesoura' and computador == 'Tesoura':
    print('Empate')
    print(f'Computador: {computador} | Jogador: {jogador}')