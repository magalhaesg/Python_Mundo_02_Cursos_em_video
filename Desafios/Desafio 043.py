# Desenvolva uma lógica que calcule o peso e a altura de uma pessoa e mostre seu IMC (Índice de Massa Corporal) e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18,5: Peso abaixo do normal
# - 18,5 a 25: Peso normal
# - 25 a 30: Sobrepeso
# - 30 a 40: Obesidade
# - Acima de 40: Obesidade mórbida

print('-=' * 20)
print(f'{" " * 12}Cálculo de IMC{" " * 12}')
print('-=' * 20)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso/(altura*altura)
print(f'Seu IMC corresponde a {IMC:.2f}')
if  IMC < 17:
    print('Muito abaixo do peso')
elif 17 <= IMC <= 18.49:
    print('Abaixo do peso')
elif 18.5 <= IMC <= 24.99:
    print('Peso normal')
elif 25 <= IMC <= 29.99:
    print('Sobrepeso')
elif 30 <= IMC <= 34.99:
    print('Obesidade I')
elif 35 <= IMC <= 39.99:
    print('Obesidade II')
elif IMC > 40:
    print('Obesidade mórbida')
else:
    print('Erro')
