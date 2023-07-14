# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo da triângulo será formado:
# — Equilátero: todos os lados iguais
# — Isósceles: dois lados iguais
# — Escaleno: todos os lados diferentes

print('-=' * 20)
print(f'{" " * 8} Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro seamento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 >= r2 + r3 or r2 >= r1 + r3 or r3 >= r1 + r2:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
else:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if r1 == r2 == r3:
       print('Tipo: Equilátero')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('Tipo: Isósceles')
    elif r1 != r2 != r3:
        print('Tipo: Escaleno')

