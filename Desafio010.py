#vCrie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Valor do dólar pré-setado de R$3,27

val = float(input("Quanto você tem na carteira em R$? "))
print("Você pode comprar {:.2f} dolares." .format(val/3.27))