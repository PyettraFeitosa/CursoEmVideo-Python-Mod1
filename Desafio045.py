'''Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint

sel = int(input("Faça a sua escolha:\n\n1- Pedra\n2- Papel\n3- Tesoura\n"))

atv = randint(1,3)

if sel == atv:
    print("Empatou.")
elif sel == 1 and atv == 2:
    print("Papel embrulha pedra. O computador venceu!")
elif sel == 1 and atv == 3:
    print("Pedra esmaga tesoura. Você venceu!")
elif sel == 2 and atv == 1:
    print("Papel embrulha pedra. Você venceu!")
elif sel == 2 and atv == 3:
    print("Tesoura corta papel. O computador venceu!")
elif sel == 3 and atv == 1:
    print("Pedra esmaga tesoura. O computador venceu!")
elif sel == 3 and atv == 2:
    print("Tesoura corta papel. Você venceu!")
else:
    print("Opção inválida!")