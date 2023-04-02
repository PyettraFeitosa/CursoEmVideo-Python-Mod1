#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input("Digite um valor em metros: "))
print("Em cm: {}\nEm mm: {}" .format(int(medida/0.01), int(medida/0.001)))