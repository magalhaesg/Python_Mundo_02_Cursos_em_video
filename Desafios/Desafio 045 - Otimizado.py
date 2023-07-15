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

print(f'Computador: {computador} | Jogador: {jogador}')

if jogador == computador:
    print('Empate')
elif (jogador == 'Pedra' and computador == 'Tesoura') or (jogador == 'Papel' and computador == 'Pedra') or (jogador == 'Tesoura' and computador == 'Papel'):
    print('Jogador venceu')
else:
    print('Computador venceu')
    print('test')