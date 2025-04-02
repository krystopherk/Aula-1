numero = int(input("Digite o número a ser calculado: "))
primo = True

for i in range(2, numero - 1):
    if numero % i == 0:
        primo = False
        break

if primo:
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} não é primo")
