def coletar_dados():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    return nome, idade

def verificar_maioridade(idade):
    
    if idade >= 18:
     return True

    else:
     return False

def mostrar_resultado(nome, maioridade):

   if maioridade:
      print(f"{nome}, você é maior de idade e pode prosseguir!")

   else:
      print(f"{nome}, você ainda não pode prosseguir. Lhe falta ódio 🤠")
