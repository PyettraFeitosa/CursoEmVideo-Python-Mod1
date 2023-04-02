'''
Exercício Python 037: Escreva um programa em Python que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base de conversão: 1 para
binário, 2 para octal e 3 para hexadecimal.
'''

num = int(input("Digite um número para ser convertido: "))
sel = int(input("Escolha uma das opções abaixo:\n1- Binário\n2- Octal\n3- Hexadecimal\n"))

if sel == 1:
    conversor = bin(num)[2:]
    print("O valor {} convertido para a base da seleção {} é: {}" .format(num, sel, conversor))

elif sel == 2:
    conversor = oct(num)[2:]
    print("O valor {} convertido para a base da seleção {} é: {}" .format(num, sel, conversor))

elif sel == 3:
    conversor = hex(num)[2:]
    print("O valor {} convertido para a base da seleção {} é: {}" .format(num, sel, conversor))

else:
    print("Opção inválida!")