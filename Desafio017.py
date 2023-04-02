#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

co = float(input("Digite o valor do cateto oposto do triângulo: "))
ca = float(input("Digite o valor do cateto adjacente do triângulo: "))

h = math.pow(co, 2) + math.pow(ca, 2)

print("O valor da hipotenusa é: {:.2f}" .format(math.sqrt(h)))