usuario_correto = "Krystopher"
senha_correta = "admin123"
contador = 0

while True:
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login efetuado com sucesso!")
        break
    else:
        print("Usuário ou senha incorretos.")
        contador += 1
        if contador == 3:
            print("Limite de tentativas alcançado.")
            break