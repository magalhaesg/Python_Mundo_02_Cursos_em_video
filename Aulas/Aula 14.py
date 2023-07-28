# Comparando o mesmo comando entre for e while
# for c in range(1,10):
#     print(c)
# print('Fim')

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')
"------------------------"
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
'------------------------'
r = 'S'
while r == 'S':
    r = str(input('Quer continuar? [S/N]')).upper()

'------------------------'
par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Numeros pares: {par}\nNumeros impares: {impar}')
