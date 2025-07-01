altura = float(input("Digite sua altura: "))
idade = int(input("Digite sua idade: "))

if altura >= 1.60 and idade >= 12:
    print ("Liberado")
elif idade >= 12:
    print ("Liberado por idade, mas altura insuficiente")
elif altura >= 1.60:
    print ("Liberado por altura, mas idade insuficiente")
else:
    print ("Lhe falta ódio")