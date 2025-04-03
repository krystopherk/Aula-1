n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação a ser realizada (+, -, *, /): ")

if operacao == "+":
    resultado = n1 + n2
elif operacao == "-":
    resultado = n1 - n2
elif operacao == "*":
    resultado = n1 * n2
elif operacao == "/":
    if n2 == 0:
        resultado = "Impossível dividir por 0"
    else:
        resultado = n1 / n2
else:
    resultado = "Operação inválida"

print(resultado)
