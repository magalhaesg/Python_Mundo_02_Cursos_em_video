# A Confederação Nacional da Natação precisa da um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# — Até 9 anos: MIRIM
# — até 14 anos: INFANTIL
# — até 19 anos: JUNIOR
# — até 20 anos: SÊNIOR
# — Acima: MASTER

from datetime import date
data = date.today()
ano = data.year
print('DIVISOR DE CATEGORIAS - CONFEDERAÇÃO BRASILEIRA DE NATAÇÃO')
nascimento = int(input('Digite o ano de nascimento: '))
idade = ano-nascimento
if nascimento < 1920 or nascimento > ano:
    print(f'Ocorreu um erro ao digitar. Entre com uma data válida entre 1950 e {ano}')
else:
    if idade <= 9:
        print(f'A idade de {idade} anos se qualifica como MIRIM')
    elif idade <= 14:
        print(f'A idade de {idade} anos se qualifica como INFANTIL')
    elif idade <= 19:
        print(f'A idade de {idade} anos se qualifica como JUNIOR')
    elif idade == 20:
        print(f'A idade de {idade} anos se qualifica como SÊNIOR')
    elif idade > 20:
        print(f'A idade de {idade} anos se qualifica como MASTER')
    else:
        print('Algo está errado, tente novamente.')
