# Peça ao usuário para inserir 10 palavras em uma lista.
# • Crie uma nova lista contendo apenas palavras que começam com uma vogal.
# • Exiba a lista original e a filtrada

lista = []

while True:
    palavra = input("Digite uma palavra: ")
    lista.append(palavra)
    if len(lista) == 10:
        break

lista_vogais = []

for palavra in lista:
    if palavra[0].lower() in ["a", "b", "c", "d", "e"]:
        lista_vogais.append(palavra)

print(lista)
print(lista_vogais)