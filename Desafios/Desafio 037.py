# Escreva um programa que leia um número inteiro qualquer a peça para o usuário escolher qual será a besa de conversão:
# 1 - para binário
# 2 - para octal
# 3 - para hexadecimal

# Exibe o cabeçalho do programa
print('CONVERSOR DE BASES')
print('Selecione uma das opções abaixo:')

# Solicita ao usuário a escolha da base de conversão
selecao = int(input('1 - para binário\n2 - para octal\n3 - para hexadecimal\n Opção Selecionada: '))

# Verifica se a opção selecionada é válida (1, 2 ou 3)
if selecao == 1 or selecao == 2 or selecao == 3:
    # Solicita ao usuário o número a ser convertido
    decimal = int(input('Digite o número que deseja converter: '))
    print('Aguarde...')

    # Realiza a conversão de acordo com a opção selecionada
    if selecao == 1:
        resultado = bin(decimal)[2:]  # Converte para binário; aqui utilizei o "[2:]" para remover o prefixo gerado automaticamento pelo python a conversão de números
        print(f'\n O número {decimal} na base binária corresponde a: {resultado}')
    elif selecao == 2:
        resultado = oct(decimal)[2:]  # Converte para octal
        print(f'\n O número {decimal} na base octal corresponde a: {resultado}')
    elif selecao == 3:
        resultado = hex(decimal)[2:]  # Converte para hexadecimal
        print(f'\n O número {decimal} na base hexadecimal corresponde a: {resultado}')
else:
    # Exibe uma mensagem de erro se a opção selecionada for inválida
    print('Opção incorreta, reinicie e tente novamente.')