n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2:
    if n1 > n3:
        print(f"{n1} é maior")
    else:
        print(f"{n3} é maior")

elif n3 > n1:
    if n3 > n2:
        print(f"{n3} é maior")
    else:
        print(f"{n2} é maior")

elif n1 > n3:
    if n1 > n2:
        print(f"{n1} é maior")
    else:
        print(f"{n2} é maior")

else:
    print("Todos são iguais")



    