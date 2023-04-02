#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input("Digite a velocidade do carro: "))

if vel > 80:
    multa = (vel - 80) * 7
    print("Seu carro foi multado em R$ {}" .format(multa))

else:
    print("Você está dentro dos limites de velocidade.")