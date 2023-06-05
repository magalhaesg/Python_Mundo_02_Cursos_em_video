# Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem na tela:
# -o primeiro valor é maior
# -o segundo valor é maior
# - os dois são iguais

print('Vamos comparar dois números!')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'O primeiro número ({n1}) é maior que o segundo ({n2})')
elif n2 > n1:
    print(f'O Segundo número ({n2}) é maior que o primeiro ({n1})')
else:
    print(f'Os números são iguais ({n1} & {n2})')
