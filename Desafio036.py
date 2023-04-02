'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

val_casa = float(input("Qual o valor da casa: "))
val_salario = float(input("Qual o valor do seu salário: "))
anos = int(input("Em quantos anos você deseja pagar essa casa: "))

meses = anos * 12
prestacao = val_casa / meses
salario = val_salario * 0.3

if prestacao <= salario:
    print("Você irá pagar o valor de R$ {:.2f} durante {} meses." .format(prestacao, meses))
else:
    print("O valor da parcela é de R$ {:.2f} e isso é mais do que 30%% do seu salário.")