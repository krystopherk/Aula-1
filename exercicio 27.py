# Peça ao usuário para inserir as notas de um aluno em uma lista. 
# Após cadastrar todas as notas, calcule e exiba:
# • A maior nota.
# • A menor nota.
# • A média das notas.
notas = []

def cadastrar(lista, valor):
    lista.append(valor)
    print(f"Notas atuais: {lista}")

def exibir(lista):
    print(f"Notas atuais: {lista}")

def excluir(lista, indice):
    if indice in lista:
        lista.remove(indice)
        print(f"Notas atuais: {lista}")
    else:
        print("Nota não encontrada")

while True:
    print("Deseja executar qual ação?")
    print("1 - Adicionar nota")
    print("2 - Visualizar notas")
    print("3 - Excluir nota")
    print("4 - Calcular")
    resposta = input("Digite o número correspondente a ação: ")

    if resposta == "1":
        try:
            valor = float(input("Digite o item a ser adicionado: "))
            cadastrar(notas, valor)
        except:
            print("Digite um valor válido")
    elif resposta == "2":
        exibir(notas)
    elif resposta == "3":
        try:
            valor = float(input("Digite o item a ser excluído: "))
            excluir(notas, valor)
        except:
            print("Digite um valor válido")
    elif resposta == "4":
        print("Encerrando...")
        break
    else:
        print("Resposta inválida")

numero_notas = len(notas)
soma_notas = sum(notas)
menor_nota = min(notas)
maior_nota = max(notas)

if notas:
    print(f"Média: {soma_notas / numero_notas}")
    print(f"Nota maior: {maior_nota}")
    print(f"Nota menor: {menor_nota}")
else:
    print("Nenhuma nota encontrada")