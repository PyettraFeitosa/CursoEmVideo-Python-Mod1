#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = int(input("Digite a distância da sua viagem em quilômetros: "))

if km <= 200:
    val = km * 0.50
    print("O valor cobrado será: {:.2f}" .format(val))
else:
    val = km * 0.45
    print("O valor cobrado será: {:.2f}" .format(val))