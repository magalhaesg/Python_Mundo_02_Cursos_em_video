# -*- coding: utf-8 -*-
'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado(inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
num = int(input("Que valor você quer sacar? \n"))
cedulas = [50, 20, 10, 1]

Regras:
Divida o valor (x) pela nota de valor mais alto (50) para obter a quantidade máxima possível dessa nota.
Em seguida, obtenha o resto da divisão por 50, que representa o valor que ainda precisa ser alcançado.
Repita os passos 1 e 2 para cada uma das outras notas (20, 10 e 1) até que o valor restante seja zero.
'''

saque = int(input("Que valor você quer sacar? "))
notas = [50, 20, 10, 1]
cedulas = [] #lista vazia para serem alocadas as quantidades de cedulas
cont = 0 #criando e definindo contador

for i in notas: # i percorrendo a lista notas [50, 20, 10, 1] = [0, 1, 2, 3]
    cedulas.append(saque//i) #divisao inteira entre valor do saque por valor da cédula (50, 20, 10, 1)
    saque = saque % i #saque tem seu valor atualizado para o resto da dividão entre saque e valor da cedula
    print(f"{cedulas[cont]} notas de R${i}") #imprime a quantidade de cedulas usando a posição de lista criada pelo contador abaixo e o valor da cedula
    cont += 1 #contador responsavel por ajudar na impressão do numero de cedulas