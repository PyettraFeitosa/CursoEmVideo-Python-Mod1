'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu 
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
* IMC abaixo de 18,5: Abaixo do Peso
* Entre 18,5 e 25: Peso Ideal
* 25 até 30: Sobrepeso
* 30 até 40: Obesidade
* Acima de 40: Obesidade Mórbida'''

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura em m: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("IMC igual a: {:.2f}. Abaixo do peso." .format(imc))
elif imc < 25.0:
    print("IMC igual a: {:.2f}. Peso ideal." .format(imc))
elif imc < 30.0:
    print("IMC igual a: {:.2f}. Sobrepeso." .format(imc))
elif imc < 40.0:
    print("IMC igual a: {:.2f}. Obesidade" .format(imc))
else:
    print("Obesidade mórbida")
