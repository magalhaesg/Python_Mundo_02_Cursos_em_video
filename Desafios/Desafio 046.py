# -*- coding: utf-8 -*-
#Faça um programa Faça um programa que mostre uma contagem na tela regressiva  para o estouro de fogos de artifício. Indo de 10 ate O, com uma pausa da segundo entre eles.
import time
import os

for i in range(10, 0, -1):
    time.sleep(0.9)
    print(f'{i}')
    os.system("cls")  # comando limpa tela
print('FELIZ ANO NOVOOO!')
