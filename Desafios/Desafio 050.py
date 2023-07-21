# -*- coding: utf-8 -*-
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o número digitado for ímpar, desconsidere-o.

num_par = 0
num_impar = 0
for i in range(0, 6):
    num = int(input(f'Digite um número {i+1} de 6: '))
    if num % 2 == 0:
        num_par += num
    else:
        num_impar += num
print(f'A soma dos números impares corresponde a {num_impar} e dos pares a {num_par}.')