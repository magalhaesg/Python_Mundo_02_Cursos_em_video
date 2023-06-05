# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. #
# O programa vai perguntar o valor da casa, o salário do comprador, e em quantos anos ele vai pagar.#
# Calcula o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o enpréstimo será negado. #

print('Imobiliária Vida - Sistema de empréstimo bancário')
salario = float(input('Digite seu salário: R$'))
casa = float(input('Digite o valor da casa: R$'))
parc = int(input('Digite em quantos anos deseja pagar: '))
valor = casa/(parc*12)
limite_prestacao = (30 / 100) * salario
print('Processando...')
if valor > limite_prestacao:
    print('EMPRÉSTIMO NEGADO\n O valor da parcela excede à 30% do valor do seu salário\n Pedimos que entre em contato com um dos nossos agentes imobiliários ')
else:
    print(f'EMPRÉSTIMO APROVADO\n O valor das suas parcelas em {parc*12} vezea será no valor de {valor:.2f} mensais :) .')