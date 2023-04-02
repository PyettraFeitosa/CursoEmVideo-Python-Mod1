'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
* à vista dinheiro/cheque: 10% de desconto
* à vista no cartão: 5% de desconto
* em até 2x no cartão: preço formal 
* 3x ou mais no cartão: 20% de juros'''

valor = float(input("Digite o valor do produto: "))
sel = int(input("Qual a forma de pagamento?\n1- À vista (dinheiro/pix)\n2- À vista no cartão\n3- Em até 2x no cartão\n4- 3x ou mais no cartão\n"))

if sel == 1:
    valor_atual = valor - (valor * 0.1)
    print("À vista com 10%% de desconto o valor final é igual a: R$ {:.2f}." .format(valor_atual))
elif sel == 2:
    valor_atual = valor - (valor * 0.05)
    print("À vista com 5%% de desconto o valor final é igual a: R$ {:.2f}." .format(valor_atual))
elif sel == 3:
    print("Em até 2x vezes no cartão o valor não sofre alterações e é igual a: R$ {:.2f}." .format(valor))
elif sel == 4:
    valor_atual = valor + (valor * 0.2)
    print("Em 3x vezes ou mais no cartão o valor sofre alterações de juros e é igual a: R$ {:.2f}." .format(valor_atual))
else:
    print("Opção inválida!")