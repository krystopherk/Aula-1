idade = int(input("Digite sua idade: "))

if idade > 0:
    if idade < 12:
        faixa = "Criança"
    elif idade <= 17:
        faixa = "Adolescente"
    elif idade <= 59:
        faixa = "Adulto"
    else:
        faixa = "Idoso"

    print(f"Você é {faixa}")
    
else:
    print("Digite uma idade válida")

