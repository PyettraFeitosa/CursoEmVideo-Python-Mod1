#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.


largura = float(input("Digite a largura de parede: "))
altura = float(input("Digite a altura de parede: "))
print("A área em m3 é: {:.2f}\nVocê precisará de {:.2f} litros de tinta para pintá-la." .format(largura*altura, (largura*altura)/2))