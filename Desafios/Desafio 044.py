# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
#
# - Dinheiro/cheque: 10% de desconto à vista.
# - Cartão de crédito: 5% de desconto à vista.
# - Parcelado em até 3 vezes no cartão: preço normal.
# - Parcelado em 4 vezes ou mais no cartão: 20% de juros.
print(f'{"LOJAS GABS".center(30, " ")}') #centraliza string
valor = float(input('Digite o valor do produto: '))
forma = int(input('Selecione a forma de pagamento\n 1 - Dinheiro/cheque: 10% de desconto à vista.\n 2 - Cartão de crédito: 5% de desconto à vista.\n 3 - Parcelado em até 3 vezes no cartão: preço normal.\n 4 - Parcelado em 4 vezes ou mais no cartão: 20% de juros.\nEscreva o número da opção desejada aqui: '))
if forma == 1:
    print(f'Valor a ser pago: {valor - (valor * 0.1):.2f}')
elif forma == 2:
    print(f'Valor a ser pago: {valor - (valor * 0.05):.2f}')
elif forma == 3:
    parc = int(input('Em quantas vezes deseja parcelar? '))
    if parc <= 3:
        print(f'Valor a ser pago: {valor:.2f} em {parc}x de {valor/parc:.2f}')
    else:
        print('Algo está errado, tente novamente')
elif forma == 4:
    parc = int(input('Em quantas vezes deseja parcelar? '))
    if 3 < parc < 12:
        print(f'Valor a ser pago: {valor + (valor * 0.2):.2f} em {parc}x de {(valor + (valor * 0.2))/parc:.2f}')
    else:
        print('Algo está errado, tente novamente')
else:
    print('Algo está errado, tente novamente')
