nota = float(input("Digite a nota do aluno: "))

if nota < 5:
    print("Reprovado")
elif nota < 7:
    print("Recuperação")
else:
    print("Aprovado")