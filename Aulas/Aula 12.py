nome = str(input('Qual o seu nome? ')).capitalize()
if nome == 'Gabriel':
    print('Olá senhor')
elif nome == 'Alice' or nome == 'Bárbara' or nome == 'Marilia':
    print('Cai fora!!!!!')
else:
    print('Não te conheço')
print(f'Tenha um bom dia, {nome}!')