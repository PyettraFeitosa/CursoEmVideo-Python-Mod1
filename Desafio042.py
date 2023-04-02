'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, 
acrescentando o recurso de mostrar que tipo de triângulo será formado:
* EQUILÁTERO: todos os lados iguais
* ISÓSCELES: dois lados iguais, um diferente
* ESCALENO: todos os lados diferentes'''

r1 = int(input("Digite o valor da primeira reta: "))
r2 = int(input("Digite o valor da segunda reta: "))
r3 = int(input("Digite o valor da terceira reta: "))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print("É triângulo!")
    if r1 == r2 == r3:
        print("O triângulo é Equilátero.")
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print("O triângulo é Isósceles.")
    else:
        print("O triângulo é Escaleno.")
else:
    print("Não é triângulo!")