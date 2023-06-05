# Crie um programa que leia duas notas de um aluno a calcule sua média, mostrando uma mensagam no final, de acordo com a média atingida:
# — Média abaixo de 5.0: REPROVADO
# — Média entre 5.0 e 6.9: RECUPERAÇÃO
# — Média 7.0 ou superior: APROVADO

# Exibe o cabeçalho do programa
print('CALCULO DE MÉDIA')

try:
    # Solicita ao usuário as notas e converte para float
    n1 = float(input('Digite a sua primeira nota: '))
    n2 = float(input('Digite a sua segunda nota: '))

    # Calcula a média das notas
    media = (n1 + n2) / 2

    # Verifica se as notas estão dentro do intervalo válido
    if n1 >= 10.01 or n2 >= 10.01:
        print('Ocorreu um erro. Pedimos que tente novamente\nLembre-se que a nota máxima para cada avaliação e a média são de no máximo 10 pontos.')
    else:
        # Verifica a categoria do aluno com base na média
        if media < 5.0:
            print(f'REPROVADO\nSua nota foi {media:.1f}')
        elif media >= 5.0 and media <= 6.9:
            print(f'RECUPERAÇÃO\nSua média foi {media:.1f}')
        elif media >= 7.0:
            print(f'APROVADO\nSua média foi {media:.1f}')

except ValueError:
    # Captura exceção caso o usuário digite um valor não numérico
    print('Ocorreu um erro. Certifique-se de inserir apenas números.')
