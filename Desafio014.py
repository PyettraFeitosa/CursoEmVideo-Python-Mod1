#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input("Digite a temperatura em ºC: "))
print("A temperatura é: {:.1f} ºF" .format((temp * (9/5)) + 32))