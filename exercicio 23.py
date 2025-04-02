conta = float(input("Digite o valor da conta: "))
taxa_gorjeta = float(input("Digite o valor da gorjeta em porcentagem, exemplo 10 seria 10%: "))

gorgeta = conta * (taxa_gorjeta / 100)

conta_final = conta + gorgeta

print(f"Você pagará {conta_final}")