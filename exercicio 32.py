# Peça ao usuário que insira as temperaturas registradas durante uma semana.
# • Exiba a maior e a menor temperatura.
# • Informe a média semanal.
# • Exiba os dias em que a temperatura foi maior que a média.

dias_semana = []
temperaturas = []
dia = 1

while True:
    try:
        temp = float(input(f"Digite a temperatura do {dia}º dia da semana:"))
        dias_semana.append(dia)
        temperaturas.append(temp)
        dia += 1

        if len(temperaturas) == 7:
            break

    except:
        print("Digite uma temperatura válida")

maior_temp = max(temperaturas)
menor_temp = min(temperaturas)
indice = temperaturas.index(maior_temp)
dia_mais_quente = dias_semana[indice]
media = sum(temperaturas) / len(temperaturas)

print(f"Maior temperatura registrada: {maior_temp}, menor temperatura registrada: {menor_temp}")
print(f"Média de temperatura: {round(media, 2)}")
print(f"O {dia_mais_quente}º foi o dia mais quente com {maior_temp} graus")