#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math
num = int(input("Digite um número: "))
print("O dobro é: {}\nO triplo é: {}\nA raiz quadrada é: {}" .format(num * 2, num * 3, math.sqrt(num)))