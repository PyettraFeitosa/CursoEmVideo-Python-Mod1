#Calculadora simples

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 + num2
mult = num1 * num2
sub = num1 - num2
div = num1 / num2
rest_div = num1 % num2
div_int = num1 // num2

print("A soma vale: {}\nA multiplicação: {}\nA subtração: {}\nA divisão: {}\nO resto da divisão: {}\nA divisão inteira: {}." .format(soma, mult, sub, div, rest_div, div_int), end='')
print("\nO número um é: {}" .format(num1))
print("O número dois é: {}" .format(num2))