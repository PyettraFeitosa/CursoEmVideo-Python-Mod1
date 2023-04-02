#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a1 = input("Digite o primeiro nome: ")
a2 = input("Digite o segundo nome: ")
a3 = input("Digite o terceiro nome: ")
a4 = input("Digite o quarto nome: ")

lista = [a1, a2, a3, a4]
random.shuffle(lista)
print("O escolhido foi: {}" .format(lista))