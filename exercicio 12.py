usuario_correto = "Krystopher"
senha_correta = "K12345678*"

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login efetuado com sucesso!")
else:
    print("Login ou usuário incorretos!")