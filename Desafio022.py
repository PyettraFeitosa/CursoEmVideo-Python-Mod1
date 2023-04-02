#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = input("Digite seu nome: ")

nome_up = nome.upper()
nome_down = nome.lower()
nome_whitout_space = nome.replace(" ", "")
nome_size = len(nome_whitout_space)
nome_separate = nome.split()
nome_size2 = len(nome_separate[0])

print(nome_up)
print(nome_down)
print(nome_whitout_space)
print(nome_size)
print(nome_separate)
print(nome_size2)