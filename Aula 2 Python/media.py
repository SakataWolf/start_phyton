soma = 0
for i in range(4):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma / 5
print("A media é: ", media)