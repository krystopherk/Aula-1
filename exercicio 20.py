contagem = 0
lista = []
impar = 0
par = 0

while contagem != 10:
    numero = float(input("Diite um número: "))
    lista = lista + [numero]
    contagem += 1

for numero in lista:
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"A quantidade de números pares é: {par}, e a quantidade de ímpares é: {impar} ")