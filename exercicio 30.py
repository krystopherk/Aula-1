# Crie um programa que simule um sorteio:
# • Adicione os nomes dos participantes em uma lista.
# • Utilize a função random.choice() para escolher um ganhador aleatório.
# • Exiba o nome do vencedor.

import random

pessoas = []

def cadastrar(lista, valor):
    lista.append(valor)
    print("Pessoa cadastrada com sucesso")

while True:
    print("Deseja executar qual ação?")
    print("1 - Adicionar pessoa")
    print("2 - Encerrar")
    resposta = input("Digite o número correspondente a ação: ")

    if resposta == "1":
        nome = input("Digite o nome da pessoa: ")
        cadastrar(pessoas, nome)

    elif resposta == "2":
        print("Encerrando...")
        break
    else:
        print("Resposta inválida")

print(f"A pessoa sortuda é: {random.choice(pessoas)}")