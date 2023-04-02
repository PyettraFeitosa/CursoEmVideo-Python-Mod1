#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input("Digite um ângulo: "))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print("O seno é: {:.2f}\nO cosseno é: {:.2f}\nA tangente é: {:.2f}" .format(sen, cos, tg))