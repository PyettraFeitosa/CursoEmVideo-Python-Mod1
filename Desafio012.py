#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

val = float(input("Digite o valor do produto: "))
print("Seu novo valor é: {:.2f}" .format(val - val*0.05))