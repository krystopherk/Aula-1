senha_atual = 0

while True:
    pergunta = input("Deseja chamar o próximo cliente? Y/N ")

    if pergunta == "Y" or pergunta == "y":
        senha_atual += 1
        print(f"Número {senha_atual} por favor se dirija ao caixa.")
    else:
        print("Atendimento encerrado por hoje, obrigado")
        break