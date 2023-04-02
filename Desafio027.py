#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Digite seu nome completo: ").strip()
separado = nome.split()
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é: {}" .format(separado[0]))
print("Seu último nome é: {}" .format(separado[len(separado)-1]))
