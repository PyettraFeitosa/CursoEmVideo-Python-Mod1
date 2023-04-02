#Calculo de notas de um aluno

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3)/3

if media >= 7.0:
    print("Sua média é: {:.1f}. Você foi aprovado!" .format(media))

elif media < 7.0 and media > 5.0:
    print("Sua média é: {:.1f}. Você está em recuperação!" .format(media))
    
else:
    print("Sua média é {:.1f}. Você foi reprovado!" .format(media))