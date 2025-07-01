nomes = []
while True:
    nome = input("Digite um nome (ou 'sair' para parar): ")
    if nome == "sair":
        break
    nomes.append(nome)

print("nomes digitados: ")
for n in nomes:
    print("-", n)