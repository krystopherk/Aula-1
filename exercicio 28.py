# Crie um programa que gerencie um estoque de produtos:
# • O usuário deve poder adicionar produtos (nome e quantidade).
# • Permita a busca por um produto específico e exiba sua quantidade.
# • Ofereça a opção de atualizar a quantidade de um produto.
# • Exiba o estoque completo ao final.

import pandas as pd
# global estoque
estoque = pd.DataFrame(columns=["Produto", "Quantidade"])

def adicionar_produto():
    nome = input("Nome do produto: ").strip()
    if nome in estoque["Produto"].values:
        print("Produto já existe. Use a opção de atualizar.")
        return
    try:
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Quantidade inválida.")
        return
    estoque.loc[len(estoque)] = [nome, quantidade]
    print("Produto adicionado com sucesso!")

def buscar_produto():
    nome = input("Nome do produto para buscar: ").strip()
    resultado = estoque[estoque["Produto"] == nome]
    if not resultado.empty:
        print(f"{nome}: {int(resultado['Quantidade'].values[0])} unidades")
    else:
        print("Produto não encontrado.")

def atualizar_quantidade():
    nome = input("Nome do produto para atualizar: ").strip()
    if nome in estoque["Produto"].values:
        try:
            nova_qtd = int(input("Nova quantidade: "))
        except ValueError:
            print("Quantidade inválida.")
            return
        # global estoque
        estoque.loc[estoque["Produto"] == nome, "Quantidade"] = nova_qtd
        print("Quantidade atualizada.")
    else:
        print("Produto não encontrado.")

def exibir_estoque():
    print("\n📦 Estoque Completo:")
    print(estoque.to_string(index=False))

while True:
    print("\n--- MENU ESTOQUE ---")
    print("1. Adicionar produto")
    print("2. Buscar produto")
    print("3. Atualizar quantidade")
    print("4. Exibir estoque")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        buscar_produto()
    elif opcao == "3":
        atualizar_quantidade()
    elif opcao == "4":
        exibir_estoque()
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
