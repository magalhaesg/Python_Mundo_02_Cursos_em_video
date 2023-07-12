# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
#
# - Dinheiro/cheque: 10% de desconto à vista.
# - Cartão de crédito: 5% de desconto à vista.
# - Parcelado em até 3 vezes no cartão: preço normal.
# - Parcelado em 4 vezes ou mais no cartão: 20% de juros.

valor = float(input('Digite o valor do produto: '))
forma = int(input('Selecione a forma de pagamento\n 1 - Dinheiro/cheque: 10% de desconto à vista.\n 2 - Cartão de crédito: 5% de desconto à vista.\n 3 - Parcelado em até 3 vezes no cartão: preço normal.\n 4 - Parcelado em 4 vezes ou mais no cartão: 20% de juros.\n  Escreva o número da opção desejada aqui: '))
if forma == 1:
    print(f'Valor a ser pago: {valor - (valor * 0.1)}')
elif forma == 2:
    print(f'Valor a ser pago: {valor - (valor * 0.05)}')
elif forma == 3:
    print(f'Valor a ser pago: {valor}')
elif forma == 4:
    print(f'Valor a ser pago: {valor + (valor * 0.2)}')