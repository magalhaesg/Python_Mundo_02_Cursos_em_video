# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
print('ALISTAMENTO MILITAR')
data = date.today()
ano_atual = data.year
ano_nasci = int(input('Digite o ano do seu nascimento: '))
jovem = ano_atual - ano_nasci
if jovem < 18:
    print(f'Ainda não está na hora do seu alistamento.\nPedimos que verifique novamente em {18 - jovem} ano(s) para confirmar se está no tempo correto de alistamento.')
elif jovem > 18:
    print(f'Você já ultrapassou o ano correto para alistamento em {jovem - 18} anos, caso não tenha comparecido a junta militar faça isso o mais breve possível. ')
elif jovem == 18:
    print(f'Esse ano é o ano em que completa 18 anos, pedimos que compareça a junta militar mais próxima.')
else:
    print('Tente novamente.')
