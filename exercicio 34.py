# Implemente um programa para gerenciar uma agenda de compromissos:
# • O usuário deve poder adicionar compromissos e suas datas.
# • Exiba os compromissos cadastrados.
# • Ofereça a opção de buscar compromissos por data.
# • Exiba todos os compromissos ordenados pela data.

from datetime import datetime
import pandas as pd

agenda = pd.DataFrame(columns=["Data", "Compromisso"])

def adicionar_compromisso():
    data = input("Data do compromisso (dd/mm/yyyy): ")

    try:
        data = datetime.strptime(data, "%d/%m/%Y")
        compromisso = input("Digite seu compromisso: ")
        agenda.loc[len(agenda)] = [data, compromisso]
        print("Compromisso adicionado com sucesso!")

    except ValueError:
        print("Data inválida")

def buscar_compromisso():
    data = input("Data a ser buscada (dd/mm/yyyy): ")
    try:
        data = datetime.strptime(data, "%d/%m/%Y")
        resultado = agenda[agenda["Data"] == data]
        if not resultado.empty:
            print(resultado)
        else:
            print("Data não encontrada.")
    except ValueError:
        print("Data inválida")


def exibir_agenda():
    print(agenda)

def exibir_ordem():
    agenda["Data"] = pd.to_datetime(agenda["Data"])  # Garante que a coluna seja tratada como data
    agenda_ordenada = agenda.sort_values(by="Data")
    print(agenda_ordenada)

while True:
    print("\n--- MENU agenda ---")
    print("1. Adicionar compromiso")
    print("2. Buscar data")
    print("3. Exibir agenda")
    print("4. Exibir ordenado por data")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_compromisso()
    elif opcao == "2":
        buscar_compromisso()
    elif opcao == "3":
        exibir_agenda()
    elif opcao == "4":
        exibir_ordem()
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
