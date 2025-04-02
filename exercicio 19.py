lista_compras = ["arroz", "feijão"]

while True:
    resposta = input("Deseja adicionar mais itens na lista? Y/N ")
    if resposta == "Y" or resposta == "y":
        item = input("Digite o item que deseja adicionar: ")
        lista_compras = lista_compras + [item]
    else:
        break

print(lista_compras)