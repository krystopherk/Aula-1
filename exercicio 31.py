# Solicite ao usuário que insira 10 números em uma lista.
# • Exiba os números em ordem crescente.
# • Exiba os números em ordem decrescente.
# • Exiba apenas os valores pares.
numeros = []

while True:
    if len(numeros) < 10:
        try:
            numero = int(input("Digite um número a ser inserido: "))
            numeros.append(numero)
        except:
            print("Digite um número inteiro válido")
    else:
        print("10 números atingidos, calculando...")
        break

print()
numeros.sort()
print(f"Ordem crescente: {numeros}")
numeros.sort(reverse=True)
print(f"Ordem decrescente: {numeros}")
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(f"Números pares: {pares}")