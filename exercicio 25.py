lista = []

def cadastrar(lista, valor):
    lista.append(valor)
    print(f"Lista atual: {lista}")

def exibir(lista):
    print(f"Lista atual: {lista}")

def excluir(lista, indice):
    if indice in lista:
        lista.pop(indice)
        print(f"Lista atual: {lista}")
    else:
        print("Item não encontrado")
while True:
    print("Deseja executar qual ação?")
    print("1 - Adicionar item a lista")
    print("2 - Visualizar lista completa")
    print("3 - Excluir item")
    print("4 - Encerrar")
    resposta = input("Digite o número correspondente a ação: ")
    if resposta == "1":
        valor = int(input("Digite o valor a ser adicionado: "))
        cadastrar(lista, valor)
    elif resposta == "2":
        exibir(lista)
    elif resposta == "3":
        valor = int(input("Digite o item a ser excluído: "))
        excluir(lista, valor)
    elif resposta == "4":
        print("Encerrando...")
        break
    else:
        print("Resposta inválida")