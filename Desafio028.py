#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = int(input("Digite um número entre 0 e 5: "))

sort = random.randint(0, 5)

if num == sort:
    print("Uau, você acertou!")

else:
    print("O número sorteado foi: {}. Tente de novo!" .format(sort))