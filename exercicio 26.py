# Implemente um programa onde o usuário pode: Adicionar itens a uma lista de compras. 
# Exibir todos os itens na lista. Remover um item específico, caso o usuário deseje. 
# Finalizar o programa exibindo a lista final.

lista = []

def cadastrar(lista, valor):
    lista.append(valor)
    print(f"Lista atual: {lista}")

def exibir(lista):
    print(f"Lista atual: {lista}")

def excluir(lista, indice):
    lista.remove(indice)
    print(f"Lista atual: {lista}")
while True:
    print("Deseja executar qual ação?")
    print("1 - Adicionar item a lista")
    print("2 - Visualizar lista completa")
    print("3 - Excluir item")
    print("4 - Encerrar")
    resposta = input("Digite o número correspondente a ação: ")
    if resposta == "1":
        valor = input("Digite o item a ser adicionado: ")
        cadastrar(lista, valor)
    elif resposta == "2":
        exibir(lista)
    elif resposta == "3":
        valor = input("Digite o item a ser excluído: ")
        excluir(lista, valor)
    elif resposta == "4":
        print("Encerrando...")
        break
    else:
        print("Resposta inválida")